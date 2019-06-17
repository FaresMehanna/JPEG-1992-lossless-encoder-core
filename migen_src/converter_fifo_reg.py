from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class ConverterFifoReg(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['converter'] >= 1

		#save some data
		self.data_width = config['converter']
		self.ctr_bits = ceil(log(config['converter']+1, 2))
		self.total_bits = self.data_width + self.ctr_bits + 1
		self.active_reg = config['converter_fifo_reg']

		# converter_fifo
		self.o_busy = Signal(1)
		self.enc_left = Signal(self.data_width)
		self.enc_ctr_left = Signal(self.ctr_bits)
		self.out_end_left = Signal(1)
		self.valid_left = Signal(1)

		# vbits_to_cbits
		self.i_busy = Signal(1)
		self.enc_right = Signal(self.data_width)
		self.enc_ctr_right = Signal(self.ctr_bits)
		self.out_end_right = Signal(1)
		self.valid_right = Signal(1)

		self.ios = \
		[self.o_busy, self.enc_left, self.enc_ctr_left, self.out_end_left, self.valid_left] + \
		[self.i_busy, self.enc_right, self.enc_ctr_right, self.out_end_right, self.valid_right]


	def elaborate(self, platform):

		m = Module()

		# please refer to: https://zipcpu.com/blog/2017/08/14/strategies-for-pipelining.html
		# for understanding "The buffered handshake"

		if self.active_reg:
			
			enc_right_reg = Signal(self.data_width)
			enc_ctr_right_reg = Signal(self.ctr_bits)
			out_end_right_reg = Signal(1)

			data_out_valid = Signal(1)

			#next is not busy
			with m.If(self.i_busy == 0):
				with m.If(data_out_valid == 0):
					m.d.sync += [
						self.enc_right.eq(self.enc_left),
						self.enc_ctr_right.eq(self.enc_ctr_left),
						self.out_end_right.eq(self.out_end_left),
						self.valid_right.eq(self.valid_left),
					]
				with m.Else():
					#output data
					#set valid to one
					m.d.sync += [
						self.valid_right.eq(1),
						self.enc_right.eq(enc_right_reg),
						self.enc_ctr_right.eq(enc_ctr_right_reg),
						self.out_end_right.eq(out_end_right_reg),
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
					self.enc_right.eq(self.enc_left),
					self.enc_ctr_right.eq(self.enc_ctr_left),
					self.out_end_right.eq(self.out_end_left),
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
					enc_right_reg.eq(self.enc_left),
					enc_ctr_right_reg.eq(self.enc_ctr_left),
					out_end_right_reg.eq(self.out_end_left),
				]
		else:
			m.d.comb += [
				self.o_busy.eq(self.i_busy),
				self.enc_right.eq(self.enc_left),
				self.enc_ctr_right.eq(self.enc_ctr_left),
				self.out_end_right.eq(self.out_end_left),
				self.valid_right.eq(self.valid_left),
			]
		return m

if __name__ == "__main__":
	config = {
		"converter": 36,
		"converter_fifo_reg": True,
	}
	d = ConverterFifoReg(config, constraints.Constraints())
	main(d, ports=d.ios)