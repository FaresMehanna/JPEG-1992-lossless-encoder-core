'''
--------------------
Module: reverser
--------------------
Description: 
    - reverser is a module to reverse a signal bits order,
    it can be configured to be comp or sync.
--------------------
Input: 
    - N-bits signal.
--------------------
Output:
    - reversed N-bits signal.
--------------------
timing:
    - 0 or 1 cycle depending on the configuration.
--------------------
Notes :
    - this module can be configured as combinatorial or 
    sync.
    - this module not currently used.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

class Reverser(Elaboratable):

	def __init__(self, num_bits, sync):

		#constants
		self.num_bits = num_bits
		self.sync = sync

		#data signals
		self.data_in = Signal(num_bits)
		self.data_out = Signal(num_bits)

		self.ios = \
		[self.data_out, self.data_in]

	def elaborate(self, platform):
		m = Module()

		for i in range(self.num_bits):
			if self.sync == True:
				m.d.sync += self.data_out[self.num_bits-1-i].eq(self.data_in[i])
			else:
				m.d.comb += self.data_out[self.num_bits-1-i].eq(self.data_in[i])
		return m

if __name__ == "__main__":
	n = Reverser(32, sync=False)
	main(n, ports=n.ios)