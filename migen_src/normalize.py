'''
--------------------
Module: normalize
--------------------
Description: 
    - Normalize is a module do a negative normalization 
    functionality for the inputted difference between the predicted
    values and the actual values. the normalization is done as
    LJ92 standard, also the module will output the ssss classes for
    every pixel.
--------------------
Input: 
    - N signals representing the difference between actual and
    predicted pixels.
    - N signals representing the difference between actual and
    predicted pixels minus one.
--------------------
Output:
    - N signals representing the ssss class of the every pixel.
    - N signals representing the pixel value within its ssss class.
--------------------
timing:
    - The normalization always calculated within the same
    cycle to be available in the next rising edge.
--------------------
Notes :
    - Normalization module is the third step in LJ92 pipeline.
    - The input values are assumed to be represented in 2's
     complement.
    - The module can be used with any number of input values.
    - The module uses traveling valid signal with no handshake.
    - The module is a MUST in LJ92 pipeline.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

# build_neg_tree is a function to do normalization on negative 
# values, It utilize the minus one values to normalize the
# pixels, it also do that in a binary tree fashion to shorten
# the net delay in fpga place and route.
# so for 16 bit depth, there will be 4 O(lg(N)) comparisons 
# in the worst case instead of 15 O(N) comparisons.
def build_neg_tree(m, val_in_mns, val_in, val_out, ssss, options, start, end):

	TEST_VALUE = 0
	SSSS = 1
	ADDED_VALUE = 2
	INDICES = 3

	if end == start:
		# print("SINGLE: " + str(start))
		m.d.sync += [
			val_out.eq(val_in + options[start][ADDED_VALUE]),
			ssss.eq(options[start][SSSS]),
		]

	elif end == start+1:
		# print("DOUBLE: " + str(start) + ", " + str(end))

		with m.If(val_in_mns[options[start][INDICES][0]: options[start][INDICES][1]] == options[start][TEST_VALUE]):
			m.d.sync += [
				val_out.eq(val_in + options[start][ADDED_VALUE]),
				ssss.eq(options[start][SSSS]),
			]
		with m.Else():
			m.d.sync += [
				val_out.eq(val_in + options[end][ADDED_VALUE]),
				ssss.eq(options[end][SSSS]),
			]

	else:
		# print("RECURSE: " + str(start) + ", " + str(end) + ", " + str(int((end+start)/2)))

		middle = int((end+start)/2)

		with m.If(val_in_mns[options[middle][INDICES][0]: options[middle][INDICES][1]] == options[middle][TEST_VALUE]):
			build_neg_tree(m, val_in_mns, val_in, val_out, ssss, options, start, middle)
		with m.Else():
			build_neg_tree(m, val_in_mns, val_in, val_out, ssss, options, middle+1, end)

# build_pos_tree is function to normalize the positive values,
# in reality it only calculate the ssss class since the values
# are already positive, since it does that by one bit checking
# , no need to build a tree, also building a tree for it is
# harder than build_neg_tree.
def build_pos_tree(m, val_in, ssss, options, start, end):

	INDEX = 0
	SSSS = 1

	with m.If(val_in[options[0][INDEX]]):
		m.d.sync += ssss.eq(options[0][SSSS])
	for i in range(1, len(options)):
		with m.Elif(val_in[options[i][INDEX]]):
			m.d.sync += ssss.eq(options[i][SSSS])


# The SingleNormalizer can do a normalization for a 
# single pixel only, for every pixel a new class is 
# implemented in the final design.
class SingleNormalizer(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		#save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']

		# difference value - in
		self.val_in = Signal(self.bd+1)
		# difference value-1 - in
		self.val_in_mns = Signal(self.bd+1)

		# normalized value - out
		self.val_out = Signal(self.bd)
		# ssss class - out
		self.ssss = Signal(5)

		self.valid = Signal(1)
		self.valid_o = Signal(1)

		#end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.ios = \
			[self.val_in, self.val_out, self.ssss, self.valid, self.valid_o, self.val_in_mns] + \
			[self.end_in, self.end_out]

	def elaborate(self, platform):

		m = Module()
		
		# values dependant on the bit depth of LJ92 to 
		# help build the tree, it represent the boundaries
		# for every ssss class and added value for every class.
		neg_options = []
		for i in range(self.bd):
			neg_options.append(((2**(self.bd-i)-1), i+1, (2**(i+1)) - 1, (1+i, self.bd+1)))
		pos_options = []
		for i in range(self.bd):
			pos_options.append((self.bd-1-i, self.bd-i))

		# if valid data
		with m.If(self.valid):
			# if negative
			with m.If(self.val_in[self.bd] == 1):
				# normalize the negative values to positive one
				# and calculate the ssss class of the input.
				build_neg_tree(m, self.val_in_mns, self.val_in, self.val_out, self.ssss, neg_options, 0, self.bd-1)
			# if positive
			with m.Else():
				# output the same input.
				# self.ssss.eq(0) is only a default and it may
				# be overwritten by build_pos_tree logic.
				m.d.sync += [
					self.val_out.eq(self.val_in),
					self.ssss.eq(0),
				]
				# overwrite ssss class if needed
				build_pos_tree(m, self.val_in, self.ssss, pos_options, 0, self.bd-1)

		# valid signal
		m.d.sync += self.valid_o.eq(self.valid)

		# end
		m.d.sync += self.end_out.eq(self.end_in)

		return m


class Normalize(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		#save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']

		# difference values - in
		self.vals_in = Array(Signal(self.bd+1, name="val_in") for _ in range(self.ps))
		# difference values-1 - in
		self.vals_in_mns = Array(Signal(self.bd+1, name="vals_in_mns") for _ in range(self.ps))

		# normalized values - out
		self.vals_out = Array(Signal(self.bd, name="val_out") for _ in range(self.ps))
		# ssss classes - out
		self.ssssx = Array(Signal(5, name="ssss") for _ in range(self.ps))

		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		#end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.pixels = [SingleNormalizer(config, constraints) for _ in range(self.ps)]

		self.ios = \
			[val_in_mns for val_in_mns in self.vals_in_mns] + \
			[val_out for val_out in self.vals_out] + \
			[val_in for val_in in self.vals_in] + \
			[self.valid_in, self.valid_out] + \
			[ssss for ssss in self.ssssx] + \
			[self.end_in, self.end_out]



	def elaborate(self, platform):

		m = Module()
		m.submodules += self.pixels

		# This loop will initiate number of SingleNormalizer-s for every pixel.
		for pixel, val_in, val_out, ssss, val_in_mns in zip(self.pixels, self.vals_in, self.vals_out, self.ssssx, self.vals_in_mns):
			m.d.comb += [
				pixel.val_in.eq(val_in),
				pixel.valid.eq(self.valid_in),
				pixel.end_in.eq(self.end_in),
				pixel.val_in_mns.eq(val_in_mns),
			]
			m.d.comb += [
				ssss.eq(pixel.ssss),
				val_out.eq(pixel.val_out),
			]

		#if valid data
		m.d.comb += self.valid_out.eq(self.pixels[0].valid_o)

		# end
		m.d.comb += self.end_out.eq(self.pixels[0].end_out)

		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 1,
	}
	n = Normalize(config, constraints.Constraints())
	main(n, ports=n.ios)