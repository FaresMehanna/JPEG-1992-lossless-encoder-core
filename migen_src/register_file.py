from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

class RegisterFile(Elaboratable):

	def __init__(self):

		self.height = Signal(16)
		self.width = Signal(16)

		self.ios = \
		[self.height, self.width]


	def elaborate(self, platform):
		m = Module()

		width_reg = Signal(16)
		height_reg = Signal(16)

		m.d.sync += [
			width_reg.eq(4096),
			height_reg.eq(3072),
		]

		m.d.comb += [
			self.width.eq(width_reg),
			self.height.eq(height_reg),
		]

		return m

if __name__ == "__main__":
	m = RegisterFile()
	main(m, ports=m.ios)