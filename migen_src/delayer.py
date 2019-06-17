from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

class Delayer(Elaboratable):

	def __init__(self, delay_stages):

		self.in_sig = Signal(1)
		self.out_sig = Signal(1)
		self.timer = Signal(ceil(log(delay_stages, 2.0)), reset=delay_stages-2)

		self.ios = [self.in_sig, self.out_sig]

	def elaborate(self, platform):

		timer_start = Signal(1)
		out_val = Signal(1)

		m = Module()
		
		with m.If(self.in_sig):
			m.d.sync += timer_start.eq(1)

		with m.If(timer_start):
			m.d.sync += self.timer.eq(self.timer - 1)
		
		m.d.sync += out_val.eq((self.timer == 0)| out_val)
		m.d.comb += self.out_sig.eq(out_val)

		return m

if __name__ == "__main__":
	d = Delayer(8)
	main(d, ports=d.ios)