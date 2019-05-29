from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *

class SingleNormalizer(Elaboratable):

	def __init__(self):

		self.val_in = Signal(17)
		self.val_out = Signal(16)
		self.ssss = Signal(5)
		self.valid = Signal(1)

		self.ios = \
			[self.val_in, self.val_out, self.ssss, self.valid]

	def elaborate(self, platform):

		m = Module()

		# if valid data
		with m.If(self.valid):
			# if negative
			with m.If(self.val_in[16] == 1):
				# normalize the negative values to positive one
				# and calculate the ssss class of the input
				with m.If(self.val_in == 0x1FFFF):
					m.d.sync += [
						self.ssss.eq(1),
						self.val_out.eq(self.val_in + 1),
					]
				l = 0x1FFFF
				for i in range(1, 16):
					with m.Elif(self.val_in >= (l - 2**i)):
						l = (l - 2**i)
						m.d.sync += [
							self.ssss.eq(i+1),
							self.val_out.eq(self.val_in + (2**(i+1)) - 1),
						]
			# if positive
			with m.Else():
				# output the same input
				m.d.sync += [
					self.val_out.eq(self.val_in),
				]
				# calculate the ssss class of the input
				with m.If(self.val_in[15]):
					m.d.sync += [
						self.ssss.eq(16),
					]
				for i in range(1, 16):
					with m.Elif(self.val_in[15-i]):
						m.d.sync += [
							self.ssss.eq(16-i),
						]
				with m.Else():
					m.d.sync += [
						self.ssss.eq(0),
					]
		return m


class Normalize(Elaboratable):

	def __init__(self):

		self.val_in1 = Signal(17)
		self.val_in2 = Signal(17)
		self.val_in3 = Signal(17)
		self.val_in4 = Signal(17)

		self.val_out1 = Signal(16)
		self.val_out2 = Signal(16)
		self.val_out3 = Signal(16)
		self.val_out4 = Signal(16)

		self.ssss1 = Signal(5)
		self.ssss2 = Signal(5)
		self.ssss3 = Signal(5)
		self.ssss4 = Signal(5)

		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.pixel1 = SingleNormalizer()
		self.pixel2 = SingleNormalizer()
		self.pixel3 = SingleNormalizer()
		self.pixel4 = SingleNormalizer()

		self.ios = \
			[self.val_in1, self.val_in2, self.val_in3, self.val_in4] + \
			[self.val_out1, self.val_out2, self.val_out3, self.val_out4] + \
			[self.ssss1, self.ssss2, self.ssss3, self.ssss4] + \
			[self.valid_in, self.valid_out]


	def elaborate(self, platform):

		m = Module()

		m.submodules.pixel1 = pixel1 = self.pixel1
		m.submodules.pixel2 = pixel2 = self.pixel2
		m.submodules.pixel3 = pixel3 = self.pixel3
		m.submodules.pixel4 = pixel4 = self.pixel4

		m.d.comb += [
			pixel1.val_in.eq(self.val_in1),
			pixel1.valid.eq(self.valid_in),
			self.ssss1.eq(pixel1.ssss),
			self.val_out1.eq(pixel1.val_out),
			pixel2.val_in.eq(self.val_in2),
			pixel2.valid.eq(self.valid_in),
			self.ssss2.eq(pixel2.ssss),
			self.val_out2.eq(pixel2.val_out),
			pixel3.val_in.eq(self.val_in3),
			pixel3.valid.eq(self.valid_in),
			self.ssss3.eq(pixel3.ssss),
			self.val_out3.eq(pixel3.val_out),
			pixel4.val_in.eq(self.val_in4),
			pixel4.valid.eq(self.valid_in),
			self.ssss4.eq(pixel4.ssss),
			self.val_out4.eq(pixel4.val_out),
		]

		#if valid data
		m.d.sync += self.valid_out.eq(self.valid_in)
		return m

if __name__ == "__main__":
	n = Normalize()
	main(n, ports=n.ios)