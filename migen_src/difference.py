from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class Difference(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		#save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']

		#no update in constraints

		self.pixels_in = Array(Signal(self.bd, name="pixel_in") for _ in range(self.ps))
		self.predics_in = Array(Signal(self.bd, name="predic_in") for _ in range(self.ps))
		self.vals_out = Array(Signal(self.bd+1, name="val_out") for _ in range(self.ps))
		self.vals_out_mns = Array(Signal(self.bd+1, name="val_out") for _ in range(self.ps))
		
		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		#end in & out
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