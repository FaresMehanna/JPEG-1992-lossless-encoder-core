from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from axi3_pkg import *
from axi3_lite_pkg import *

class AxiLite(Elaboratable):

	def __init__(self):

		# clk and reset input
		self.s_axi_aclk = Signal(1)		#in
		self.s_axi_areset_n = Signal(1)	#in

		# slave buses
		self.s_axi_ro = Record(axi3m_read_in_r)		#out
		self.s_axi_ri = Record(axi3m_read_out_r)	#in
		self.s_axi_wo = Record(axi3m_write_in_r)	#out
		self.s_axi_wi = Record(axi3m_write_out_r)	#in

		# clk and reset output
		self.m_axi_aclk = Signal(1)		#out
		self.m_axi_areset_n = Signal(1)	#out

		# master buses
		self.m_axi_ri = Record(axi3ml_read_in_r)	#in
		self.m_axi_ro = Record(axi3ml_read_out_r)	#out
		self.m_axi_wi = Record(axi3ml_write_in_r)	#in
		self.m_axi_wo = Record(axi3ml_write_out_r)	#out

		self.ios = \
			[self.s_axi_aclk, self.s_axi_areset_n] + \
			[self.s_axi_ro.arready, self.s_axi_ro.rid] + \
			[self.s_axi_ro.rdata, self.s_axi_ro.rlast] + \
			[self.s_axi_ro.rresp, self.s_axi_ro.rvalid] + \
			[self.s_axi_ri.arid, self.s_axi_ri.araddr] + \
			[self.s_axi_ri.arburst, self.s_axi_ri.arlen] + \
			[self.s_axi_ri.arsize, self.s_axi_ri.arprot] + \
			[self.s_axi_ri.arvalid, self.s_axi_ri.rready] + \
			[self.s_axi_wo.awready, self.s_axi_wo.wready] + \
			[self.s_axi_wo.bid, self.s_axi_wo.bresp] + \
			[self.s_axi_wo.bvalid] + \
			[self.s_axi_wi.awid, self.s_axi_wi.awaddr] + \
			[self.s_axi_wi.awburst, self.s_axi_wi.awlen] + \
			[self.s_axi_wi.awsize, self.s_axi_wi.awprot] + \
			[self.s_axi_wi.awvalid, self.s_axi_wi.wid] + \
			[self.s_axi_wi.wdata, self.s_axi_wi.wstrb] + \
			[self.s_axi_wi.wlast, self.s_axi_wi.wvalid] + \
			[self.s_axi_wi.bready] + \
			[self.m_axi_ri.arready, self.m_axi_ri.rdata] + \
			[self.m_axi_ri.rresp, self.m_axi_ri.rvalid] + \
			[self.m_axi_ro.araddr, self.m_axi_ro.arprot] + \
			[self.m_axi_ro.arvalid, self.m_axi_ro.rready] + \
			[self.m_axi_wi.awready, self.m_axi_wi.wready] + \
			[self.m_axi_wi.bresp, self.m_axi_wi.bvalid] + \
			[self.m_axi_wo.awaddr, self.m_axi_wo.awprot] + \
			[self.m_axi_wo.awvalid, self.m_axi_wo.wdata] + \
			[self.m_axi_wo.wstrb, self.m_axi_wo.wvalid] + \
			[self.m_axi_wo.bready] + \
			[self.m_axi_aclk, self.m_axi_areset_n]

	def elaborate(self, platform):

		m = Module()

		rwid = Signal(12)

		#main process
		with m.If(self.s_axi_areset_n == 0):
			m.d.sync += rwid.eq(0)
		with m.Else():
			with m.If(self.s_axi_ri.arvalid):
				m.d.sync += rwid.eq(self.s_axi_ri.arid)
			with m.If(self.s_axi_wi.awvalid):
				m.d.sync += rwid.eq(self.s_axi_wi.awid)
		m.d.sync += [
			self.s_axi_ro.rid.eq(rwid),
			self.s_axi_wo.bid.eq(rwid),
		]

		# clk and reset
		m.d.comb += [
			self.m_axi_aclk.eq(self.s_axi_aclk),
			self.m_axi_areset_n.eq(self.s_axi_areset_n),
		]

		# read address
		m.d.comb += [
			self.s_axi_ro.arready.eq(self.m_axi_ri.arready),
		]

		# read data
		m.d.comb += [
			self.s_axi_ro.rdata.eq(self.m_axi_ri.rdata),
			self.s_axi_ro.rlast.eq(1),
			self.s_axi_ro.rresp.eq(self.m_axi_ri.rresp),
			self.s_axi_ro.rvalid.eq(self.m_axi_ri.rvalid),
		]

		# read address
		m.d.comb += [
			self.m_axi_ro.araddr.eq(self.s_axi_ri.araddr),
			self.m_axi_ro.arprot.eq(self.s_axi_ri.arprot),
			self.m_axi_ro.arvalid.eq(self.s_axi_ri.arvalid),
		]

		# read data
		m.d.comb += [
			self.m_axi_ro.rready.eq(self.s_axi_ri.rready),
		]

		# write address
		m.d.comb += [
			self.s_axi_wo.awready.eq(self.m_axi_wi.awready),
		]

		# write data
		m.d.comb += [
			self.s_axi_wo.wready.eq(self.m_axi_wi.wready),
		]

		# write response
		m.d.comb += [
			self.s_axi_wo.bresp.eq(self.m_axi_wi.bresp),
			self.s_axi_wo.bvalid.eq(self.m_axi_wi.bvalid),
		]

		# write address
		m.d.comb += [
			self.m_axi_wo.awaddr.eq(self.s_axi_wi.awaddr),
			self.m_axi_wo.awprot.eq(self.s_axi_wi.awprot),
			self.m_axi_wo.awvalid.eq(self.s_axi_wi.awvalid),
		]

		# write data
		m.d.comb += [
			self.m_axi_wo.wdata.eq(self.s_axi_wi.wdata),
			self.m_axi_wo.wstrb.eq(self.s_axi_wi.wstrb),
			self.m_axi_wo.wvalid.eq(self.s_axi_wi.wvalid),
		]

		# write response
		m.d.comb += [
			self.m_axi_wo.bready.eq(self.s_axi_wi.bready),
		]

		return m

if __name__ == "__main__":
	d = AxiLite()
	main(d, ports=d.ios)