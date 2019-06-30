from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import integration_3, constraints

class Integration3AxiStream(Elaboratable):

	def __init__(self):

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

		# axi stream master
		self.m_tvalid = Signal(1)
		self.m_tlast = Signal(1)
		self.m_tready = Signal(1)
		self.m_tdata = Signal(32)

		# axi steam slave
		self.s_tvalid = Signal(1)
		self.s_tlast = Signal(1)
		self.s_tready = Signal(1)
		self.s_tdata = Signal(64)

		self.top = integration_3.Integration3(config, cons)

		self.ios = \
			[self.m_tvalid, self.m_tlast, self.m_tready, self.m_tdata] + \
			[self.s_tvalid, self.s_tlast, self.s_tready, self.s_tdata]

	def elaborate(self, platform):

		m = Module()

		m.submodules.top_module = top = self.top

		s_end = Signal(1)

		# master interface
		m.d.comb += [
			self.m_tdata.eq(top.data_out),
			self.m_tlast.eq(top.end_out),
			top.busy_in.eq(self.m_tready==0),
			self.m_tvalid.eq(top.valid_out),
		]

		# slave interface
		m.d.comb += [
			top.pixels_in[0].eq(self.s_tdata[0:12]),
			top.pixels_in[1].eq(self.s_tdata[12:24]),
			top.pixels_in[2].eq(self.s_tdata[24:36]),
			top.pixels_in[3].eq(self.s_tdata[36:48]),
			self.s_tready.eq(top.nready==0),
			s_end.eq(self.s_tlast),
			top.valid_in.eq(self.s_tvalid),
		]

		return m

if __name__ == "__main__":
	d = Integration3AxiStream()
	main(d, ports=d.ios)