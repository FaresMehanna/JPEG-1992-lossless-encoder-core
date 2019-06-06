from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *

class Converter31(Elaboratable):

	def __init__(self):

		# left fifo
		self.latch_output = Signal(1)
		self.enc_out = Signal(124)
		self.enc_out_ctr = Signal(7)
		self.out_end = Signal(1)
		self.valid_out = Signal(1)

		# right fifo
		self.enc_in = Signal(31)
		self.enc_in_ctr = Signal(5)
		self.in_end = Signal(1)
		self.valid_in = Signal(1)
		self.close_full = Signal(1)

		self.ios = [self.latch_output, self.enc_out, self.enc_out_ctr] + \
		[self.out_end, self.valid_out, self.enc_in, self.enc_in_ctr, self.in_end] + \
		[self.valid_in, self.close_full]


	def elaborate(self, platform):

		m = Module()

		enc_out_latch = Signal(93)
		out_end_latch = Signal(1)

		zeros = Signal(16)

		with m.FSM() as outTransaction:
			with m.State("IDLE"):
				m.d.sync += self.valid_in.eq(0)
				# if there is new input & can write it
				with m.If(self.valid_out & (self.close_full==0)):
					# latch the input
					m.d.sync += [
						self.latch_output.eq(1),
					]
					m.next = "BRUST"

			with m.State("BRUST"):
				with m.If(self.valid_out):
					#if all input can fill
					with m.If(self.enc_out_ctr <= 31):
						m.d.sync += [
							self.enc_in.eq(self.enc_out),
							self.enc_in_ctr.eq(self.enc_out_ctr),
							self.in_end.eq(self.out_end),
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
							self.enc_in_ctr.eq(31),
							self.in_end.eq(0),
							self.valid_in.eq(1),
							self.latch_output.eq(0),
							#latch current input
							enc_out_latch.eq(self.enc_out[0:93]),
							out_end_latch.eq(self.out_end),
						]
						with m.If(self.enc_out_ctr <= 62):
							m.d.sync += [
								self.enc_in.eq(self.enc_out[31:62]),
								self.enc_in_ctr.eq(self.enc_out_ctr - 31),
							]
							m.next = "2STEPS"
						with m.Elif(self.enc_out_ctr <= 93):
							m.d.sync += [
								self.enc_in.eq(self.enc_out[62:93]),
								self.enc_in_ctr.eq(self.enc_out_ctr - 62),
							]
							m.next = "3STEPS"
						with m.Elif(self.enc_out_ctr <= 124):
							m.d.sync += [
								self.enc_in.eq(self.enc_out[93:124]),
								self.enc_in_ctr.eq(self.enc_out_ctr - 93),
							]
							m.next = "4STEPS"
				with m.Else():
					m.d.sync += self.valid_in.eq(0)

					
			with m.State("2STEPS"):
				m.d.sync += [
					self.enc_in.eq(enc_out_latch[0:31]),
					self.enc_in_ctr.eq(31),
					self.in_end.eq(out_end_latch),
					self.valid_in.eq(1),
				]
				m.next = "IDLE"

			with m.State("3STEPS"):
				m.d.sync += [
					self.enc_in.eq(enc_out_latch[31:62]),
					self.enc_in_ctr.eq(31),
					self.in_end.eq(0),
					self.valid_in.eq(1),
				]
				m.next = "2STEPS"

			with m.State("4STEPS"):
				m.d.sync += [
					self.enc_in.eq(enc_out_latch[62:93]),
					self.enc_in_ctr.eq(31),
					self.in_end.eq(0),
					self.valid_in.eq(1),
				]
				m.next = "3STEPS"

		return m


if __name__ == "__main__":
	d = Converter31()
	main(d, ports=d.ios)