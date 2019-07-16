'''
--------------------
Module: dma_axi_lite
--------------------
Description: 
    - dma_axi_lite is a module implements AXI lite interface to allow
    the PS to read/write certain registers for DMA operation.
    - it can be used to read/write the starting address of reading and
    writing.
    - it can be used to start the DMA as well.
--------------------
Input: 
    - AXI lite interface inputs.
--------------------
Output:
    - AXI lite interface outputs.
    - read and write starting addresses.
	- signal starting the operation.
--------------------
timing:
    - timing as normal AXI lite interface.
--------------------
Notes :
    - this module is only used when axi_hp[reader/writer] are used,
	and it is not part of the LJ92 encoder.
    - to read and write the registers, the address will be as
    following (uint32_t)((AXI_LITE_ADDRESS | 0x400) + reg_index),
    reg_index is between 0 and 3.
    0 represents starting read_address
    1 represents starting write_address
    2 represents starting the operation
    3 is reserved for future use.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from axi3_pkg import *
from axi3_lite_pkg import *

#reference: https://github.com/apertus-open-source-cinema/axiom-beta-firmware/blob/master/peripherals/soc_main/reg_file.vhd

class DMAAxiLite(Elaboratable):

	def __init__(self):

		# clk and resets
		self.s_axi_aclk_ = Signal(1)
		self.s_axi_areset_n_ = Signal(1)

		# axi lite buses
		self.s_axi_ro_ = Record(axi3ml_read_in_r)	#out
		self.s_axi_ri_ = Record(axi3ml_read_out_r)	#in
		self.s_axi_wo_ = Record(axi3ml_write_in_r)	#out
		self.s_axi_wi_ = Record(axi3ml_write_out_r)	#in

		# addresses to start read and write
		self.read_addr = Signal(32)
		self.write_addr = Signal(32)

		# start the operation
		self.start = Signal(32)

		# debug data
		self.in1 = Signal(32)
		self.in2 = Signal(32)
		self.in3 = Signal(32)
		self.in4 = Signal(32)
		self.in5 = Signal(32)
		self.in6 = Signal(32)
		self.in7 = Signal(32)
		self.in8 = Signal(32)
		self.in9 = Signal(32)

		self.ios = \
			[self.s_axi_aclk_, self.s_axi_areset_n_] + \
			[self.read_addr, self.write_addr] + \
			[self.start, self.in1, self.in2, self.in3, self.in4] + \
			[self.in5, self.in6, self.in7, self.in8, self.in9] + \
			[self.s_axi_ro_.arready, self.s_axi_ro_.rdata] + \
			[self.s_axi_ro_.rresp, self.s_axi_ro_.rvalid] + \
			[self.s_axi_ri_.araddr, self.s_axi_ri_.arprot] + \
			[self.s_axi_ri_.arvalid, self.s_axi_ri_.rready] + \
			[self.s_axi_wo_.awready, self.s_axi_wo_.wready] + \
			[self.s_axi_wo_.bresp, self.s_axi_wo_.bvalid] + \
			[self.s_axi_wi_.awaddr, self.s_axi_wi_.awprot] + \
			[self.s_axi_wi_.awvalid, self.s_axi_wi_.wdata] + \
			[self.s_axi_wi_.wstrb, self.s_axi_wi_.wvalid] + \
			[self.s_axi_wi_.bready]

		self.axi_ios = \
			[self.s_axi_aclk_, self.s_axi_areset_n_] + \
			[self.s_axi_ro_.arready, self.s_axi_ro_.rdata] + \
			[self.s_axi_ro_.rresp, self.s_axi_ro_.rvalid] + \
			[self.s_axi_ri_.araddr, self.s_axi_ri_.arprot] + \
			[self.s_axi_ri_.arvalid, self.s_axi_ri_.rready] + \
			[self.s_axi_wo_.awready, self.s_axi_wo_.wready] + \
			[self.s_axi_wo_.bresp, self.s_axi_wo_.bvalid] + \
			[self.s_axi_wi_.awaddr, self.s_axi_wi_.awprot] + \
			[self.s_axi_wi_.awvalid, self.s_axi_wi_.wdata] + \
			[self.s_axi_wi_.wstrb, self.s_axi_wi_.wvalid] + \
			[self.s_axi_wi_.bready]

	def elaborate(self, platform):

		m = Module()

		# registers to hold data
		addr_v = Signal(32)

		arready_v = Signal(1)
		rvalid_v = Signal(1)

		awready_v = Signal(1)
		wready_v = Signal(1)
		bvalid_v = Signal(1)

		rdata_v = Signal(32)
		rresp_v = Signal(2)

		bresp_v = Signal(2)

		# wires for writing operations
		wdata_v = Signal(32)
		wstrb_v = Signal(4)

		m.d.comb += [
			wdata_v.eq(0),
			wstrb_v.eq(0),
		]

		# enable and index
		basic_enable = Signal(1)
		basic_index = Signal(4)

		m.d.comb += [
			basic_enable.eq(addr_v[10]),
			basic_index.eq(addr_v),
		]

		def read_basic():
			with m.Switch(basic_index):
				with m.Case(0):
					m.d.sync += rdata_v.eq(self.read_addr)
				with m.Case(1):
					m.d.sync += rdata_v.eq(self.write_addr)
				with m.Case(2):
					m.d.sync += rdata_v.eq(self.start)
				with m.Case(3):
					m.d.sync += rdata_v.eq(self.in1)
				with m.Case(4):
					m.d.sync += rdata_v.eq(self.in2)
				with m.Case(5):
					m.d.sync += rdata_v.eq(self.in3)
				with m.Case(6):
					m.d.sync += rdata_v.eq(self.in4)
				with m.Case(7):
					m.d.sync += rdata_v.eq(self.in5)
				with m.Case(8):
					m.d.sync += rdata_v.eq(self.in6)
				with m.Case(9):
					m.d.sync += rdata_v.eq(self.in7)
				with m.Case(10):
					m.d.sync += rdata_v.eq(self.in8)
				with m.Case(11):
					m.d.sync += rdata_v.eq(self.in9)

			m.d.sync += rresp_v.eq(0)

		def write_to_basic():
			m.d.sync += bresp_v.eq(0)
			for i in range(4):
				start = i*8
				end = start+8
				with m.If(wstrb_v[i]):
					with m.Switch(basic_index):
						with m.Case(0):
							m.d.sync += self.read_addr[start:end].eq(wdata_v[start:end])
						with m.Case(1):
							m.d.sync += self.write_addr[start:end].eq(wdata_v[start:end])
						with m.Case(2):
							m.d.sync += self.start[start:end].eq(wdata_v[start:end])
						with m.Case(3):
							m.d.sync += bresp_v.eq(2)
						with m.Case(4):
							m.d.sync += bresp_v.eq(2)
						with m.Case(5):
							m.d.sync += bresp_v.eq(2)
						with m.Case(6):
							m.d.sync += bresp_v.eq(2)
						with m.Case(7):
							m.d.sync += bresp_v.eq(2)
						with m.Case(8):
							m.d.sync += bresp_v.eq(2)
						with m.Case(9):
							m.d.sync += bresp_v.eq(2)
						with m.Case(10):
							m.d.sync += bresp_v.eq(2)
						with m.Case(11):
							m.d.sync += bresp_v.eq(2)
							
		def clean_write_basic():
			pass


		with m.FSM() as main:

			with m.State("IDLE"):
				#needed from other states
				m.d.sync += [
					rvalid_v.eq(0),
					bvalid_v.eq(0),
				]
				#read operation
				with m.If(self.s_axi_ri_.arvalid):
					m.next = "READ_ADDRESS"
				with m.Elif(self.s_axi_wi_.awvalid):
					m.next = "WRITE_ADDRESS"


			with m.State("READ_ADDRESS"):
				# ack address, ready for transfer
				m.d.sync += [
					addr_v.eq(self.s_axi_ri_.araddr >> 2),
					arready_v.eq(1),
				]
				m.next = "READ_DATA"


			with m.State("READ_DATA"):
				m.d.sync += arready_v.eq(0)	# done
				# ssss bram
				with m.If(basic_enable):
					read_basic()
				# decode error
				with m.Else():
					m.d.sync += rresp_v.eq(3)
				# to finish
				with m.If(self.s_axi_ri_.rready):
					m.d.sync += rvalid_v.eq(1)
					m.next = "IDLE"


			with m.State("WRITE_ADDRESS"):
				# ack address, ready for transfer
				m.d.sync += [
					addr_v.eq(self.s_axi_wi_.awaddr >> 2),
					awready_v.eq(1),
				]
				m.next = "WRITE_DATA"


			with m.State("WRITE_DATA"):
				m.d.sync += awready_v.eq(0)	# done
				m.d.sync += wready_v.eq(1)	# ready for data
				with m.If(self.s_axi_wi_.wvalid):
					m.d.comb += [
						wdata_v.eq(self.s_axi_wi_.wdata),
						wstrb_v.eq(self.s_axi_wi_.wstrb),
					]
					# ssss bram
					with m.If(basic_enable):
						write_to_basic()
					# decode error
					with m.Else():
						m.d.sync += bresp_v.eq(3)
					m.next = "WRITE_RESPONSE"


			with m.State("WRITE_RESPONSE"):
				clean_write_basic()
				m.d.sync += wready_v.eq(0)
				with m.If(self.s_axi_wi_.bready):
					m.d.sync += bvalid_v.eq(1)
					m.next = "IDLE"

		m.d.comb += [
			self.s_axi_ro_.arready.eq(arready_v),
			self.s_axi_ro_.rvalid.eq(rvalid_v),
		]

		m.d.comb += [
			self.s_axi_wo_.awready.eq(awready_v),
			self.s_axi_wo_.wready.eq(wready_v),
			self.s_axi_wo_.bvalid.eq(bvalid_v),
		]

		m.d.comb += [
			self.s_axi_ro_.rdata.eq(rdata_v),
			self.s_axi_ro_.rresp.eq(rresp_v),
		]

		m.d.comb += [
			self.s_axi_wo_.bresp.eq(bresp_v),
		]

		return m


if __name__ == "__main__":
	d = DMAAxiLite()
	main(d, ports=d.ios)