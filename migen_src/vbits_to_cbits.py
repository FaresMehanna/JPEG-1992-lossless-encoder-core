from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *

INPUT_SIZE = 48
OUTPUT_SIZE = 32
BUFFER_SIZE = 144

class BufferPicker(Elaboratable):

	def __init__(self):

		self.in_signal = Signal(BUFFER_SIZE)
		self.out_signal = Signal(OUTPUT_SIZE)
		self.buff_consum = Signal(max=(BUFFER_SIZE+1))

		self.ios = [self.in_signal, self.out_signal, self.buff_consum]

	def elaborate(self, platform):

		m = Module()
		zeros = Signal(OUTPUT_SIZE)
		with m.Switch(self.buff_consum):
			for i in range(1, OUTPUT_SIZE):
				start = 0
				end = i
				zero_length = OUTPUT_SIZE - i
				with m.Case(i):
					m.d.comb += [
						self.out_signal.eq(Cat(zeros[0:zero_length],self.in_signal[start:end])),
					]
			for i in range(OUTPUT_SIZE, BUFFER_SIZE+1):
				start = i - OUTPUT_SIZE
				end = i
				with m.Case(i):
					m.d.comb += [
						self.out_signal.eq(self.in_signal[start:end]),
					]
		return m

class BufferSetter(Elaboratable):

	def __init__(self):

		self.enc_in = Signal(INPUT_SIZE)
		self.enc_in_ctr = Signal(max=(INPUT_SIZE+1))
		self.buff = Signal(BUFFER_SIZE)
		self.latch = Signal(1)

		self.ios = [self.enc_in, self.enc_in_ctr, self.buff]


	def elaborate(self, platform):

		m = Module()

		with m.If(self.latch):
			m.d.sync += [
				self.buff.eq((self.buff << self.enc_in_ctr) | self.enc_in),
			]

		return m


class VBitsToCBits(Elaboratable):

	def __init__(self):

		assert BUFFER_SIZE >= (INPUT_SIZE+OUTPUT_SIZE)
		assert OUTPUT_SIZE%8 == 0

		self.out_bytes = int(OUTPUT_SIZE/8)
		self.latch_input = Signal(1)
		self.enc_in = Signal(INPUT_SIZE)
		self.enc_in_ctr = Signal(max=(INPUT_SIZE+1))
		self.in_end = Signal(1)
		self.valid_in = Signal(1)

		self.data_out = Signal(OUTPUT_SIZE)
		self.valid_out = Signal(1)
		self.end_out = Signal(1)

		self.busy_in = Signal(1)
		
		self.buffer_picker = BufferPicker()
		self.buffer_setter = BufferSetter()

		self.ios = \
			[self.enc_in, self.enc_in_ctr, self.in_end, self.valid_in] + \
			[self.data_out, self.valid_out, self.latch_input, self.busy_in] + \
			[self.end_out]

	def elaborate(self, platform):

		m = Module()

		buff = Signal(BUFFER_SIZE)
		buff_consum = Signal(max=(BUFFER_SIZE+1))

		output = Signal(OUTPUT_SIZE)
		buffered_output = Signal(OUTPUT_SIZE)
		m.d.sync += self.data_out.eq(output)

		m.submodules.buff_pick = buff_pick = self.buffer_picker
		m.d.comb += [
			buff_pick.in_signal.eq(buff),
			buff_pick.buff_consum.eq(buff_consum),
			output.eq(buff_pick.out_signal),
		]

		buff_set_latch = Signal(1)
		m.d.comb += buff_set_latch.eq(0)

		m.submodules.buff_set = buff_set = self.buffer_setter
		m.d.comb += [
			buff.eq(buff_set.buff),
			buff_set.enc_in.eq(self.enc_in),
			buff_set.enc_in_ctr.eq(self.enc_in_ctr),
			buff_set.latch.eq(buff_set_latch),
		]
		
		sig1 = Signal(1)
		sig2 = Signal(1)

		m.d.comb += [
			sig1.eq(0),
			sig2.eq(buff_set_latch),
		]

		current_end = Signal()

		# activate valid signal
		with m.FSM() as outTransaction:

			with m.State("OUTPUT"):
				#if we have enough data, or end signal is activated -> last input
				with m.If((buff_consum >= OUTPUT_SIZE) | ((buff_consum < OUTPUT_SIZE) & current_end)):
					m.d.comb += sig1.eq(1)
					m.d.sync += [
						self.valid_out.eq(1),
						buffered_output.eq(output),
					]
					m.next = "BRUST"
				#added to handle end signal - if last input then sent end_out to one
				with m.If((buff_consum <= OUTPUT_SIZE) & current_end):
					m.d.sync += [
						self.end_out.eq(1),
					]

			with m.State("BRUST"):
				#device latched the prev output and new output is ready
				with m.If((self.busy_in == 0) & (buff_consum >= OUTPUT_SIZE)):
					m.d.comb += sig1.eq(1)
					m.d.sync += [
						self.valid_out.eq(1),
						buffered_output.eq(output),
					]
				#device latched the prev output but NO new output is ready
				with m.Elif(self.busy_in == 0):
					m.d.sync += [
						self.valid_out.eq(0),
					]
					m.next = "OUTPUT"
				#device did not latch the prev output
				with m.Else():
					m.d.sync += self.data_out.eq(buffered_output)
				#added to handle end signal - if last input then sent end_out to one
				with m.If((buff_consum <= OUTPUT_SIZE) & current_end):
					m.d.sync += [
						self.end_out.eq(1),
					]

		new_consum = Signal(max=(BUFFER_SIZE+1))
		with m.FSM() as inTransaction:

			with m.State("INPUT"):
				with m.If(buff_consum <= (BUFFER_SIZE-INPUT_SIZE)):
					#if we have new data
					with m.If(self.valid_in):
						m.d.sync += [
							self.latch_input.eq(1),
						]
						m.next = "DELAY_BRUST"

			with m.State("DELAY_BRUST"):
				with m.If(self.valid_in):
					m.d.comb += buff_set_latch.eq(1)
					m.d.sync += current_end.eq(self.in_end)
					# burst
					with m.If((new_consum <= (BUFFER_SIZE-INPUT_SIZE))):
						m.next = "BRUST"
					with m.Else():
						m.d.sync += [
							self.latch_input.eq(0),
						]
						m.next = "INPUT"
				with m.Else():
					m.next = "INPUT"

			with m.State("BRUST"):
				#if we have new data
				with m.If(self.valid_in):
					m.d.comb += buff_set_latch.eq(1)
					m.d.sync += current_end.eq(self.in_end)
					with m.If(new_consum <= (BUFFER_SIZE-INPUT_SIZE)):
						m.d.sync += [
							self.latch_input.eq(1),
						]
					with m.Else():
						m.d.sync += [
							self.latch_input.eq(0),
						]
						m.next = "INPUT"

		with m.If(sig1 & sig2):
			m.d.comb += new_consum.eq(buff_consum - OUTPUT_SIZE + self.enc_in_ctr)
		with m.Elif(sig1):
			m.d.comb += new_consum.eq(buff_consum - OUTPUT_SIZE)
		with m.Elif(sig2):
			m.d.comb += new_consum.eq(buff_consum+ self.enc_in_ctr)

		with m.If(sig1 | sig2):
			m.d.sync += buff_consum.eq(new_consum)

		return m

if __name__ == "__main__":
	d = VBitsToCBits()
	main(d, ports=d.ios)