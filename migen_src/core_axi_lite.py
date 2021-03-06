'''
--------------------
Module: core_axi_lite
--------------------
Description: 
    - core_axi_lite is a module implements AXI lite interface to allow
    the PS to read/write certain registers or BRAM.
    - it can be used to read/write the height and width of the frame.
    - it can be used to read/write Huffman table values.
    - it can be used to read debugging registers - if enabled.
--------------------
Input: 
    - AXI lite interface inputs.
    - Huffman table BRAM port read/write port.
--------------------
Output:
    - AXI lite interface outputs.
    - Huffman table BRAM port read/write port.
	- height and width register.
--------------------
timing:
    - timing as normal AXI lite interface, but it take more cycles
    per transaction since BRAM is registered, so expect lower
    throughput.
--------------------
Notes :
    - this module is optional and is not important to be used
    if the height & width of frames is constant in the camera,
    and no experiments with Huffman values is needed.
    - to read and write in Huffman table, the address will be as
    following (uint32_t)((AXI_LITE_ADDRESS | 0x400) + ssss_index),
    ssss_index is between 0 and 2*bit_depth.
    It take up to 2*bit_depth since every ssss will be accessed 
    as 2 x uint32_t registers, the size exactly is defined in
    encoding module.
    - to read and write in height and width registers, the address will 
    be as following (uint32_t)((AXI_LITE_ADDRESS | 0x800)),
    first 16 bits are representing the height and second 16 bits are
    representing the width register.
    - to read and write the allowed cycles for every frame, the
    address will be (uint32_t)((AXI_LITE_ADDRESS | 0x800) + 1),
    keep in mind this is only 24-bits register.
    - to read from debug module register, the address will be as
    following (uint32_t)((AXI_LITE_ADDRESS | 0x1000) + reg_index),
    reg_index is between 0 and 7.
    - to check how ssss values are set, you may refer to encoding
    module where the Huffman BRAM originally defined.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from axi3_pkg import *
from axi3_lite_pkg import *
import constraints
import debug_module
import clk_domains

#reference: https://github.com/apertus-open-source-cinema/axiom-beta-firmware/blob/master/peripherals/soc_main/reg_file.vhd

class CoreAxiLite(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16

		# clk and resets
		self.s_axi_aclk = Signal(1)
		self.s_axi_areset_n = Signal(1)

		# axi lite buses
		self.s_axi_ro = Record(axi3ml_read_in_r)	#out
		self.s_axi_ri = Record(axi3ml_read_out_r)	#in
		self.s_axi_wo = Record(axi3ml_write_in_r)	#out
		self.s_axi_wi = Record(axi3ml_write_out_r)	#in

		# height and width for signals
		self.height = Signal(16)
		self.width = Signal(16)

		# allowed cycles for every frame
		self.allowed_cycles = Signal(24)

		# ssss huffman data to encoders
		self.bd = config['bit_depth']
		self.mem_depth = self.bd+1
		self.mem_width = self.bd+21

		# debug module enabled?
		self.debug = config['axi_lite_debug']

		# ssss write port
		self.wp_addr = Signal(5)
		self.wp_data = Signal(self.bd+21)
		self.wp_en = Signal(1)

		# ssss read port
		self.rp_addr = Signal(5)
		self.rp_data = Signal(self.bd+21)

		# debug register
		if self.debug:
			#debug module
			self.debug_module = debug_module.DebugModule()
			#debug enables
			self.debug_en = Signal(8)

		# height and width registers
		self.height_width = Signal(32)

		self.ios = \
			[self.s_axi_aclk, self.s_axi_areset_n] + \
			[self.height, self.width] + \
			[self.allowed_cycles] + \
			[self.wp_addr, self.wp_data, self.wp_en] + \
			[self.rp_addr, self.rp_data] + \
			[self.s_axi_ro.arready, self.s_axi_ro.rdata] + \
			[self.s_axi_ro.rresp, self.s_axi_ro.rvalid] + \
			[self.s_axi_ri.araddr, self.s_axi_ri.arprot] + \
			[self.s_axi_ri.arvalid, self.s_axi_ri.rready] + \
			[self.s_axi_wo.awready, self.s_axi_wo.wready] + \
			[self.s_axi_wo.bresp, self.s_axi_wo.bvalid] + \
			[self.s_axi_wi.awaddr, self.s_axi_wi.awprot] + \
			[self.s_axi_wi.awvalid, self.s_axi_wi.wdata] + \
			[self.s_axi_wi.wstrb, self.s_axi_wi.wvalid] + \
			[self.s_axi_wi.bready]

		self.axi_ios = \
			[self.s_axi_aclk, self.s_axi_areset_n] + \
			[self.s_axi_ro.arready, self.s_axi_ro.rdata] + \
			[self.s_axi_ro.rresp, self.s_axi_ro.rvalid] + \
			[self.s_axi_ri.araddr, self.s_axi_ri.arprot] + \
			[self.s_axi_ri.arvalid, self.s_axi_ri.rready] + \
			[self.s_axi_wo.awready, self.s_axi_wo.wready] + \
			[self.s_axi_wo.bresp, self.s_axi_wo.bvalid] + \
			[self.s_axi_wi.awaddr, self.s_axi_wi.awprot] + \
			[self.s_axi_wi.awvalid, self.s_axi_wi.wdata] + \
			[self.s_axi_wi.wstrb, self.s_axi_wi.wvalid] + \
			[self.s_axi_wi.bready]

		if self.debug:
			self.ios += [self.debug_en]

	def elaborate(self, platform):

		m = Module()

		if self.debug:
			# registers
			self.debug_regs = Array(Signal(32) for _ in range(8))
			# module
			m.submodules.debug_module = debug_module = self.debug_module
			#connect them
			m.d.comb += debug_module.regs_en.eq(self.debug_en)
			m.d.comb += [m_reg.eq(d_reg) for m_reg, d_reg in zip(self.debug_regs, debug_module.registers)]

		clk_domains.load_clk(m)

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

		# wires for addressing operations
		ssss_enable = Signal(1)
		hw_enable = Signal(1)
		debug_enable = Signal(1)
		ssss_index = Signal(6)
		debug_index = Signal(3)
		hw_index = Signal(1)

		m.d.comb += [
			ssss_enable.eq(addr_v[10]),
			hw_enable.eq(addr_v[11]),
			debug_enable.eq(addr_v[12]),
			ssss_index.eq(addr_v),
			debug_index.eq(addr_v),
			hw_index.eq(addr_v),
		]

		# height and width registers
		height_width = self.height_width

		# ssss wires to extend data to 64bits
		rp_data64_in = Signal(64)
		rp_data64 = Signal(64)
		m.d.comb += rp_data64.eq(self.rp_data)
		m.d.comb += rp_data64_in.eq(0)

		# function that handle read/write operations on height and width register
		def read_hw():
			with m.If(hw_index==0):
				m.d.full += [
					rdata_v.eq(height_width),
					rresp_v.eq(0),
				]
			with m.Else():
				m.d.full += [
					rdata_v.eq(self.allowed_cycles),
					rresp_v.eq(0),
				]

		def write_to_hw():
			for i in range(4):
				start = i*8
				end = start+8
				with m.If(wstrb_v[i]):
					with m.If(hw_index==0):
						m.d.full += height_width[start:end].eq(wdata_v[start:end])
					with m.Else():
						if end <= 24:
							m.d.full += self.allowed_cycles[start:end].eq(wdata_v[start:end])
			m.d.full += bresp_v.eq(0)

		def clean_write_hw():
			pass

		# functions that handle read/write operations to memory that has ssss data 
		def read_ssss():
			# first 32 bits
			with m.If(ssss_index[0]==0):
				m.d.full += rdata_v.eq(rp_data64[0:32])
			# second 32 bits
			with m.Else():
				m.d.full += rdata_v.eq(rp_data64[32:64])
			m.d.full += rresp_v.eq(0)

		def write_to_ssss():							
			# first 32 bits
			with m.If(ssss_index[0]==0):
				for i in range(4):
					start = i*8
					end = start+8
					with m.If(wstrb_v[i]):
						m.d.comb += rp_data64_in[start:end].eq(wdata_v[start:end])
					with m.Else():
						m.d.comb += rp_data64_in[start:end].eq(rp_data64[start:end])
			# second 32 bits
			with m.Else():
				for i in range(4):
					start = 32 + i*8
					end = start+8
					with m.If(wstrb_v[i]):
						m.d.comb += rp_data64_in[start:end].eq(wdata_v[start:end])
					with m.Else():
						m.d.comb += rp_data64_in[start:end].eq(rp_data64[start:end])
			m.d.full += [
				self.wp_addr.eq((ssss_index >> 1)),
				self.wp_data.eq(rp_data64_in),
				self.wp_en.eq(1),
				bresp_v.eq(0),
			]

		def clean_write_ssss():
			m.d.full += self.wp_en.eq(0)

		# functions that handle read operation to debug.
		def read_debug():
			m.d.full += [
				rdata_v.eq(self.debug_regs[debug_index]),
				rresp_v.eq(0),
			]

		def write_to_debug():							
			m.d.full += bresp_v.eq(2)

		def clean_write_debug():
			pass

		with m.FSM() as main:

			with m.State("IDLE"):
				#needed from other states
				m.d.full += [
					rvalid_v.eq(0),
					bvalid_v.eq(0),
				]
				#read operation
				with m.If(self.s_axi_ri.arvalid):
					m.next = "READ_ADDRESS"
				with m.Elif(self.s_axi_wi.awvalid):
					m.next = "WRITE_ADDRESS"


			with m.State("READ_ADDRESS"):
				# ack address, ready for transfer
				m.d.full += [
					addr_v.eq(self.s_axi_ri.araddr >> 2),
					self.rp_addr.eq(self.s_axi_ri.araddr >> 3),
					arready_v.eq(1),
				]
				m.next = "READ_DATA_DELAY1"


			with m.State("READ_DATA_DELAY1"):
				m.d.full += arready_v.eq(0)	# done
				m.next = "READ_DATA_DELAY2"


			with m.State("READ_DATA_DELAY2"):
				m.next = "READ_DATA"


			with m.State("READ_DATA"):
				# ssss bram
				with m.If((ssss_enable == 1) & (ssss_index < 2*self.mem_depth)):
					read_ssss()
				# height & width
				with m.Elif(hw_enable == 1):
					read_hw()
				# debug
				if self.debug:
					with m.Elif(debug_enable == 1):
						read_debug()
				# decode error
				with m.Else():
					m.d.full += rresp_v.eq(3)
				# to finish
				with m.If(self.s_axi_ri.rready):
					m.d.full += rvalid_v.eq(1)
					m.next = "IDLE"


			with m.State("WRITE_ADDRESS"):
				# ack address, ready for transfer
				m.d.full += [
					addr_v.eq(self.s_axi_wi.awaddr >> 2),
					self.rp_addr.eq(self.s_axi_wi.awaddr >> 3),
					awready_v.eq(1),
				]
				m.next = "WRITE_DATA_DELAY1"


			with m.State("WRITE_DATA_DELAY1"):
				m.d.full += awready_v.eq(0)	# done
				m.next = "WRITE_DATA_DELAY2"


			with m.State("WRITE_DATA_DELAY2"):
				m.next = "WRITE_DATA"


			with m.State("WRITE_DATA"):
				m.d.full += wready_v.eq(1)	# ready for data
				with m.If(self.s_axi_wi.wvalid):
					m.d.comb += [
						wdata_v.eq(self.s_axi_wi.wdata),
						wstrb_v.eq(self.s_axi_wi.wstrb),
					]
					# ssss bram
					with m.If((ssss_enable == 1) & (ssss_index < 2*self.mem_depth)):
						write_to_ssss()	
					# height & width
					with m.Elif(hw_enable == 1):
						write_to_hw()
					# debug
					if self.debug:
						with m.Elif(debug_enable == 1):
							write_to_debug()
					# decode error
					with m.Else():
						m.d.full += bresp_v.eq(3)
					m.next = "WRITE_RESPONSE"


			with m.State("WRITE_RESPONSE"):
				if self.debug:
					clean_write_debug()
				clean_write_hw()
				clean_write_ssss()
				m.d.full += wready_v.eq(0)
				with m.If(self.s_axi_wi.bready):
					m.d.full += bvalid_v.eq(1)
					m.next = "IDLE"

		m.d.comb += [
			self.s_axi_ro.arready.eq(arready_v),
			self.s_axi_ro.rvalid.eq(rvalid_v),
		]

		m.d.comb += [
			self.s_axi_wo.awready.eq(awready_v),
			self.s_axi_wo.wready.eq(wready_v),
			self.s_axi_wo.bvalid.eq(bvalid_v),
		]

		m.d.comb += [
			self.s_axi_ro.rdata.eq(rdata_v),
			self.s_axi_ro.rresp.eq(rresp_v),
		]

		m.d.comb += [
			self.s_axi_wo.bresp.eq(bresp_v),
		]

		m.d.comb += [
			self.height.eq(height_width[0:16]),
			self.width.eq(height_width[16:32]),
		]

		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 12,
		"axi_lite_debug": True,
	}
	d = CoreAxiLite(config, constraints.Constraints())
	main(d, ports=d.ios)