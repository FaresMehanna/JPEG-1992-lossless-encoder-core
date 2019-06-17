from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

def logic(data_in, data_out, data_out_ctr, zeros, ones, m):
	# 0xFF 0x00 0xFF 0x00
	with m.If(data_in[0:16] == 0xFFFF):
		m.d.sync += [
			data_out.eq(Cat(zeros, ones, zeros, ones)),
			data_out_ctr.eq(4),
		]
	# 0xZZ 0xFF 0x00
	with m.Elif(data_in[0:8] == 0xFF):
		m.d.sync += [
			data_out.eq(Cat(zeros, ones, data_in[8:16])),
			data_out_ctr.eq(3),
		]
	# 0xFF 0x00 0xZZ
	with m.Elif(data_in[8:16] == 0xFF):
		m.d.sync += [
			data_out.eq(Cat(data_in[0:8], zeros, ones)),
			data_out_ctr.eq(3),
		]
	with m.Else():
		m.d.sync += [
			data_out.eq(data_in),
			data_out_ctr.eq(2),
		]

class Fix0xFF(Elaboratable):

	def __init__(self):

		#data in
		self.data_in = Signal(16)

		#data out
		self.data_out = Signal(32)
		self.data_out_ctr = Signal(max=4+1)

		#signals
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)
		self.o_busy = Signal(1)	#I'm busy
		self.i_busy = Signal(1)	#next not busy

		self.ios = \
			[self.valid_in, self.valid_out, self.o_busy, self.i_busy] + \
			[self.data_out, self.data_out_ctr, self.data_in]

	def elaborate(self, platform):
		m = Module()
		
		zeros = Signal(8)
		ones = Signal(8, reset=0xFF)

		data_out_reg = Signal(32)
		data_out_ctr_reg = Signal(max=5)
		data_out_valid = Signal(1)

		# please refer to: https://zipcpu.com/blog/2017/08/14/strategies-for-pipelining.html
		# for understanding "The buffered handshake"

		#next is not busy
		with m.If(self.i_busy == 0):
			with m.If(data_out_valid == 0):
				m.d.sync += self.valid_out.eq(self.valid_in),
				logic(self.data_in, self.data_out, self.data_out_ctr, zeros, ones, m)
			with m.Else():
				m.d.sync += [
					self.valid_out.eq(1),
					self.data_out.eq(data_out_reg),
					self.data_out_ctr.eq(data_out_ctr_reg),
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
			logic(self.data_in, self.data_out, self.data_out_ctr, zeros, ones, m)
		#next is busy and there is valid data and there is registered valid data
		#and this core is not busy
		with m.Elif((self.valid_in==1) & (self.o_busy == 0)):
			m.d.sync += [
				data_out_valid.eq((self.valid_in==1) & (self.valid_out==1)),
				self.o_busy.eq((self.valid_in==1) & (self.valid_out==1)),
			]

		with m.If(self.o_busy == 0):
			logic(self.data_in, data_out_reg, data_out_ctr_reg, zeros, ones, m)

		return m


if __name__ == "__main__":
	d = Fix0xFF()
	main(d, ports=d.ios)