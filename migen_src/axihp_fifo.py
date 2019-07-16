from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from nmigen.lib.fifo import SyncFIFO

class AxiHPFifo(Elaboratable):

	def __init__(self):

		self.data_in = Signal(64)
		self.data_out = Signal(64)

		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.read = Signal(1)

		self.writable = Signal(1)
		self.readable = Signal(1)

		self.writable16 = Signal(1)
		self.readable16 = Signal(1)

		self.ios = \
			[self.data_in, self.data_out] + \
			[self.end_in, self.end_out] + \
			[self.valid_in, self.valid_out] + \
			[self.writable, self.readable] + \
			[self.writable16, self.readable16] + \
			[self.read]

		self.fifo = SyncFIFO(65, 32)

	def elaborate(self, platform):

		m = Module()

		m.submodules.fifo = fifo = self.fifo

		# fifo in
		m.d.comb += [
			fifo.we.eq(self.valid_in),
			fifo.din.eq(Cat(self.end_in, self.data_in)),
			fifo.re.eq(self.read),
		]

		# writable & readable
		m.d.comb += [
			self.writable.eq(fifo.writable),
			self.readable.eq(fifo.readable),
			self.readable16.eq(fifo.level >= 16),
			self.writable16.eq(fifo.level <= 12),
		]

		# data out
		m.d.comb += [
			self.data_out.eq(fifo.dout[1:65]),
			self.end_out.eq(fifo.dout[0]),
			self.valid_out.eq(fifo.readable),
		]

		return m

if __name__ == "__main__":
	d = AxiHPFifo()
	main(d, ports=d.ios)