'''
--------------------
Module: register_file
--------------------
Description: 
    - register_file is a component where some values are stored
    and outputted for any other component to use.
--------------------
Input: 
    - no input.
--------------------
Output:
    - height and width of the frame.
--------------------
timing:
    - always same values.
--------------------
Notes :
    - this module is optional since height and width
    are existed in Axi-lite module for access from PS,
    so if axi lite is used, then no need to use this 
    module.
--------------------
'''

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