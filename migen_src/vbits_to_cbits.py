from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class OutputHandler(Elaboratable):

	def __init__(self, config, constraints):

		self.output_size = config['out_bits']
		self.input_size = config['converter']
		self.buffer_size = config['vbits_to_cbits_buffer_size']
		self.out_bytes = int(self.output_size/8)

		#output data
		self.data_out = Signal(self.output_size)
		self.valid_out = Signal(1)
		self.end_out = Signal(1)
		self.busy_in = Signal(1)

		#buffer data
		self.buffer = Signal(self.buffer_size)
		self.buff_consum = Signal(max=(self.buffer_size+1))
		self.new_buff_consum = Signal(max=(self.buffer_size+1))
		self.new_buff_consum_actv = Signal(1)
		#is read happen to the buffer?
		self.dec_buff_out = Signal(1)

		#signal for end from input handler
		self.end_in = Signal(1)


	def elaborate(self, platform):

		m = Module()

		# right & left shift to handle data output
		shift_right = Signal(max=self.buffer_size-self.output_size+1)
		shift_left = Signal(max=self.buffer_size-self.output_size+1)
		m.d.comb += shift_right.eq(self.buff_consum - self.output_size)
		m.d.comb += shift_left.eq(self.output_size - self.buff_consum)

		# initial value for dec_buff_out
		m.d.comb += self.dec_buff_out.eq(0)

		# conditions
		buff_consum_less_eq = Signal(1)
		buff_consum_greater_eq = Signal(1)

		with m.If(self.new_buff_consum_actv):
			m.d.sync += [
				buff_consum_greater_eq.eq((self.new_buff_consum >= self.output_size)),
				buff_consum_less_eq.eq((self.new_buff_consum <= self.output_size)),
			]

		def do_output():
			with m.If(buff_consum_greater_eq):
				m.d.sync += self.data_out.eq(self.buffer >> shift_right),
			with m.Else():
				m.d.sync += self.data_out.eq(self.buffer << shift_left),
			# for i in range(self.output_size):
			# 	m.d.sync += self.data_out[i].eq(self.buffer[self.output_size-i-1])

			m.d.sync += self.valid_out.eq(1),
			m.d.comb += self.dec_buff_out.eq(1)

		# activate valid signal
		with m.FSM() as outTransaction:

			with m.State("OUTPUT"):
				#if we have enough data, or end signal is activated -> last input
				with m.If((buff_consum_greater_eq) | ((buff_consum_less_eq) & self.end_in)):
					do_output()
					m.next = "BRUST"
				#added to handle end signal - if last input then sent end_out to one
				with m.If((buff_consum_less_eq) & self.end_in):
					m.d.sync += self.end_out.eq(1),

			with m.State("BRUST"):
				#device latched the prev output and new output is ready
				with m.If((self.busy_in == 0) & (buff_consum_greater_eq)):
					do_output()
				#device latched the prev output but NO new output is ready
				with m.Elif(self.busy_in == 0):
					m.d.sync += self.valid_out.eq(0),
					m.next = "OUTPUT"
				#device did not latch the prev output
				with m.Else():
					pass
				#added to handle end signal - if last input then sent end_out to one
				with m.If((buff_consum_less_eq) & self.end_in):
					m.d.sync += self.end_out.eq(1),

		return m

