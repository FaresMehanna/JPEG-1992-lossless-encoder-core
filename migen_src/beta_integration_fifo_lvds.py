from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import beta_integration
import b64_b32_2
import b16_b40

class BetaIntegrationFIFOLVDS(Elaboratable):

	def __init__(self):

		# axi stream master
		self.m_tvalid = Signal(1)
		self.m_tready = Signal(1)
		self.m_tdata = Signal(40)

		# axi steam slave - MUST BE FIFO
		self.s_tvalid = Signal(1)
		self.s_tready = Signal(1)
		self.s_tdata = Signal(64)

		self.top = beta_integration.BetaIntegration()
		self.b64_b32 = b64_b32_2.B64B32_2()
		self.b16_b40 = b16_b40.B16B40()

		self.ios = \
			[self.m_tvalid, self.m_tready, self.m_tdata] + \
			[self.s_tvalid, self.s_tready, self.s_tdata]

		if self.top.config['support_axi_lite']:
			self.ios += self.top.integration_3.integration_2.integration_1.core_axi_lite.axi_ios

	def elaborate(self, platform):

		m = Module()

		m.submodules.top_module = top = self.top
		m.submodules.b64_b32 = b64_b32 = self.b64_b32
		m.submodules.b16_b40 = b16_b40 = self.b16_b40

		# master interface and b16_b40
		m.d.comb += [
			self.m_tdata.eq(b16_b40.data_out),
			b16_b40.i_busy.eq(self.m_tready==0),
			self.m_tvalid.eq(b16_b40.valid_out),
		]

		# b16_b40 and top
		m.d.comb += [
			b16_b40.data_in.eq(top.data_out),
			top.busy_in.eq(b16_b40.o_busy),
			b16_b40.valid_in.eq(top.valid_out),
		]

		# slave interface and b64_b32
		m.d.comb += [
			b64_b32.data_in.eq(self.s_tdata),
			self.s_tready.eq(b64_b32.o_busy==0),
			b64_b32.valid_in.eq(self.s_tvalid),
		]

		# b64_b32 and top
		m.d.comb += [
			top.pixel_in1.eq(b64_b32.data_out[12:24]),
			top.pixel_in2.eq(b64_b32.data_out[0:12]),
			b64_b32.i_busy.eq(top.nready),
			top.valid_in.eq(b64_b32.valid_out),
		]

		return m

if __name__ == "__main__":
	d = BetaIntegrationFIFOLVDS()
	main(d, ports=d.ios)