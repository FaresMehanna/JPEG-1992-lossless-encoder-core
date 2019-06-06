from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *
import integration_3

class Integration3AxiStream(Elaboratable):

	def __init__(self):

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

		self.top = integration_3.Integration3()

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
			top.pixel_in1.eq(self.s_tdata[0:12]),
			top.pixel_in2.eq(self.s_tdata[12:24]),
			top.pixel_in3.eq(self.s_tdata[24:36]),
			top.pixel_in4.eq(self.s_tdata[36:48]),
			self.s_tready.eq(top.nready==0),
			s_end.eq(self.s_tlast),
			top.valid_in.eq(self.s_tvalid),
		]

		return m

if __name__ == "__main__":
	d = Integration3AxiStream()
	main(d, ports=d.ios)