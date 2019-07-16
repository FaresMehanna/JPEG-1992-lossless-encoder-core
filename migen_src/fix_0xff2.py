'''
--------------------
Module: fix_0xff2
--------------------
Description: 
    - fix_0xff is the second step in two steps to fix the 0xff
    bytes, in LJ92 standard, every 0xFF byte must be followed
    with 0x00 byte.
    This module will convert 4 bytes variable size into two
    bytes for the output.
--------------------
Input: 
    - single signal with variable number of bytes - must be 4-bytes for now.
--------------------
Output:
    - single signal with constant number of bytes - must be 2-bytes for now.
--------------------
timing:
    - result ready in the next rising edge.
--------------------
Notes :
    - this module handle only constant number of bytes, 2 only.
    - this module is a must to be complaint with LJ92 standard,
    but not crucial in the compressing algorithm.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

# normal_logic, represent the normal logic of input_data and
# buffer_data and the output can be processed in 1 cycle, and the
# buffer is not filled yet, if filled then the "clean_logic"
# will be called.
def normal_logic(valid_in, data_in, data_in_ctr, data_out, end_in, end_out, buffer_data, buffer_count, o_busy, m, end_reg):
	with m.If(valid_in):
		with m.Switch(buffer_count):
			#no data in buffer
			with m.Case(0):
				with m.Switch(data_in_ctr):
					with m.Case(2):
						m.d.sync += [
							data_out.eq(data_in[0:16]),
						]
					with m.Case(3):
						m.d.sync += [
							data_out.eq(data_in[8:24]),
							buffer_data.eq(data_in[0:8]),
							buffer_count.eq(1),
						]
					with m.Case(4):
						m.d.sync += [
							data_out.eq(data_in[16:32]),
							buffer_data.eq(data_in[0:16]),
							buffer_count.eq(2),
						]
						#switch to new mode!
						m.d.sync += [
							o_busy.eq(1),
						]
						m.next = "CLEAN"

			#single byte in buffer
			with m.Case(1):
				with m.Switch(data_in_ctr):
					with m.Case(2):
						m.d.sync += [
							data_out.eq(Cat(data_in[8:16], buffer_data[0:8])),
							buffer_data.eq(data_in[0:8]),
							buffer_count.eq(1),
						]
					with m.Case(3):
						m.d.sync += [
							data_out.eq(Cat(data_in[16:24], buffer_data[0:8])),
							buffer_data.eq(data_in[0:16]),
							buffer_count.eq(2),
						]
						#switch to new mode!
						m.d.sync += [
							o_busy.eq(1),
						]
						m.next = "CLEAN"
					with m.Case(4):
						m.d.sync += [
							data_out.eq(Cat(data_in[24:32], buffer_data[0:8])),
							buffer_data.eq(data_in[0:24]),
							buffer_count.eq(3),
						]
						#switch to new mode!
						m.d.sync += [
							o_busy.eq(1),
						]
						m.next = "CLEAN"
		with m.If(end_in):
			with m.If((buffer_count == 0) & (data_in_ctr == 2)):
				m.d.sync += end_out.eq(1)
				m.next = "PRE_END"
			with m.Else():
				#switch to ending mode!
				m.d.sync += [
					o_busy.eq(1),
					end_reg.eq(1),
				]
				m.next = "CLEAN"

				
# this state only happens when the buffer is filled
# with data and need to be cleaned, so this will stop
# accepting new data until the buffer is emptied.
def clean_logic(data_out, end_out, buffer_data, buffer_count, m, end_reg):
	with m.Switch(buffer_count):
		#1 byte in buffer
		with m.Case(1):
			m.d.sync += [
				data_out[8:16].eq(buffer_data[0:8]),
				data_out[0:8].eq(0x00),
				buffer_count.eq(0),
			]
		#2 bytes in buffer
		with m.Case(2):
			m.d.sync += [
				data_out.eq(buffer_data[0:16]),
				buffer_count.eq(0),
			]
		#3 bytes in buffer
		with m.Case(3):
			m.d.sync += [
				data_out.eq(buffer_data[8:24]),
				buffer_data.eq(buffer_data[0:8]),
				buffer_count.eq(1),
			]
	with m.If(end_reg):
		with m.If((buffer_count <= 2)):
			m.d.sync += end_out.eq(1)
			m.next = "END"

class Fix0xFF2(Elaboratable):

	def __init__(self):

		#data in
		self.data_in = Signal(32)
		self.data_in_ctr = Signal(max=5)

		#data out
		self.data_out = Signal(16)

		#signals
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.o_busy = Signal(1)	#I'm busy
		self.i_busy = Signal(1)	#next busy

		self.ios = \
			[self.valid_in, self.valid_out, self.o_busy, self.i_busy] + \
			[self.data_out, self.data_in_ctr, self.data_in] + \
			[self.end_in, self.end_out]

	def elaborate(self, platform):
		m = Module()

		buffer_data = Signal(24)
		buffer_count = Signal(2)

		data_out_reg = Signal(16)
		end_out_reg = Signal(1)
		data_out_valid = Signal(1)

		end_reg = Signal(1)

		with m.FSM() as pack:
			with m.State("NORMAL"):
				with m.If(self.i_busy == 0):
					with m.If(data_out_valid == 0):
						m.d.sync += self.valid_out.eq(self.valid_in)
						normal_logic(self.valid_in, self.data_in, self.data_in_ctr, self.data_out, self.end_in, self.end_out, buffer_data, buffer_count, self.o_busy, m, end_reg)
					with m.Else():
						m.d.sync += [
							self.valid_out.eq(1),
							self.data_out.eq(data_out_reg),
							self.end_out.eq(end_out_reg),
						]
					m.d.sync += [
						self.o_busy.eq(0),
						data_out_valid.eq(0),
					]
				#next is busy and no valid data
				with m.Elif(self.valid_out == 0):
					m.d.sync += [
						self.valid_out.eq(self.valid_in),
						self.o_busy.eq(0),
						data_out_valid.eq(0),
					]
					normal_logic(self.valid_in, self.data_in, self.data_in_ctr, self.data_out, self.end_in, self.end_out, buffer_data, buffer_count ,self.o_busy, m, end_reg)
				#next is busy and there is valid data and there is registered valid data
				#and this core is not busy
				with m.Elif((self.valid_in==1) & (self.o_busy == 0)):
					m.d.sync += [
						data_out_valid.eq((self.valid_in==1) & (self.valid_out==1)),
						self.o_busy.eq((self.valid_in==1) & (self.valid_out==1)),
					]

				with m.If(self.o_busy == 0):
					normal_logic(self.valid_in, self.data_in, self.data_in_ctr, data_out_reg, self.end_in, end_out_reg,  buffer_data, buffer_count ,self.o_busy, m, end_reg)
			
			with m.State("CLEAN"):
				with m.If(self.i_busy == 0):
					with m.If(data_out_valid == 0):
						clean_logic(self.data_out, self.end_out, buffer_data, buffer_count, m, end_reg)
						m.d.sync += self.valid_out.eq(1)
						with m.If(end_reg==0):
							m.d.sync += self.o_busy.eq(0)
							m.next = "NORMAL"
					with m.Else():
						m.d.sync += [
							self.valid_out.eq(1),
							self.data_out.eq(data_out_reg),
							self.end_out.eq(end_out_reg),
							data_out_valid.eq(0),
						]

			with m.State("PRE_END"):
				with m.If(self.i_busy == 0):
					with m.If(data_out_valid):
						m.d.sync += [
							self.valid_out.eq(1),
							self.data_out.eq(data_out_reg),
							self.end_out.eq(1),
						]
					m.next = "END"

			with m.State("END"):
				pass

		return m

if __name__ == "__main__":
	d = Fix0xFF2()
	main(d, ports=d.ios)