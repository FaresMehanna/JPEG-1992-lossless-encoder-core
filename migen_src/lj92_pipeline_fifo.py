from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from nmigen.lib.fifo import SyncFIFOBuffered
from math import log, ceil
import constraints

class LJ92PipelineFifo(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1
		assert config['LJ92_fifo_depth'] >= 25

		#data width
		single_data_bits = min(16+config['bit_depth'], 31)
		self.data_bits = single_data_bits*config['pixels_per_cycle']
		self.ctr_bits = ceil(log(self.data_bits+1, 2))
		self.total_width = self.data_bits + self.ctr_bits + 1

		self.depth = config['LJ92_fifo_depth']

		# lj92 pipeline ports
		self.enc_in = Signal(self.data_bits)
		self.enc_in_ctr = Signal(max=self.data_bits+1)
		self.in_end = Signal(1)
		self.valid_in = Signal(1)

		self.latch_output = Signal(1)
		self.enc_out = Signal(self.data_bits)
		self.enc_out_ctr = Signal(max=self.data_bits+1)
		self.out_end = Signal(1)
		self.valid_out = Signal(1)

		# port to indicate it is full and no more
		# input should be inserted in the lj92 pipeline
		self.close_full = Signal(1)

		self.ios = \
			[self.enc_in, self.enc_in_ctr, self.in_end, self.valid_in] + \
			[self.enc_out, self.enc_out_ctr, self.out_end, self.valid_out] + \
			[self.latch_output, self.close_full]

		# 4x dual port bram with 36kb each.
		self.fifo = SyncFIFOBuffered(self.total_width, self.depth)

	def elaborate(self, platform):

		m = Module()

		m.submodules.fifo = fifo = self.fifo

		# lj92 pipeline with fifo
		m.d.comb += [
			fifo.we.eq(self.valid_in),
			fifo.din.eq(Cat(self.enc_in, self.enc_in_ctr, self.in_end)),
		]

		m.d.comb += [
			self.valid_out.eq(fifo.readable),
			self.enc_out.eq(fifo.dout[0:self.data_bits]),
			self.enc_out_ctr.eq(fifo.dout[self.data_bits:self.total_width-1]),
			self.out_end.eq(fifo.dout[self.total_width-1:self.total_width]),
			fifo.re.eq(self.latch_output),
		]

		# fifo with close_full
		m.d.sync += [
			self.close_full.eq(fifo.level >= (self.depth-10)),
		]

		return m


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
		"LJ92_fifo_depth": 128,
	}
	d = LJ92PipelineFifo(config, constraints.Constraints())
	main(d, ports=d.ios)