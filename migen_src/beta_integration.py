from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import integration_3
import constraints
import fix_0xff, fix_0xff2

class BetaIntegration(Elaboratable):

	def __init__(self):

		self.config = config = {
			"bit_depth" : 12,
			"pixels_per_cycle": 2,
			"LJ92_fifo_depth": 512, #512 x 72 = RAM36
			"out_bits": 16,
			"converter" : 30,
			"converter_fifo_depth": 512, #512 x 36 = RAM18
			"vbits_to_cbits_buffer_size": 77,
			"support_axi_lite": True,
			"axi_lite_debug": True,
			"predictor_function": 1,
			"num_of_components": 4,
		}
		cons = constraints.Constraints()

		#pixels in
		self.pixel_in1 = Signal(12)
		self.pixel_in2 = Signal(12)

		#data out
		self.data_out = Signal(16)

		#signals
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)
		self.end_out = Signal(1)
		self.nready = Signal(1)
		self.busy_in = Signal(1)

		self.integration_3 = integration_3.Integration3(config, cons)
		self.fix_0xff = fix_0xff.Fix0xFF()
		self.fix_0xff2 = fix_0xff2.Fix0xFF2()

		self.ios = \
			[self.valid_in, self.valid_out, self.end_out] + \
			[self.pixel_in1, self.pixel_in2, self.nready] + \
			[self.data_out, self.busy_in]
			
	def elaborate(self, platform):

		m = Module()
		
		m.submodules.integration_3 = integration_3 = self.integration_3
		m.submodules.fix_0xff = fix_0xff = self.fix_0xff
		m.submodules.fix_0xff2 = fix_0xff2 = self.fix_0xff2

		if self.config['axi_lite_debug'] and self.config['support_axi_lite']:
			# set debugging counters
			trans_started = Signal(1)
			m.d.sync += trans_started.eq(trans_started | self.valid_in)
			debug_en = Signal(8)
			m.d.sync += self.integration_3.integration_2.integration_1.core_axi_lite.debug_en.eq(debug_en)
			m.d.sync += debug_en[0].eq((trans_started==1) & (self.end_out==0) & (self.valid_in==0))
			m.d.sync += debug_en[1].eq((trans_started==1) & (self.end_out==0) & (self.valid_in==1))
			m.d.sync += debug_en[2].eq((trans_started==1) & (self.end_out==0) & (self.valid_out==0))
			m.d.sync += debug_en[3].eq((trans_started==1) & (self.end_out==0) & (self.valid_out==1))
			m.d.sync += debug_en[4].eq((trans_started==1) & (self.end_out==0) & (self.nready==1))
			m.d.sync += debug_en[5].eq((trans_started==1) & (self.end_out==0) & (self.nready==0))
			m.d.sync += debug_en[6].eq((trans_started==1) & (self.end_out==0) & (self.busy_in==1))
			m.d.sync += debug_en[7].eq((trans_started==1) & (self.end_out==0) & (self.busy_in==0))

		#in
		m.d.comb += [
			integration_3.pixels_in[0].eq(self.pixel_in1),
			integration_3.pixels_in[1].eq(self.pixel_in2),
			integration_3.valid_in.eq(self.valid_in),
			integration_3.busy_in.eq(fix_0xff.o_busy),
		]
		#out
		#int3 and fixer
		m.d.comb += [
			fix_0xff.data_in.eq(integration_3.data_out),
			fix_0xff.valid_in.eq(integration_3.valid_out),
			fix_0xff.end_in.eq(integration_3.end_out),
			fix_0xff.i_busy.eq(fix_0xff2.o_busy),
		]
		#fixer1 and fixer2
		m.d.comb += [
			fix_0xff2.data_in.eq(fix_0xff.data_out),
			fix_0xff2.valid_in.eq(fix_0xff.valid_out),
			fix_0xff2.end_in.eq(fix_0xff.end_out),
			fix_0xff2.i_busy.eq(self.busy_in),
			fix_0xff2.data_in_ctr.eq(fix_0xff.data_out_ctr),
		]
		#out
		m.d.comb += [
			self.data_out.eq(fix_0xff2.data_out),
			self.valid_out.eq(fix_0xff2.valid_out),
			self.end_out.eq(fix_0xff2.end_out),
			self.nready.eq(integration_3.nready),
		]
		return m


if __name__ == "__main__":
	d = BetaIntegration()
	main(d, ports=d.ios)