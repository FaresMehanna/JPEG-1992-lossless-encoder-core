from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from axi3_pkg import *

#reference: https://github.com/apertus-open-source-cinema/axiom-beta-firmware/blob/master/peripherals/soc_main/axihp_reader.vhd

class AxiHPReader(Elaboratable):

	def __init__(self, data_w=64, data_c=16):

		self.m_axi_aclk_ = Signal(1)		# in
		self.m_axi_areset_n_ = Signal(1)	# in
		self.enable = Signal(1)			# in
		self.inactive = Signal(1)		# out

		self.m_axi_ro = Record(axi3s_read_in_r)		#out
		self.m_axi_ri = Record(axi3s_read_out_r)	#in

		self.data_clk = Signal(1)		# out
		self.data_enable = Signal(1)	# out
		self.data_out = Signal(data_w)	# out
		self.data_full = Signal(1)		# in

		self.addr_clk = Signal(1)		# out
		self.addr_enable = Signal(1)	# out
		self.addr_in = Signal(32)		# in
		self.addr_empty = Signal(1)		# in

		self.reader_error = Signal(1)	# out
		self.reader_active = Signal(4)	# out

		self.data_w = data_w
		self.data_c = data_c

		self.ios = \
			[self.m_axi_aclk_, self.m_axi_areset_n_, self.enable, self.inactive] + \
			[self.data_clk, self.data_enable, self.data_out, self.data_full] + \
			[self.addr_clk, self.addr_enable, self.addr_in, self.addr_empty] + \
			[self.reader_error, self.reader_active] + \
			[self.m_axi_ro.arid, self.m_axi_ro.araddr] + \
			[self.m_axi_ro.arburst, self.m_axi_ro.arlen] + \
			[self.m_axi_ro.arsize, self.m_axi_ro.arprot] + \
			[self.m_axi_ro.arvalid, self.m_axi_ro.rready] + \
			[self.m_axi_ri.arready, self.m_axi_ri.racount] + \
			[self.m_axi_ri.rid, self.m_axi_ri.rdata] + \
			[self.m_axi_ri.rlast, self.m_axi_ri.rresp] + \
			[self.m_axi_ri.rvalid, self.m_axi_ri.rcount]

		self.axi_ios = \
			[self.m_axi_aclk_, self.m_axi_areset_n_] + \
			[self.m_axi_ro.arid, self.m_axi_ro.araddr] + \
			[self.m_axi_ro.arburst, self.m_axi_ro.arlen] + \
			[self.m_axi_ro.arsize, self.m_axi_ro.arprot] + \
			[self.m_axi_ro.arvalid, self.m_axi_ro.rready] + \
			[self.m_axi_ri.arready, self.m_axi_ri.racount] + \
			[self.m_axi_ri.rid, self.m_axi_ri.rdata] + \
			[self.m_axi_ri.rlast, self.m_axi_ri.rresp] + \
			[self.m_axi_ri.rvalid, self.m_axi_ri.rcount]

	def elaborate(self, platform):

		m = Module()

		# needed signals
		arlen_c = Signal(4)
		m.d.comb += arlen_c.eq(self.data_c - 1)

		active = Signal(4)
		arvalid = Signal(1)
		rlast = Signal(1)
		rready = Signal(1)

		data_en = Signal(1)
		addr_en = Signal(1)
		resp_en = Signal(1)


		'''---------------------
		|   Address Pipeline   |
		---------------------'''

		m.d.comb += addr_en.eq((arvalid==1) & (self.m_axi_ri.arready==1))

		# idle phase
		with m.If(arvalid==0):
			# writer enabled & fifo not empty & below max
			with m.If((self.enable==1) & (self.addr_empty==0) & (active[3]==0)):
				m.d.sync += arvalid.eq(1)

		# active phase
		with m.If(arvalid):
			with m.If(self.m_axi_ri.arready):
				m.d.sync += arvalid.eq(0)

		m.d.comb += [
			self.m_axi_ro.araddr.eq(self.addr_in),
			self.m_axi_ro.arvalid.eq(arvalid),
			self.addr_enable.eq(addr_en),
		]


		'''---------------------
		|     Data Pipeline    |
		---------------------'''

		m.d.comb += data_en.eq((rready==1) & (self.m_axi_ri.rvalid==1))

		# idle phase
		with m.If(rready==0):
			# fifo not full & inactive
			with m.If((self.data_full==0) & (active!=0)):
				m.d.sync += rready.eq(1)

		# active phase
		with m.Else():
			with m.If(self.m_axi_ri.rlast):
				m.d.sync += rready.eq(0)

		m.d.comb += [
			self.reader_error.eq(((data_en==1) & (self.m_axi_ri.rresp!=0))),
			self.data_out.eq(self.m_axi_ri.rdata),
			self.m_axi_ro.rready.eq(rready),
			self.data_enable.eq(data_en),
		]


		'''---------------------
		| In Flight Accounting |
		---------------------'''

		# one more
		with m.If((addr_en==1) & (self.m_axi_ri.rlast==0)):
			m.d.sync += active.eq(active + 1)

		# one less
		with m.Elif((addr_en==0) & (self.m_axi_ri.rlast==1)):
			m.d.sync += active.eq(active - 1)

		m.d.comb += self.inactive.eq(active==0)


		'''---------------------
		| Constant Values, clk |
		---------------------'''

		m.d.comb += [
			self.m_axi_ro.arid.eq(0),
		]

		m.d.comb += [
			self.m_axi_ro.arlen.eq(arlen_c),
		]

		m.d.comb += [
			self.m_axi_ro.arburst.eq(0b01),
			self.m_axi_ro.arsize.eq(0b11),
		]

		m.d.comb += [
			self.m_axi_ro.arprot.eq(0),
		]

		m.d.comb += [
			self.data_clk.eq(self.m_axi_aclk_),
			self.addr_clk.eq(self.m_axi_aclk_),
		]

		m.d.comb += [
			self.reader_active.eq(active),
		]

		return m


if __name__ == "__main__":
	d = AxiHPReader()
	main(d, ports=d.ios)