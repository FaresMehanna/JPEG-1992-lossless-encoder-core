'''
--------------------
Module: merge
--------------------
Description: 
    - merge is a module that  combine the encoded values of
    several pixels into one chunk of bits.
--------------------
Input: 
    - N signals representing the encoded value for the pixel.
    - N signals representing how many bits represent encoded value.
--------------------
Output:
    - single signal representing the encoded value for all the pixels.
    - single signal representing how many bits represent encoded value
    for all the pixels.
--------------------
timing:
    - The merging done in binary tree fashion, so it take 
    O(lg(N)) to complete.
--------------------
Notes :
    - merging module is the fifth step in LJ92 pipeline.
    - The module can be used with any number of input values.
    - The module uses traveling valid signal with no handshake.
    - The module is a optional in LJ92 pipeline, only used when
    several pixels is present.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

# SingleMerger is a module to handle single merge between
# two values, it is a simple shift then OR.
class SingleMerger(Elaboratable):

	def __init__(self, width):

		self.enc_in1 = Signal(width)
		self.enc_in_ctr1 = Signal(max=width+1)

		self.enc_in2 = Signal(width)
		self.enc_in_ctr2 = Signal(max=width+1)

		self.enc_out = Signal(width*2)
		self.enc_out_ctr = Signal(max=width*2+1)

		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		#end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.ios = \
			[self.enc_in1, self.enc_in_ctr1] + \
			[self.enc_in2, self.enc_in_ctr2] + \
			[self.enc_out, self.enc_out_ctr] + \
			[self.valid_in, self.valid_out] + \
			[self.end_in, self.end_out]


	def elaborate(self, platform):

		m = Module()

		with m.If(self.valid_in):
			m.d.sync += [
				self.enc_out_ctr.eq(self.enc_in_ctr1 + self.enc_in_ctr2),
				self.enc_out.eq((self.enc_in1 << self.enc_in_ctr2) | (self.enc_in2)),
			]
			
		# valid
		m.d.sync += self.valid_out.eq(self.valid_in)

		# end
		m.d.sync += self.end_out.eq(self.end_in)

		return m

'''
         |            = 0
    |         |       = 1
  |    |   |     |    = 2
 | |  | | | |   | |   = 3
'''
# The main class that ordered the pixels in the lowest
# level and add SingleMerger in all above levels.
class Merge(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 2

		#save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']

		single_ctr = min(16+self.bd, 31)
		total_ctr = single_ctr * self.ps

		self.encs_in = Array(Signal(single_ctr, name="enc_in") for _ in range(self.ps))
		self.encs_in_ctr = Array(Signal(5, name="enc_in_ctr") for _ in range(self.ps))

		self.enc_out = Signal(total_ctr, name="enc_out")
		self.enc_out_ctr = Signal(max=total_ctr+1, name="enc_out_ctr")

		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		#end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		# set levels of merge!
		levels = ceil(log(self.ps ,2))
		self.mergers = []

		#set the base level
		elems = 2**(levels-1)
		merger_width = single_ctr
		for i in range(elems):
			#create single merger for each two pixels
			self.mergers.append(SingleMerger(merger_width))

		#set all the above loops
		while elems != 1:
			elems = int(elems / 2)
			merger_width = merger_width * 2
			for j in range(elems):
				#create single merger for each two mergers
				self.mergers.append(SingleMerger(merger_width))

		self.ios = \
			[enc_in_ctr for enc_in_ctr in self.encs_in_ctr] + \
			[enc_in for enc_in in self.encs_in] + \
			[self.enc_out, self.enc_out_ctr] + \
			[self.valid_in, self.valid_out] + \
			[self.end_in, self.end_out]


	def elaborate(self, platform):

		m = Module()

		m.submodules += self.mergers

		# connect the base level
		levels = ceil(log(self.ps ,2))
		elems = 2**(levels-1)

		in_ctr = 0
		for i in range(elems):
			# connect pixels with mergers,
			# if number of pixels is not power of two, a zero
			# value is added to represent a null value.
			if in_ctr < self.ps:
				m.d.comb += [
					self.mergers[i].enc_in1.eq(self.encs_in[in_ctr]),
					self.mergers[i].enc_in_ctr1.eq(self.encs_in_ctr[in_ctr]),
					self.mergers[i].valid_in.eq(self.valid_in),
					self.mergers[i].end_in.eq(self.end_in),
				]
				in_ctr += 1
				if in_ctr < self.ps:
					m.d.comb += [
						self.mergers[i].enc_in2.eq(self.encs_in[in_ctr]),
						self.mergers[i].enc_in_ctr2.eq(self.encs_in_ctr[in_ctr]),
					]
					in_ctr += 1
				else:
					m.d.comb += [
						self.mergers[i].enc_in2.eq(0),
						self.mergers[i].enc_in_ctr2.eq(0),
					]
			# connect two mergers with each other
			else:
				m.d.comb += [
					self.mergers[i].enc_in1.eq(0),
					self.mergers[i].enc_in_ctr1.eq(0),
					self.mergers[i].enc_in2.eq(0),
					self.mergers[i].enc_in_ctr2.eq(0),
					self.mergers[i].valid_in.eq(self.valid_in),
					self.mergers[i].end_in.eq(self.end_in),
				]

		high_ctr = elems
		low_ctr = 0
		# connect all other levels
		while elems != 1:
			elems = int(elems / 2)
			for j in range(elems):
				m.d.comb += [
					self.mergers[high_ctr].enc_in1.eq(self.mergers[low_ctr].enc_out),
					self.mergers[high_ctr].enc_in_ctr1.eq(self.mergers[low_ctr].enc_out_ctr),
					self.mergers[high_ctr].enc_in2.eq(self.mergers[low_ctr+1].enc_out),
					self.mergers[high_ctr].enc_in_ctr2.eq(self.mergers[low_ctr+1].enc_out_ctr),
					self.mergers[high_ctr].valid_in.eq(self.mergers[low_ctr].valid_out),
					self.mergers[high_ctr].end_in.eq(self.mergers[low_ctr].end_out),
				]
				low_ctr += 2
				high_ctr += 1

		# top merger with main
		m.d.comb += [
			self.enc_out.eq(self.mergers[-1].enc_out),
			self.enc_out_ctr.eq(self.mergers[-1].enc_out_ctr),
			self.valid_out.eq(self.mergers[-1].valid_out),
			self.end_out.eq(self.mergers[-1].end_out),
		]

		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
	}
	m = Merge(config, constraints.Constraints())
	main(m, ports=m.ios)