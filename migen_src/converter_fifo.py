from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from nmigen.lib.fifo import SyncFIFOBuffered
from math import log, ceil
from constants import *

DATA_WIDTH = 48
CTR_BITS = 6
DATA_CTR = DATA_WIDTH + CTR_BITS

class ConverterFifo(Elaboratable):

	def __init__(self, depth):

		self.depth = depth

		self.enc_in = Signal(DATA_WIDTH)
		self.enc_in_ctr = Signal(CTR_BITS)
		self.in_end = Signal(1)
		self.valid_in = Signal(1)
		self.writable = Signal(1)
		self.close_full = Signal(1)


		self.latch_output = Signal(1)
		self.enc_out = Signal(DATA_WIDTH)
		self.enc_out_ctr = Signal(CTR_BITS)
		self.out_end = Signal(1)
		self.valid_out = Signal(1)

		self.ios = \
			[self.enc_in, self.enc_in_ctr, self.in_end, self.valid_in] + \
			[self.enc_out, self.enc_out_ctr, self.out_end, self.valid_out] + \
			[self.latch_output, self.writable, self.close_full]

		self.fifo = SyncFIFOBuffered(DATA_CTR+1, depth)

	def elaborate(self, platform):

		m = Module()

		m.submodules.fifo = fifo = self.fifo

		# lj92 pipeline with fifo
		m.d.comb += [
			fifo.we.eq(self.valid_in),
			fifo.din.eq(Cat(self.enc_in, self.enc_in_ctr, self.in_end)),
		]

		m.d.comb += [
			self.writable.eq(fifo.writable),
			self.valid_out.eq(fifo.readable),
			self.enc_out.eq(fifo.dout[0:DATA_WIDTH]),
			self.enc_out_ctr.eq(fifo.dout[DATA_WIDTH:DATA_CTR]),
			self.out_end.eq(fifo.dout[DATA_CTR:DATA_CTR+1]),
			fifo.re.eq(self.latch_output),
		]

		# fifo with close_full
		m.d.sync += [
			self.close_full.eq(fifo.level > (self.depth-10)),
		]

		return m

if __name__ == "__main__":
	d = ConverterFifo(128)
	main(d, ports=d.ios)