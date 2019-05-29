from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *

class SingleMerger(Elaboratable):

	def __init__(self, width):

		self.enc_in1 = Signal(width)
		self.enc_in_ctr1 = Signal(int(log(width, 2)) + 1)

		self.enc_in2 = Signal(width)
		self.enc_in_ctr2 = Signal(int(log(width, 2)) + 1)

		self.enc_out = Signal(width * 2)
		self.enc_out_ctr = Signal(int(log(width, 2)) + 2)

		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.ios = \
			[self.enc_in1, self.enc_in_ctr1] + \
			[self.enc_in2, self.enc_in_ctr2] + \
			[self.enc_out, self.enc_out_ctr] + \
			[self.valid_in, self.valid_out]

	def elaborate(self, platform):

		m = Module()

		with m.If(self.valid_in):
			m.d.sync += [
				self.enc_out_ctr.eq(self.enc_in_ctr1 + self.enc_in_ctr2),
				self.enc_out.eq((self.enc_in1 << self.enc_in_ctr2) | (self.enc_in2)),
			]

		#if valid data
		m.d.sync += self.valid_out.eq(self.valid_in)

		return m

class Merge(Elaboratable):

	def __init__(self):

		self.enc_in1 = Signal(31)
		self.enc_in_ctr1 = Signal(5)
		self.enc_in2 = Signal(31)
		self.enc_in_ctr2 = Signal(5)
		self.enc_in3 = Signal(31)
		self.enc_in_ctr3 = Signal(5)
		self.enc_in4 = Signal(31)
		self.enc_in_ctr4 = Signal(5)

		self.enc_out = Signal(124)
		self.enc_out_ctr = Signal(7)

		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.merger_lvl1_1 = SingleMerger(31)
		self.merger_lvl1_2 = SingleMerger(31)
		self.merger_lvl2 = SingleMerger(62)

		self.ios = \
			[self.enc_in1, self.enc_in_ctr1] + \
			[self.enc_in2, self.enc_in_ctr2] + \
			[self.enc_in3, self.enc_in_ctr3] + \
			[self.enc_in4, self.enc_in_ctr4] + \
			[self.enc_out, self.enc_out_ctr] + \
			[self.valid_in, self.valid_out]


	def elaborate(self, platform):

		m = Module()

		m.submodules.merger_lvl1_1 = mlv11 = self.merger_lvl1_1
		m.submodules.merger_lvl1_2 = mlv12 = self.merger_lvl1_2
		m.submodules.merger_lvl2 = mlv2 = self.merger_lvl2

		# main with mlv11
		m.d.comb += [
			mlv11.enc_in1.eq(self.enc_in1),
			mlv11.enc_in_ctr1.eq(self.enc_in_ctr1),
			mlv11.enc_in2.eq(self.enc_in2),
			mlv11.enc_in_ctr2.eq(self.enc_in_ctr2),
			mlv11.valid_in.eq(self.valid_in),
		]

		# main with mlv12
		m.d.comb += [
			mlv12.enc_in1.eq(self.enc_in3),
			mlv12.enc_in_ctr1.eq(self.enc_in_ctr3),
			mlv12.enc_in2.eq(self.enc_in4),
			mlv12.enc_in_ctr2.eq(self.enc_in_ctr4),
			mlv12.valid_in.eq(self.valid_in),
		]

		# mlv11 and mlv12 with mlv2
		m.d.comb += [
			mlv2.enc_in1.eq(mlv11.enc_out),
			mlv2.enc_in_ctr1.eq(mlv11.enc_out_ctr),
			mlv2.enc_in2.eq(mlv12.enc_out),
			mlv2.enc_in_ctr2.eq(mlv12.enc_out_ctr),
			mlv2.valid_in.eq(mlv11.valid_out),
		]

		#mlv2 with main
		m.d.comb += [
			self.enc_out.eq(mlv2.enc_out),
			self.enc_out_ctr.eq(mlv2.enc_out_ctr),
			self.valid_out.eq(mlv2.valid_out),
		]

		return m

if __name__ == "__main__":
	m = Merge()
	main(m, ports=m.ios)