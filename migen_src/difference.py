'''
--------------------
Module: difference
--------------------
Description: 
    - Difference is a module implements a difference 
    functionality for the inputted pixels and the predicted
    values for them. It simply subtract them as the subtraction
    values will be used later for encoding.
--------------------
Input: 
    - N pixels signals.
    - N predicted signals.
--------------------
Output:
    - N signals representing the subtracted values.
    - N signals representing the subtracted values minus one, this
    is needed for the normalizer step.
--------------------
timing:
    - The subtraction always calculated within the same
    cycle to be available in the next rising edge.
--------------------
Notes :
    - Difference module is the second step in LJ92 pipeline.
    - The "minus one" values are only present as these are needed
    in the normalization step.
    - The module can only be used with any number of input pixels.
    - The module uses traveling valid signal with no handshake.
    - The module is a MUST in LJ92 pipeline.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class Difference(Elaboratable):

	def __init__(self, config, constraints):

		# config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		# save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']

		# no update in constraints

		# the actual pixels value - in
		self.pixels_in = Array(Signal(self.bd, name="pixel_in") for _ in range(self.ps))

		# the predicted pixels value - in
		self.predics_in = Array(Signal(self.bd, name="predic_in") for _ in range(self.ps))

		# the subtracted values - out
		self.vals_out = Array(Signal(self.bd+1, name="val_out") for _ in range(self.ps))

		# the subtracted values minus 1 - out
		self.vals_out_mns = Array(Signal(self.bd+1, name="val_out") for _ in range(self.ps))
		
		# valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		# end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.ios = \
			[val_out_mns for val_out_mns in self.vals_out_mns] + \
			[predic_in for predic_in in self.predics_in] + \
			[pixel_in for pixel_in in self.pixels_in] + \
			[val_out for val_out in self.vals_out] + \
			[self.valid_in, self.valid_out] + \
			[self.end_in, self.end_out]


	def elaborate(self, platform):

		m = Module()

		#if valid data
		with m.If(self.valid_in):
			m.d.sync += [val_out.eq(pixel_in-predic_in) for val_out, pixel_in, predic_in in zip(self.vals_out, self.pixels_in, self.predics_in)]
			m.d.sync += [val_out_mns.eq(pixel_in-predic_in-1) for val_out_mns, pixel_in, predic_in in zip(self.vals_out_mns, self.pixels_in, self.predics_in)]

		#if valid data
		m.d.sync += self.valid_out.eq(self.valid_in)

		# end
		m.d.sync += self.end_out.eq(self.end_in)
		
		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
	}
	d = Difference(config, constraints.Constraints())
	main(d, ports=d.ios)