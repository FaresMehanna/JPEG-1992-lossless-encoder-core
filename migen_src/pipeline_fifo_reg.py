from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class PipelineFifoReg(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		#save some data
		single_data_bits = min(16+config['bit_depth'], 31)
		self.data_bits = single_data_bits*config['pixels_per_cycle']
		self.active_reg = config['pipeline_fifo_reg']

		# pipeline_fifo
		self.o_busy = Signal(1)
		self.enc_left = Signal(self.data_bits)
		self.enc_ctr_left = Signal(max=self.data_bits+1)
		self.out_end_left = Signal(1)
		self.valid_left = Signal(1)

		# converter
		self.i_busy = Signal(1)
		self.enc_right = Signal(self.data_bits)
		self.enc_ctr_right = Signal(max=self.data_bits+1)
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
			
			enc_right_reg = Signal(self.data_bits)
			enc_ctr_right_reg = Signal(max=self.data_bits+1)
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
		"bit_depth" : 12,
		"pixels_per_cycle": 4,
		"pipeline_fifo_reg": True,
	}
	d = PipelineFifoReg(config, constraints.Constraints())
	main(d, ports=d.ios)