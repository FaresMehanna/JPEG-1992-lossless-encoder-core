from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from axi3_pkg import *

#reference: https://github.com/apertus-open-source-cinema/axiom-beta-firmware/blob/master/peripherals/soc_main/axihp_writer.vhd

class AxiHPWriter(Elaboratable):

	def __init__(self, data_w=64, data_c=16):

		self.m_axi_aclk = Signal(1)		# in
		self.m_axi_areset_n = Signal(1)	# in
		self.enable = Signal(1)			# in
		self.inactive = Signal(1)		# out

		self.m_axi_wo = Record(axi3s_write_in_r)	#out
		self.m_axi_wi = Record(axi3s_write_out_r)	#in

		self.addr_clk = Signal(1)		# out
		self.addr_enable = Signal(1)	# out
		self.addr_in = Signal(32)		# in
		self.addr_empty = Signal(1)		# in

		self.data_clk = Signal(1)		# out
		self.data_enable = Signal(1)	# out
		self.data_in = Signal(data_w)	# in
		self.data_empty = Signal(1)		# in

		self.write_strobe = Signal(8)	# in

		self.writer_error = Signal(1)	# out
		self.writer_active = Signal(4)	# out
		self.writer_unconf = Signal(4)	# out

		self.data_w = data_w
		self.data_c = data_c

		self.ios = \
			[self.m_axi_aclk, self.m_axi_areset_n, self.enable, self.inactive] + \
			[self.data_clk, self.data_enable, self.data_in, self.data_empty] + \
			[self.addr_clk, self.addr_enable, self.addr_in, self.addr_empty] + \
			[self.write_strobe] + \
			[self.writer_error, self.writer_active, self.writer_unconf] + \
			[self.m_axi_wo.awid, self.m_axi_wo.awaddr] + \
			[self.m_axi_wo.awburst, self.m_axi_wo.awlen] + \
			[self.m_axi_wo.awsize, self.m_axi_wo.awprot] + \
			[self.m_axi_wo.awvalid, self.m_axi_wo.wid] + \
			[self.m_axi_wo.wdata, self.m_axi_wo.wstrb] + \
			[self.m_axi_wo.wlast, self.m_axi_wo.wvalid] + \
			[self.m_axi_wo.bready] + \
			[self.m_axi_wi.awready, self.m_axi_wi.wacount] + \
			[self.m_axi_wi.wready, self.m_axi_wi.wcount] + \
			[self.m_axi_wi.bid, self.m_axi_wi.bresp] + \
			[self.m_axi_wi.bvalid]

	def elaborate(self, platform):

		m = Module()

		# needed signals
		awlen_c = Signal(4)
		m.d.comb += awlen_c.eq(self.data_c)

		active = Signal(4)
		unconf = Signal(4)

		awvalid = Signal(1)
		wvalid = Signal(1)
		wlast = Signal(1)	# need counter instead of SRL16E to work!
		bready = Signal(1)

		data_en = Signal(1)
		addr_en = Signal(1)
		resp_en = Signal(1)


		'''---------------------
		|   Address Pipeline   |
		---------------------'''

		m.d.sync += addr_en.eq((awvalid==1) & (self.m_axi_wi.awready==1))

		# idle phase
		with m.If(awvalid==0):
			# writer enabled & address available & below max
			with m.If((self.enable==1) & (self.addr_empty==0) & (active[3]==0)):
				m.d.sync += awvalid.eq(1)

		# active phase
		with m.If(awvalid):
			with m.If(self.m_axi_wi.awready):
				m.d.sync += awvalid.eq(0)

		m.d.sync += [
			self.m_axi_wo.awaddr.eq(self.addr_in),
			self.m_axi_wo.awvalid.eq(awvalid),
			self.addr_enable.eq(addr_en),
		]


		'''---------------------
		|     Data Pipeline    |
		---------------------'''

		# wlast circuit
		counter = Signal(4)
		with m.If(data_en):
			with m.If(counter==(self.data_c-1)):
				m.d.sync += [
					counter.eq(0),
					wlast.eq(1),
				]
			with m.Else():
				m.d.sync += [
					counter.eq(counter + 1),
					wlast.eq(0),
				]

		m.d.sync += data_en.eq((wvalid==1) & (self.m_axi_wi.wready==1))

		# idle phase
		with m.If(wvalid==0):
			# fifo not empty & inactive
			with m.If((self.data_empty==0) & (active!=0)):
				m.d.sync += wvalid.eq(1)

		# active phase
		with m.Else():
			with m.If(wlast):
				m.d.sync += wvalid.eq(0)

		m.d.sync += [
			self.m_axi_wo.wdata.eq(self.data_in),
			self.m_axi_wo.wvalid.eq(wvalid),
			self.m_axi_wo.wlast.eq(wlast),
			self.data_enable.eq(data_en),
		]


		'''---------------------
		|   Response Pipeline  |
		---------------------'''

		m.d.sync += resp_en.eq((bready==1) & (self.m_axi_wi.bvalid==1))

		# idle phase
		with m.If(bready==0):
			# writer enabled
			with m.If(self.enable):
				m.d.sync += bready.eq(1)

		# active phase
		with m.Else():
			with m.If(unconf==0):
				m.d.sync += bready.eq(0)

		m.d.sync += [
			self.m_axi_wo.bready.eq(bready),
			self.writer_error.eq((resp_en==1) & (self.m_axi_wi.bresp!=0)),
		]


		'''---------------------
		| In Flight Accounting |
		---------------------'''

		# active_proc
		with m.If((addr_en==1) & (wlast==0)):
			# one more
			m.d.sync += active.eq(active + 1)

		with m.Elif((addr_en==0) & (wlast==1)):
			# one less
			m.d.sync += active.eq(active - 1)

		# unconf_proc
		with m.If((addr_en==1) & (resp_en==0)):
			# one more
			m.d.sync += unconf.eq(unconf + 1)
			
		with m.Elif((addr_en==0) & (resp_en==1)):
			# one less
			m.d.sync += unconf.eq(unconf - 1)

		m.d.sync += self.inactive.eq((active==0) & (unconf==0))


		'''---------------------
		| Constant Values, clk |
		---------------------'''

		m.d.sync += [
			self.m_axi_wo.awid.eq(0),
			self.m_axi_wo.wid.eq(0),
		]

		m.d.sync += [
			self.m_axi_wo.awlen.eq(awlen_c),
		]

		m.d.sync += [
			self.m_axi_wo.awburst.eq(0b01),
			self.m_axi_wo.awsize.eq(0b11),
			self.m_axi_wo.wstrb.eq(self.write_strobe),
		]

		m.d.sync += [
			self.m_axi_wo.awprot.eq(0),
		]

		m.d.sync += [
			self.data_clk.eq(self.m_axi_aclk),
			self.addr_clk.eq(self.m_axi_aclk),
		]

		return m


if __name__ == "__main__":
	d = AxiHPWriter()
	main(d, ports=d.ios)