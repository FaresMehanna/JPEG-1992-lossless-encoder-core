from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class PipelineReg(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		#save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']
		self.active_reg = config['pipeline_reg']

		single_ctr = min(16+self.bd, 31)
		total_ctr = single_ctr * self.ps

		# pipeline ending
		self.enc_left = Signal(total_ctr)
		self.enc_left_ctr = Signal(max=total_ctr+1)

		# fifo starting
		self.enc_right = Signal(total_ctr)
		self.enc_right_ctr = Signal(max=total_ctr+1)

		self.valid_left = Signal(1)
		self.valid_right = Signal(1)

		self.ios = \
		[self.enc_left, self.enc_left_ctr, self.valid_left] + \
		[self.enc_right, self.enc_right_ctr, self.valid_right]

	def elaborate(self, platform):

		m = Module()

		if self.active_reg:
			m.d.sync += [
				self.enc_right.eq(self.enc_left),
				self.enc_right_ctr.eq(self.enc_left_ctr),
				self.valid_right.eq(self.valid_left),
			]
		else:
			m.d.comb += [
				self.enc_right.eq(self.enc_left),
				self.enc_right_ctr.eq(self.enc_left_ctr),
				self.valid_right.eq(self.valid_left),
			]
		return m


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
		"pipeline_reg": True,
	}
	d = PipelineReg(config, constraints.Constraints())
	main(d, ports=d.ios)