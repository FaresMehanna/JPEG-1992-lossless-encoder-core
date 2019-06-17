from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class ConverterReg(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['converter'] >= 1

		#save needed configs
		self.conv_bits = config['converter']
		self.activ_reg = config['converter_reg']

		# left converter
		self.left_enc = Signal(self.conv_bits)
		self.left_enc_ctr = Signal(max=self.conv_bits+1)
		self.left_end = Signal(1)
		self.left_valid = Signal(1)
		self.left_close_full = Signal(1)

		# right fifo
		self.right_enc = Signal(self.conv_bits)
		self.right_enc_ctr = Signal(max=self.conv_bits+1)
		self.right_end = Signal(1)
		self.right_valid = Signal(1)
		self.right_close_full = Signal(1)

		self.ios = \
		[self.left_close_full, self.left_enc, self.left_enc_ctr, self.left_end, self.left_valid] + \
		[self.right_close_full, self.right_enc, self.right_enc_ctr, self.right_end, self.right_valid]

	def elaborate(self, platform):

		m = Module()

		if self.activ_reg == True:
			m.d.sync += [
				self.right_enc.eq(self.left_enc),
				self.right_enc_ctr.eq(self.left_enc_ctr),
				self.right_end.eq(self.left_end),
				self.right_valid.eq(self.left_valid),
				self.left_close_full.eq(self.right_close_full),
			]
		else:
			m.d.comb += [
				self.right_enc.eq(self.left_enc),
				self.right_enc_ctr.eq(self.left_enc_ctr),
				self.right_end.eq(self.left_end),
				self.right_valid.eq(self.left_valid),
				self.left_close_full.eq(self.right_close_full),
			]
		return m


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
		"converter": 36,
		"converter_reg": True,
	}
	d = ConverterReg(config, constraints.Constraints())
	main(d, ports=d.ios)