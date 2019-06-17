from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class VBitsToCBitsReg(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['out_bits'] >= 1

		#save some data
		self.output_size = config['out_bits']
		self.active_reg = config['vbits_to_cbits_reg']

		# VBitsToCBits
		self.o_busy = Signal(1)
		self.data_left = Signal(self.output_size)
		self.valid_left = Signal(1)
		self.end_left = Signal(1)

		# fixer
		self.i_busy = Signal(1)
		self.data_right = Signal(self.output_size)
		self.valid_right = Signal(1)
		self.end_right = Signal(1)

		self.ios = \
		[self.o_busy, self.data_left, self.valid_left, self.end_left] + \
		[self.i_busy, self.data_right, self.valid_right, self.end_right]


	def elaborate(self, platform):

		m = Module()

		# please refer to: https://zipcpu.com/blog/2017/08/14/strategies-for-pipelining.html
		# for understanding "The buffered handshake"

		if self.active_reg:
			
			data_reg = Signal(self.output_size)
			end_reg = Signal(1)
			data_out_valid = Signal(1)

			#next is not busy
			with m.If(self.i_busy == 0):
				with m.If(data_out_valid == 0):
					m.d.sync += [
						self.data_right.eq(self.data_left),
						self.end_right.eq(self.end_left),
						self.valid_right.eq(self.valid_left),
					]
				with m.Else():
					#output data
					#set valid to one
					m.d.sync += [
						self.valid_right.eq(1),
						self.data_right.eq(data_reg),
						self.end_right.eq(end_reg),
					]
				m.d.sync += [
					self.o_busy.eq(0),
					data_out_valid.eq(0),
				]
			#next is busy and no valid data
			with m.Elif(self.valid_right == 0):
				m.d.sync += [
					self.o_busy.eq(0),
					data_out_valid.eq(0),
				]
				m.d.sync += [
					self.data_right.eq(self.data_left),
					self.end_right.eq(self.end_left),
					self.valid_right.eq(self.valid_left),
				]
			#next is busy and there is valid data and there is registered valid data
			#and this core is not busy
			with m.Elif((self.valid_left==1) & (self.o_busy == 0)):
				m.d.sync += [
					data_out_valid.eq((self.valid_left==1) & (self.valid_right==1)),
					self.o_busy.eq((self.valid_left==1) & (self.valid_right==1)),
				]

			with m.If(self.o_busy == 0):
				m.d.sync += [
					data_reg.eq(self.data_left),
					end_reg.eq(self.end_left),
				]
		else:
			m.d.comb += [
				self.o_busy.eq(self.i_busy),
				self.data_right.eq(self.data_left),
				self.valid_right.eq(self.valid_left),
				self.end_right.eq(self.end_left),
			]
		return m

if __name__ == "__main__":
	config = {
		"out_bits" : 16,
		"vbits_to_cbits_reg": True,
	}
	d = VBitsToCBitsReg(config, constraints.Constraints())
	main(d, ports=d.ios)