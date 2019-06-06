from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from nmigen.lib.fifo import SyncFIFOBuffered
from math import log, ceil
from constants import *


class LJ92PipelineFifo(Elaboratable):

	def __init__(self, depth):

		assert depth > 50

		self.depth = depth

		# lj92 pipeline ports
		self.enc_in = Signal(124)
		self.enc_in_ctr = Signal(7)
		self.in_end = Signal(1)
		self.valid_in = Signal(1)

		self.latch_output = Signal(1)
		self.enc_out = Signal(124)
		self.enc_out_ctr = Signal(7)
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
		self.fifo = SyncFIFOBuffered(7+124+1, depth)

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
			self.enc_out.eq(fifo.dout[0:124]),
			self.enc_out_ctr.eq(fifo.dout[124:131]),
			self.out_end.eq(fifo.dout[131:132]),
			fifo.re.eq(self.latch_output),
		]

		# fifo with close_full
		m.d.sync += [
			self.close_full.eq(fifo.level > (self.depth-50)),
		]

		return m


if __name__ == "__main__":
	d = LJ92PipelineFifo(128)
	main(d, ports=d.ios)