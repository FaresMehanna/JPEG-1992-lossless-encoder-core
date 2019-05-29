from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *
import random

class Difference(Elaboratable):

	def __init__(self):

		self.pixel_in1 = Signal(16)
		self.pixel_in2 = Signal(16)
		self.pixel_in3 = Signal(16)
		self.pixel_in4 = Signal(16)

		self.predic_in1 = Signal(16)
		self.predic_in2 = Signal(16)
		self.predic_in3 = Signal(16)
		self.predic_in4 = Signal(16)

		self.val_out1 = Signal(17)
		self.val_out2 = Signal(17)
		self.val_out3 = Signal(17)
		self.val_out4 = Signal(17)
		
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.ios = \
			[self.pixel_in1, self.pixel_in2, self.pixel_in3, self.pixel_in4] + \
			[self.predic_in1, self.predic_in2, self.predic_in3, self.predic_in4] + \
			[self.val_out1, self.val_out2, self.val_out3, self.val_out4] + \
			[self.valid_in, self.valid_out]


	def elaborate(self, platform):

		m = Module()

		#if valid data
		with m.If(self.valid_in):
			m.d.sync += [
				self.val_out1.eq(self.pixel_in1-self.predic_in1),
				self.val_out2.eq(self.pixel_in2-self.predic_in2),
				self.val_out3.eq(self.pixel_in3-self.predic_in3),
				self.val_out4.eq(self.pixel_in4-self.predic_in4),
			]

		#if valid data
		m.d.sync += self.valid_out.eq(self.valid_in)

		return m

if __name__ == "__main__":
	d = Difference()
	main(d, ports=d.ios)