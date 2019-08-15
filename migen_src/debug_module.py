'''
--------------------
Module: debug_module
--------------------
Description: 
    - when some debugging info is required this module
    can be used to gather some run-time data.
    this module is simply 8 counters that get incremented
    when active signal is asserted.
--------------------
Input: 
    - 8 activate signals.
--------------------
Output:
    - 8 counters.
--------------------
timing:
    - No need for time analysis for this module.
--------------------
Notes :
    - this module is optional and can only be
    used with axi lite module to access theses
    counters from PS.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
import clk_domains

class DebugModule(Elaboratable):

	def __init__(self):

		self.registers = Array(Signal(32) for _ in range(8))
		self.regs_en = Signal(8)

		self.ios = \
			[reg for reg in self.registers] + \
			[self.regs_en]


	def elaborate(self, platform):

		m = Module()

		clk_domains.load_clk(m)

		for i in range(8):
			with m.If(self.regs_en[i]):
				m.d.full += self.registers[i].eq(self.registers[i] + 1)

		return m


if __name__ == "__main__":
	d = DebugModule()
	main(d, ports=d.ios)