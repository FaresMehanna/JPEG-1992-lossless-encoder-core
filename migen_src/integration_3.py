from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import vbits_to_cbits
import integration_2
import constraints

class Integration3(Elaboratable):

	def __init__(self, config, cons):

		assert config['bit_depth'] >= 1
		assert config['pixels_per_cycle'] >= 1
		assert config['out_bits'] >= 1

		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']
		self.out_bits = config['out_bits']

		#pixels in
		self.pixels_in = Array(Signal(self.bd, name="pixel_in") for _ in range(self.ps))

		#data out
		self.data_out = Signal(self.out_bits)

		#signals
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)
		self.end_out = Signal(1)
		self.nready = Signal(1)
		self.busy_in = Signal(1)

		self.integration_2 = integration_2.Integration2(config, cons)
		self.vbits_to_cbits = vbits_to_cbits.VBitsToCBits(config, cons)

		self.ios = \
			[self.valid_in, self.valid_out, self.end_out] + \
			[self.data_out, self.busy_in, self.nready] + \
			[pixel_in for pixel_in in self.pixels_in] + \
			[self.integration_2.integration_1.fend_out]

	def elaborate(self, platform):

		m = Module()

		m.submodules.integration_2 = integration_2 = self.integration_2
		m.submodules.vbits_to_cbits = vbits_to_cbits = self.vbits_to_cbits

		#integration_2 and this
		m.d.comb += [integ_pixel_in.eq(pixel_in) for integ_pixel_in, pixel_in in zip(integration_2.pixels_in, self.pixels_in)]
		m.d.comb += [
			integration_2.valid_in.eq(self.valid_in),
		]

		# converter_fifo and vbits_to_cbits
		m.d.comb += [
			integration_2.latch_output.eq(vbits_to_cbits.latch_input),
			vbits_to_cbits.enc_in.eq(integration_2.enc_out),
			vbits_to_cbits.enc_in_ctr.eq(integration_2.enc_out_ctr),
			vbits_to_cbits.in_end.eq(integration_2.out_end),
			vbits_to_cbits.valid_in.eq(integration_2.valid_out),
			vbits_to_cbits.busy_in.eq(self.busy_in),
		]

		# vbits_to_cbits and this
		m.d.comb += [
			self.data_out.eq(vbits_to_cbits.data_out),
			self.valid_out.eq(vbits_to_cbits.valid_out),
			self.end_out.eq(vbits_to_cbits.end_out),
		]

		# self.busy
		m.d.comb += [
			self.nready.eq(integration_2.nready),
		]

		return m


if __name__ == "__main__":
	config = {
		"bit_depth" : 12,
		"pixels_per_cycle": 4,
		"LJ92_fifo_depth": 128,
		"out_bits": 32,
		"converter" : 48,
		"converter_fifo_depth": 256,
		"vbits_to_cbits_buffer_size": 144,
		"predictor_function": 1,
		"num_of_components": 4,
		"axi_lite_debug": False,
		"support_axi_lite": False,
	}
	cons = constraints.Constraints()
	d = Integration3(config, cons)
	main(d, ports=d.ios)