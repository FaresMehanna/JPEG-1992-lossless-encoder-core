'''
--------------------
Module: address_generator
--------------------
Description: 
    - address_generator is a simple module, using a starting address
    it will increment the address by some offset to be used in the
    axi_hp[reader/writer].
--------------------
Input: 
    - address_latch, if the address is used in this cycle.
--------------------
Output:
    - address_o, the current valid address.
    - address_valid, if the address is now valid.
--------------------
timing:
    - always calculation done in the same cycle and new data
    is ready in the next rising edge.
--------------------
Notes :
    - Only needed when using with axi_hp[reader/writer].
    - This module is not part of the LJ92 encoder.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *

class AddressGenerator(Elaboratable):

	def __init__(self, address_shift):

		self.address_o = Signal(32)		# out
		self.address_valid = Signal(1)	# out
		self.address_latch = Signal(1)	# in

		self.starting_address = Signal(32)
		self.address_shift = address_shift

		self.ios = \
		[self.address_o, self.address_valid, self.address_latch] + \
		[self.starting_address]

	def elaborate(self, platform):

		m = Module()

		with m.FSM() as fsm:
			with m.State("IDLE"):
				m.d.sync += [
					self.address_o.eq(self.starting_address),
					self.address_valid.eq(1),
				]
				# start loop?
				with m.If(self.address_latch):
					m.d.sync += self.address_o.eq(self.address_o + self.address_shift)
					m.next = "LOOP"

			with m.State("LOOP"):
				# normal process
				with m.If(self.address_latch):
					m.d.sync += self.address_o.eq(self.address_o + self.address_shift)

		return m

if __name__ == "__main__":
	d = AddressGenerator(16)
	main(d, ports=d.ios)