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

		data_top = 0
		steps = 0
		while data_top + self.conv_bits <= self.total_ctr:
			data_top += self.conv_bits
			steps += 1

		enc_out_latch = Signal(data_top)
		out_end_latch = Signal(1)

		# register prev data
		enc_out_reg = Signal(self.total_ctr)
		enc_out_ctr_reg = Signal(max=self.total_ctr+1)
		out_end_reg = Signal(1)
		valid_out_reg = Signal(1)

		def reg_data():
			m.d.sync += [
				enc_out_reg.eq(self.enc_out),
				enc_out_ctr_reg.eq(self.enc_out_ctr),
				out_end_reg.eq(self.out_end),
				valid_out_reg.eq(self.valid_out),
			]

		with m.FSM() as outTransaction:

			with m.State("IDLE"):

				m.d.sync += [
					self.valid_in.eq(0),
					self.latch_output.eq(0),
				]

				#if there is input in the buffer & can write it
				with m.If(valid_out_reg & (self.close_full==0)):
					# latch the input
					m.d.sync += [
						self.latch_output.eq(1),
					]
					m.next = "BRUST"

				# if there is new input & can write it
				with m.Elif(self.valid_out & (self.close_full==0)):
					# latch the input
					m.d.sync += [
						self.latch_output.eq(1),
					]
					m.next = "BRUST_IDLE"

			with m.State("BRUST_IDLE"):
				reg_data()
				m.next = "BRUST"

			with m.State("BRUST"):
				reg_data()
				with m.If(valid_out_reg):
					#if all input can fill
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

						start = 0
						end = self.conv_bits
						state = "STEPS_"
						for i in range(steps):
							start += self.conv_bits	#36 72 108 $64
							end = min(end + self.conv_bits, self.total_ctr) # 72 108 144->124 $128->112
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

			# the rest of state
			state = "STEPS"
			start = 0
			end = self.conv_bits
			for i in range(steps):
				with m.State("STEPS_"+str(i)):
					m.d.sync += [
						self.enc_in.eq(enc_out_latch[start:end]),
						self.enc_in_ctr.eq(self.conv_bits),
						self.in_end.eq(out_end_latch),
						self.valid_in.eq(1),
					]
					if i == 0:
						m.next = "IDLE"
					else:
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