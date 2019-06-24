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

		#is read happen to the buffer?
		self.dec_buff_out = Signal(1)

		#signal for end from input handler
		self.end_in = Signal(1)


	def elaborate(self, platform):

		m = Module()

		# right & left shift to handle data output
		shift_right = Signal(max=self.buffer_size-self.output_size+1)
		shift_left = Signal(max=self.output_size)
		m.d.comb += shift_right.eq(self.buff_consum - self.output_size)
		m.d.comb += shift_left.eq(self.output_size - self.buff_consum)

		# initial value for dec_buff_out
		m.d.comb += self.dec_buff_out.eq(0)

		# conditions
		buff_consum_less_eq = Signal(1)
		buff_consum_greater_eq = Signal(1)

		m.d.comb += [
			buff_consum_greater_eq.eq((self.buff_consum >= self.output_size)),
			buff_consum_less_eq.eq((self.buff_consum <= self.output_size)),
		]

		def do_output():
			with m.If(buff_consum_greater_eq):
				m.d.sync += self.data_out.eq(self.buffer >> shift_right),
			with m.Else():
				m.d.sync += self.data_out.eq(self.buffer << shift_left),
			#added to handle end signal - if last input then sent end_out to one
			with m.If((buff_consum_less_eq) & self.end_in):
				m.d.sync += self.end_out.eq(1)
				m.next = "END"
			m.d.sync += self.valid_out.eq(1)
			m.d.comb += self.dec_buff_out.eq(1)

		# activate valid signal
		with m.FSM() as outTransaction:

			with m.State("OUTPUT"):
				#if we have enough data, or end signal is activated -> last input
				with m.If((buff_consum_greater_eq) | ((buff_consum_less_eq) & self.end_in)):
					m.next = "BRUST"
					do_output()

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

			with m.State("END"):
				pass

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

		#signals indicating decrease in buffer
		self.dec_buff = Signal(1)

		#signal for end
		self.end_out = Signal(1)

		self.ios = \
			[self.enc_in, self.enc_in_ctr, self.in_end, self.valid_in] + \
			[self.latch_input, self.buffer, self.buff_consum] + \
			[self.end_out, self.dec_buff]

	def elaborate(self, platform):

		m = Module()

		# inner buff consumption - same as self.buff_consum, better for routing?
		self.start = Signal(1)
		self.buff_free = Signal(max=(self.buffer_size+1))
		self.new_buff_free = Signal(max=(self.buffer_size+1))

		#signals indicating increase & decrease in buffer
		self.inc_buff = Signal(1)
		self.buff_change = Signal(1)
		m.d.comb += self.inc_buff.eq(0)
		m.d.comb += self.buff_change.eq(self.inc_buff | self.dec_buff)

		# register valid_in
		valid_in_late = Signal(1)
		m.d.sync += valid_in_late.eq(self.valid_in)

		# to register data from fifo
		enc_in_reg = Signal(self.input_size)
		enc_in_ctr_reg = Signal(max=(self.input_size+1))
		in_end_reg = Signal(1)
		valid_in_reg = Signal(1)

		# to buffer un-handled data
		enc_in_buff = Signal(self.input_size)
		enc_in_ctr_buff = Signal(max=(self.input_size+1))
		in_end_buff = Signal(1)
		valid_in_buff = Signal(1)

		#signal indicating buffer register
		self.buff_reg = Signal(1)
		m.d.comb += self.buff_reg.eq(0)


		def reg_data():
			m.d.sync += [
				enc_in_reg.eq(self.enc_in),
				enc_in_ctr_reg.eq(self.enc_in_ctr),
				in_end_reg.eq(self.in_end),
				valid_in_reg.eq(self.valid_in),
			]
			m.d.comb += self.buff_reg.eq(1)

		def get_input_from_reg():
			m.d.sync += [
				self.buffer.eq((self.buffer << enc_in_ctr_reg) | enc_in_reg),
				self.end_out.eq(in_end_reg),
			]
			m.d.comb += self.inc_buff.eq(1)

		def reg_to_buff():
			m.d.sync += [
				enc_in_buff.eq(enc_in_reg),
				enc_in_ctr_buff.eq(enc_in_ctr_reg),
				in_end_buff.eq(in_end_reg),
				valid_in_buff.eq(valid_in_reg),
			]

		def swap_reg_buff():
			# do swap
			m.d.sync += [
				enc_in_buff.eq(enc_in_reg),
				enc_in_ctr_buff.eq(enc_in_ctr_reg),
				in_end_buff.eq(in_end_reg),
				enc_in_reg.eq(enc_in_buff),
				enc_in_ctr_reg.eq(enc_in_ctr_buff),
				in_end_reg.eq(in_end_buff),
			]

		# for some unknown reason, reset value in Signal() doesn't
		# work, so this is work around this problem.
		with m.If(self.start==0):
			m.d.sync += [
				self.buff_free.eq(self.buffer_size),
				self.start.eq(1),
			]

		with m.FSM() as inTransaction:

			with m.State("INPUT"):
					#valid data in buffer
					with m.If(valid_in_buff):
						with m.If((enc_in_ctr_buff <= self.buff_free)):
							swap_reg_buff()
							m.next = "CLEAN_BUFFER"
					#if we have data in buffer
					with m.Elif(valid_in_reg):
						m.d.sync += self.latch_input.eq(1)
						m.next = "BRUST"
					#if we have new data
					with m.Else():
						m.d.sync += self.latch_input.eq(1)
						m.next = "REGISTER_FOR_BRUST"

			with m.State("CLEAN_BUFFER"):
				# invalidate buffered data
				m.d.sync += valid_in_buff.eq(0),
				# swap regs back
				swap_reg_buff()
				# get input from swapped data then go to input
				get_input_from_reg()
				### short cut ###
				#if we have data in buffer
				with m.If(valid_in_reg):
					m.d.sync += self.latch_input.eq(1)
					m.next = "BRUST"
				#if we have new data
				with m.Else():
					m.d.sync += self.latch_input.eq(1)
					m.next = "REGISTER_FOR_BRUST"

			with m.State("REGISTER_FOR_BRUST"):
				reg_data()
				m.next = "BRUST"

			with m.State("BRUST"):
				#if we have new data
				reg_data()
				reg_to_buff()
				with m.If(valid_in_reg):
					with m.If(enc_in_ctr_reg <= self.buff_free):
						get_input_from_reg()
						m.d.sync += self.latch_input.eq(1)
					with m.Else():
						m.d.sync += self.latch_input.eq(0)
						m.next = "INPUT"

		#handle buffer free
		with m.If(self.inc_buff & self.dec_buff):
			m.d.comb += self.new_buff_free.eq(self.buff_free + self.output_size - enc_in_ctr_reg)
		with m.Else():
			with m.If(self.dec_buff):
				m.d.comb += self.new_buff_free.eq(self.buff_free + self.output_size)
			with m.Elif(self.inc_buff):
				m.d.comb += self.new_buff_free.eq(self.buff_free - enc_in_ctr_reg)

		# update buff_free, buff_consum
		with m.If(self.buff_change):
			m.d.sync += self.buff_free.eq(self.new_buff_free)
			m.d.sync += self.buff_consum.eq(self.buffer_size - self.new_buff_free)

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