class InputHandler(Elaboratable):

	def __init__(self, config, constraints):

		self.output_size = config['out_bits']
		self.input_size = config['converter']
		self.buffer_size = config['vbits_to_cbits_buffer_size']

		# input port from last stage
		self.latch_input = Signal(1)
		self.enc_in = Signal(self.input_size)
		self.enc_in_ctr = Signal(max=(self.input_size+1))
		self.in_end = Signal(1)
		self.valid_in = Signal(1)

		#buffer & related info - ALL OUTPUTS
		self.buffer = Signal(self.buffer_size)
		self.buff_consum = Signal(max=(self.buffer_size+1))
		self.new_buff_consum = Signal(max=(self.buffer_size+1))
		self.new_buff_consum_actv = Signal(1)

		#signals indicating decrease in buffer - ALL INPUTS
		self.dec_buff = Signal(1)

		#signal for end
		self.end_out = Signal(1)

		self.ios = \
			[self.enc_in, self.enc_in_ctr, self.in_end, self.valid_in] + \
			[self.latch_input, self.buffer, self.buff_consum] + \
			[self.end_out, self.dec_buff]

	def elaborate(self, platform):

		m = Module()

		#signals indicating increase & decrease in buffer
		self.inc_buff = Signal(1)
		m.d.comb += self.inc_buff.eq(0)

		# to register data from fifo
		enc_in_reg = Signal(self.input_size)
		enc_in_ctr_reg = Signal(max=(self.input_size+1))
		in_end_reg = Signal(1)
		valid_in_reg = Signal(1)

		# termination condition for brust & base input
		brust_cond = Signal(1)
		normal_cond = Signal(1)

		# Default value of self.new_buff_consum_actv
		m.d.comb += self.new_buff_consum_actv.eq(0)

		def reg_data():
			m.d.sync += [
				enc_in_reg.eq(self.enc_in),
				enc_in_ctr_reg.eq(self.enc_in_ctr),
				in_end_reg.eq(self.in_end),
				valid_in_reg.eq(self.valid_in),
			]

		def get_input():
			m.d.sync += [
				self.buffer.eq((self.buffer << enc_in_ctr_reg) | enc_in_reg),
				self.end_out.eq(in_end_reg),
			]
			# m.d.sync += [
			# 	self.buffer.eq((self.buffer >> self.output_size) | (enc_in_reg << self.buff_consum)),
			# 	self.end_out.eq(self.in_end),
			# ]
			m.d.comb += self.inc_buff.eq(1)

		with m.FSM() as inTransaction:

			with m.State("INPUT"):
				with m.If(normal_cond):
					#if we have data in buffer
					with m.If(valid_in_reg):
						m.d.sync += self.latch_input.eq(1)
						m.next = "BRUST"
					#if we have new data
					with m.Elif(self.valid_in):
						m.d.sync += self.latch_input.eq(1)
						m.next = "DELAY_BRUST"

			with m.State("DELAY_BRUST"):
				reg_data()
				m.next = "BRUST"

			with m.State("BRUST"):
				#if we have new data
				reg_data()
				with m.If(valid_in_reg):
					get_input()
					with m.If(((self.buff_consum + enc_in_ctr_reg) <= (self.buffer_size-self.input_size))):
						m.d.sync += self.latch_input.eq(1)
					with m.Else():
						m.d.sync += self.latch_input.eq(0)
						m.next = "INPUT"

		with m.If(self.inc_buff & self.dec_buff):
			m.d.comb += self.new_buff_consum.eq(self.buff_consum - self.output_size + enc_in_ctr_reg)
		with m.Elif(self.dec_buff):
			m.d.comb += self.new_buff_consum.eq(self.buff_consum - self.output_size)
		with m.Elif(self.inc_buff):
			m.d.comb += self.new_buff_consum.eq(self.buff_consum + enc_in_ctr_reg)

		with m.If(self.inc_buff | self.dec_buff):
			m.d.sync += self.buff_consum.eq(self.new_buff_consum)
			m.d.comb += self.new_buff_consum_actv.eq(1)

		m.d.sync += normal_cond.eq(self.new_buff_consum <= (self.buffer_size-self.input_size))

		# with m.If(self.valid_in & (self.inc_buff | self.dec_buff)):
			# m.d.sync += brust_cond.eq(((self.new_buff_consum + self.enc_in_ctr) <= (self.buffer_size-self.input_size)))

		return m

class VBitsToCBits(Elaboratable):

	def __init__(self, config, constraints):

		assert config['vbits_to_cbits_buffer_size'] >= (config['converter']+config['out_bits'])
		assert config['out_bits']%8 == 0

		self.output_size = config['out_bits']
		self.input_size = config['converter']
		self.buffer_size = config['vbits_to_cbits_buffer_size']
		self.out_bytes = int(self.output_size/8)

		self.latch_input = Signal(1)
		self.enc_in = Signal(self.input_size)
		self.enc_in_ctr = Signal(max=(self.input_size+1))
		self.in_end = Signal(1)
		self.valid_in = Signal(1)

		self.data_out = Signal(self.output_size)
		self.valid_out = Signal(1)
		self.end_out = Signal(1)
		self.busy_in = Signal(1)
		
		self.input_handler = InputHandler(config, constraints)
		self.output_handler = OutputHandler(config, constraints)

		self.ios = \
			[self.enc_in, self.enc_in_ctr, self.in_end, self.valid_in] + \
			[self.data_out, self.valid_out, self.latch_input, self.busy_in] + \
			[self.end_out]

	def elaborate(self, platform):

		m = Module()

		m.submodules.input_handler = input_handler = self.input_handler
		m.submodules.output_handler = output_handler = self.output_handler

		# this and input_handler
		m.d.comb += [
			self.latch_input.eq(input_handler.latch_input),
			input_handler.enc_in.eq(self.enc_in),
			input_handler.enc_in_ctr.eq(self.enc_in_ctr),
			input_handler.in_end.eq(self.in_end),
			input_handler.valid_in.eq(self.valid_in),
		]

		# input_handler and output_handler
		m.d.comb += [
			input_handler.dec_buff.eq(output_handler.dec_buff_out),
			output_handler.buffer.eq(input_handler.buffer),
			output_handler.buff_consum.eq(input_handler.buff_consum),
			output_handler.end_in.eq(input_handler.end_out),
			output_handler.new_buff_consum.eq(input_handler.new_buff_consum),
			output_handler.new_buff_consum_actv.eq(input_handler.new_buff_consum_actv),
		]

		# output_handler and this
		m.d.comb += [
			self.data_out.eq(output_handler.data_out),
			self.valid_out.eq(output_handler.valid_out),
			self.end_out.eq(output_handler.end_out),
			output_handler.busy_in.eq(self.busy_in),
		]

		return m

if __name__ == "__main__":
	config = {
		"out_bits" : 32,
		"converter": 48,
		"vbits_to_cbits_buffer_size": 144,
	}
	d = VBitsToCBits(config, constraints.Constraints())
	main(d, ports=d.ios)