from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import integration_1
import converter_fifo, converter, lj92_pipeline_fifo
import constraints
import config

class Integration2(Elaboratable):

	def __init__(self, config, cons):

		assert config['bit_depth'] >= 1
		assert config['pixels_per_cycle'] >= 1

		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']
		enc_out_bits = min(31, 16+self.bd) * self.ps

		#pixels in
		self.pixels_in = Array(Signal(self.bd, name="pixel_in") for _ in range(self.ps))

		self.enc_out = Signal(enc_out_bits)
		self.enc_out_ctr = Signal(max=enc_out_bits+1)
		self.latch_output = Signal(1)

		#valid in & out
		self.nready = Signal(1)
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)
		self.out_end = Signal(1)

		self.integration_1 = integration_1.Integration1(config, cons)
		self.lj92_pipeline_fifo = lj92_pipeline_fifo.LJ92PipelineFifo(config, cons)
		self.converter = converter.Converter(config, cons)
		self.converter_fifo = converter_fifo.ConverterFifo(config, cons)

		self.ios = \
			[pixel_in for pixel_in in self.pixels_in] + \
			[self.enc_out, self.enc_out_ctr] + \
			[self.latch_output, self.nready] + \
			[self.valid_in, self.valid_out] + \
			[self.integration_1.fend_out]
			
	def elaborate(self, platform):

		m = Module()

		m.submodules.integration_1 = integration_1 = self.integration_1
		m.submodules.lj92_pipeline_fifo = lj92_pipeline_fifo = self.lj92_pipeline_fifo
		m.submodules.converter = converter = self.converter
		m.submodules.converter_fifo = converter_fifo = self.converter_fifo

		#integration_1 and this
		m.d.comb += [integ_pixel_in.eq(pixel_in) for integ_pixel_in, pixel_in in zip(integration_1.pixels_in, self.pixels_in)]
		m.d.comb += [
			integration_1.valid_in.eq((self.valid_in == 1) & (lj92_pipeline_fifo.close_full == 0)),
		]

		# integration_1 and lj92_pipeline_fifo
		m.d.comb += [
			lj92_pipeline_fifo.enc_in.eq(integration_1.enc_out),
			lj92_pipeline_fifo.enc_in_ctr.eq(integration_1.enc_out_ctr),
			lj92_pipeline_fifo.valid_in.eq(integration_1.valid_out),
			lj92_pipeline_fifo.in_end.eq(integration_1.end_out),
			self.nready.eq(lj92_pipeline_fifo.close_full),
		]

		# lj92_pipeline_fifo and converter
		m.d.comb += [
			lj92_pipeline_fifo.latch_output.eq(converter.latch_output),
			converter.enc_out.eq(lj92_pipeline_fifo.enc_out),
			converter.enc_out_ctr.eq(lj92_pipeline_fifo.enc_out_ctr),
			converter.out_end.eq(lj92_pipeline_fifo.out_end),
			converter.valid_out.eq(lj92_pipeline_fifo.valid_out),
		]

		# converter and converter_fifo
		m.d.comb += [
			converter_fifo.enc_in.eq(converter.enc_in),
			converter_fifo.enc_in_ctr.eq(converter.enc_in_ctr),
			converter_fifo.in_end.eq(converter.in_end),
			converter_fifo.valid_in.eq(converter.valid_in),
			converter.close_full.eq(converter_fifo.close_full),
		]

		# converter_fifo and this
		m.d.comb += [
			self.enc_out.eq(converter_fifo.enc_out),
			self.enc_out_ctr.eq(converter_fifo.enc_out_ctr),
			self.valid_out.eq(converter_fifo.valid_out),
			self.out_end.eq(converter_fifo.out_end),
			converter_fifo.latch_output.eq(self.latch_output),
		]

		return m


if __name__ == "__main__":
	config = {
		"bit_depth" : 12,
		"pixels_per_cycle": 4,
		"LJ92_fifo_depth": 128,
		"converter" : 48,
		"converter_fifo_depth": 256,
		"predictor_function": 1,
		"num_of_components": 4,
		"axi_lite_debug": False,
		"support_axi_lite": False,
	}
	cons = constraints.Constraints()
	d = Integration2(config, cons)
	main(d, ports=d.ios)