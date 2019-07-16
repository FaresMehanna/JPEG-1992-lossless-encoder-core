'''
--------------------
Module: converter
--------------------
Description: 
    - converter is a module introduced as an optimization step in
    the core, since the output of LJ92 pipeline is variable in number of
    bits, it is not very friendly to build the rest of the core
    on the worst case possible, so a converter module is introduced
    to lower the worst case to a more sensible one by dividing
    the big chunks of data into several smaller ones, also it
    should be noted that most of the chunks are already small in size,
    so this will divide very small amount of chunks.
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
    - one cycle or more depending on the size of the input.
--------------------
Notes :
    - converter implementation assume that it read and write to
    fifo modules.
    - The module is optional step made as an optimization step.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class Converter(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1
		assert config['converter'] >= 1
		single_ctr = min(16+config['bit_depth'], 31)
		self.total_ctr = total_ctr = single_ctr*config['pixels_per_cycle']
		assert config['converter'] <= total_ctr

		#save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']
		self.conv_bits = config['converter']

		# left fifo
		self.latch_output = Signal(1)
		self.enc_out = Signal(total_ctr)
		self.enc_out_ctr = Signal(max=total_ctr+1)
		self.out_end = Signal(1)
		self.valid_out = Signal(1)

		# right fifo
		self.enc_in = Signal(self.conv_bits)
		self.enc_in_ctr = Signal(max=self.conv_bits+1)
		self.in_end = Signal(1)
		self.valid_in = Signal(1)
		self.close_full = Signal(1)

		self.ios = [self.latch_output, self.enc_out, self.enc_out_ctr] + \
		[self.out_end, self.valid_out, self.enc_in, self.enc_in_ctr, self.in_end] + \
		[self.valid_in, self.close_full]


	def elaborate(self, platform):

		m = Module()

		# based on the size of the input and the size of the
		# output, calculate the max number of steps and the
		# number of bits needed to be cached.
		data_top = 0
		steps = 0
		while data_top + self.conv_bits <= self.total_ctr:
			data_top += self.conv_bits
			steps += 1

		enc_out_latch = Signal(data_top)
		out_end_latch = Signal(1)

		# register inputted data to allow for faster MHz
		enc_out_reg = Signal(self.total_ctr)
		enc_out_ctr_reg = Signal(max=self.total_ctr+1)
		out_end_reg = Signal(1)
		valid_out_reg = Signal(1)

		# function that will be used in any place to 
		# register the inputted data
		def reg_data():
			m.d.sync += [
				enc_out_reg.eq(self.enc_out),
				enc_out_ctr_reg.eq(self.enc_out_ctr),
				out_end_reg.eq(self.out_end),
				valid_out_reg.eq(self.valid_out),
			]

		# function that will try to go to BURST mode,
		# it may be used in IDLE state or any other state.
		def try_burst_idle():
			#if there is input in the buffer & can write it
			with m.If(valid_out_reg & (self.close_full==0)):
				# latch the input
				m.d.sync += [
					self.latch_output.eq(1),
				]
				m.next = "BURST"

			# if there is new input & can write it
			with m.Elif(self.valid_out & (self.close_full==0)):
				# latch the input
				m.d.sync += [
					self.latch_output.eq(1),
				]
				m.next = "BURST_PREPARE"

			#else stay/goto IDLE
			with m.Else():
				m.next = "IDLE"

		# finite state machine that implement the converter
		# logic.
		with m.FSM() as outTransaction:

			with m.State("IDLE"):

				m.d.sync += [
					self.valid_in.eq(0),
					self.latch_output.eq(0),
				]

				#this may overwrite self.latch_output
				try_burst_idle()

			with m.State("BURST_PREPARE"):
				reg_data()
				m.d.sync += self.valid_in.eq(0)
				m.next = "BURST"

			# most of the time it should be here in "BRUST"
			# state and go only to "STEPS_X" when the inputted
			# data is big.
			with m.State("BURST"):
				reg_data()
				with m.If(valid_out_reg):
					#if all input can fill the output
					with m.If(enc_out_ctr_reg <= self.conv_bits):
						m.d.sync += [
							self.enc_in.eq(enc_out_reg),
							self.enc_in_ctr.eq(enc_out_ctr_reg),
							self.in_end.eq(out_end_reg),
							self.valid_in.eq(1),
						]
						with m.If(self.close_full):
							m.d.sync += [
								self.latch_output.eq(0),
							]
							m.next = "IDLE"
					# if inputted data is bigger than the converter
					with m.Else():
						#latch only the first part of the input
						m.d.sync += [
							self.enc_in_ctr.eq(self.conv_bits),
							self.in_end.eq(0),
							self.valid_in.eq(1),
							self.latch_output.eq(0),
							#latch current input
							enc_out_latch.eq(enc_out_reg[0:data_top]),
							out_end_latch.eq(out_end_reg),
						]

						# depends on the size of the input data it
						# will move to suitable "STEPS_X" state.
						start = 0
						end = self.conv_bits
						state = "STEPS_"
						for i in range(steps):
							start += self.conv_bits	#30
							end = min(end + self.conv_bits, self.total_ctr) #56
							if i == 0:
								with m.If(enc_out_ctr_reg <= end):
									m.d.sync += [
										self.enc_in.eq(enc_out_reg[start:end]),
										self.enc_in_ctr.eq(enc_out_ctr_reg - start),
									]
									m.next = state + str(i)
							else:
								with m.Elif(enc_out_ctr_reg <= end):
									m.d.sync += [
										self.enc_in.eq(enc_out_reg[start:end]),
										self.enc_in_ctr.eq(enc_out_ctr_reg - start),
									]
									m.next = state + str(i)
				with m.Else():
					m.d.sync += self.valid_in.eq(0)

			# the rest of states.
			# every state handle part of the data and
			# move to the next one.
			state = "STEPS"
			start = 0
			end = self.conv_bits
			for i in range(steps):
				with m.State("STEPS_"+str(i)):
					m.d.sync += [
						self.enc_in.eq(enc_out_latch[start:end]),
						self.enc_in_ctr.eq(self.conv_bits),
						self.valid_in.eq(1),
					]
					if i == 0:
						m.d.sync += self.in_end.eq(out_end_latch),
						try_burst_idle()
					else:
						m.d.sync += self.in_end.eq(0),
						m.next = "STEPS_" + str(i-1)
				start += self.conv_bits
				end += self.conv_bits

		return m


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
		"converter": 36,
	}
	d = Converter(config, constraints.Constraints())
	main(d, ports=d.ios)