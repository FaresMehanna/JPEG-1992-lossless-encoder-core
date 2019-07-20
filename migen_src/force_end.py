'''
--------------------
Module: force_end
--------------------
Description: 
    - force_end is a module to indicate that a force end
    must occur, since the current frame took too much cycles.
    - It work by counting every cycle after the first valid
    input.
--------------------
Input: 
    - allowed_cycles signal.
    - valid_in signal.
--------------------
Output:
    - force_end signal.
--------------------
timing:
    - after the first valid_in by allowed_cycles, it will
    set force_end to 1.
--------------------
Notes :
    - this module is optional but it should be used as the
    marker module make a use of it and will use a different
    marking if the force end is signaled.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
import constraints

class ForceEnd(Elaboratable):

	def __init__(self, config, constraints):

		self.valid_in = Signal(1)
		self.allowed_cycles = Signal(24)

		self.fend = Signal(1)

		self.ios = \
		[self.valid_in, self.allowed_cycles, self.fend]


	def elaborate(self, platform):

		m = Module()

		counter = Signal(24)

		with m.FSM() as fsm:
			
			with m.State("IDLE"):
				with m.If(self.valid_in):
					m.next = "COUNTING"

			with m.State("COUNTING"):
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == self.allowed_cycles):
					m.next = "END"

			with m.State("END"):
				m.d.sync += self.fend.eq(1)

		return m

if __name__ == "__main__": 
	m = ForceEnd({}, constraints.Constraints())
	main(m, ports=m.ios)