from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *

class Predictor(Elaboratable):

	def __init__(self):

		#pixels in
		self.pixel_in1 = Signal(16)
		self.pixel_in2 = Signal(16)
		self.pixel_in3 = Signal(16)
		self.pixel_in4 = Signal(16)

		#new row signal
		self.new_row = Signal(1)

		#same pixels in
		self.pixel_out1 = Signal(16)
		self.pixel_out2 = Signal(16)
		self.pixel_out3 = Signal(16)
		self.pixel_out4 = Signal(16)

		#prediction using P1
		self.predic_out1 = Signal(16)
		self.predic_out2 = Signal(16)
		self.predic_out3 = Signal(16)
		self.predic_out4 = Signal(16)

		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.ios = \
			[self.pixel_in1, self.pixel_in2, self.pixel_in3, self.pixel_in4] + \
			[self.pixel_out1, self.pixel_out2, self.pixel_out3, self.pixel_out4] + \
			[self.predic_out1, self.predic_out2, self.predic_out3, self.predic_out4] + \
			[self.valid_in, self.valid_out]

	def elaborate(self, platform):

		m = Module()

		#buffer values
		buff1 = Signal(16, reset=2**(BIT_DEPTH-1))
		buff2 = Signal(16, reset=2**(BIT_DEPTH-1))
		buff3 = Signal(16, reset=2**(BIT_DEPTH-1))
		buff4 = Signal(16, reset=2**(BIT_DEPTH-1))

		#last row buffer
		lbuff1 = Signal(16, reset=2**(BIT_DEPTH-1))
		lbuff2 = Signal(16, reset=2**(BIT_DEPTH-1))
		lbuff3 = Signal(16, reset=2**(BIT_DEPTH-1))
		lbuff4 = Signal(16, reset=2**(BIT_DEPTH-1))

		with m.If(self.valid_in):
			#handle pixel_out1
			m.d.sync += [
				self.pixel_out1.eq(self.pixel_in1),
				self.pixel_out2.eq(self.pixel_in2),
				self.pixel_out3.eq(self.pixel_in3),
				self.pixel_out4.eq(self.pixel_in4),
			]

			#handle prediction
			with m.If(self.new_row):
				m.d.sync += [
					self.predic_out1.eq(lbuff1),
					self.predic_out2.eq(lbuff2),
					self.predic_out3.eq(lbuff3),
					self.predic_out4.eq(lbuff4),
				]
			with m.Else():
				m.d.sync += [
					self.predic_out1.eq(buff1),
					self.predic_out2.eq(buff2),
					self.predic_out3.eq(buff3),
					self.predic_out4.eq(buff4),
				]

			#handle row-buffer update
			with m.If(self.new_row):
				m.d.sync += [
					lbuff1.eq(self.pixel_in1),
					lbuff2.eq(self.pixel_in2),
					lbuff3.eq(self.pixel_in3),
					lbuff4.eq(self.pixel_in4),
				]

			#handle ordinary-buffers
			m.d.sync += [
				buff1.eq(self.pixel_in1),
				buff2.eq(self.pixel_in2),
				buff3.eq(self.pixel_in3),
				buff4.eq(self.pixel_in4),
			]

		#if valid data
		m.d.sync += self.valid_out.eq(self.valid_in)

		return m

if __name__ == "__main__":
	p = Predictor()
	main(p, ports=p.ios)