'''
--------------------
Module: converter_fifo
--------------------
Description: 
    - converter_fifo is a fifo enclosure using BRAM, that
    sit between the converter and the rest of the logic.
--------------------
Input: 
    - single signal representing the encoded value for all the pixels.
    - single signal representing how many bits represent encoded value
    for all the pixels.
--------------------
Output:
    - single signal representing the encoded value for all the pixels.
    - single signal representing how many bits represent encoded value
    for all the pixels.
--------------------
timing:
    - This is a fifo based on BRAM, so there is one cycle latency.
--------------------
Notes :
    - converter_fifo module is placed after the converter module
    - The module is a optional in LJ92 pipeline, but it is a must
    if the converter module is used.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from nmigen.lib.fifo import SyncFIFOBuffered
from math import log, ceil
import constraints

class ConverterFifo(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['converter'] >= 1
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1
		#how many steps in converter
		single_ctr = min(16 + config['bit_depth'], 31)
		total_ctr = single_ctr * config['pixels_per_cycle']
		self.steps = ceil(total_ctr / config['converter']) + 3
		assert config['converter_fifo_depth'] > (self.steps + 3)

		#save some data
		self.data_width = config['converter']
		self.ctr_bits = ceil(log(config['converter']+1, 2))
		self.total_bits = self.data_width + self.ctr_bits + 1
		self.depth = config['converter_fifo_depth']

		self.enc_in = Signal(self.data_width)
		self.enc_in_ctr = Signal(self.ctr_bits)
		self.in_end = Signal(1)
		self.valid_in = Signal(1)
		self.writable = Signal(1)
		self.close_full = Signal(1)


		self.latch_output = Signal(1)
		self.enc_out = Signal(self.data_width)
		self.enc_out_ctr = Signal(self.ctr_bits)
		self.out_end = Signal(1)
		self.valid_out = Signal(1)

		self.ios = \
			[self.enc_in, self.enc_in_ctr, self.in_end, self.valid_in] + \
			[self.enc_out, self.enc_out_ctr, self.out_end, self.valid_out] + \
			[self.latch_output, self.writable, self.close_full]

		self.fifo = SyncFIFOBuffered(self.total_bits, self.depth)

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
			self.enc_out.eq(fifo.dout[0:self.data_width]),
			self.enc_out_ctr.eq(fifo.dout[self.data_width:self.total_bits-1]),
			self.out_end.eq(fifo.dout[self.total_bits-1:self.total_bits]),
			fifo.re.eq(self.latch_output),
		]

		# fifo with close_full
		m.d.sync += [
			self.close_full.eq(fifo.level >= (self.depth-self.steps)),
		]

		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
		"converter": 36,
		"converter_fifo_depth": 128,
	}
	d = ConverterFifo(config, constraints.Constraints())
	main(d, ports=d.ios)