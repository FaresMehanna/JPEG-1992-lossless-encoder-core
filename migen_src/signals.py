from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *

class Signals(Elaboratable):

	def __init__(self):

		self.height = Signal(16)
		self.width = Signal(16)
		self.new_input = Signal(1)

		self.end_of_frame = Signal(1)
		self.new_row = Signal(1, reset=1)

		self.ios = \
		[self.height, self.width, self.new_input] + \
		[self.end_of_frame, self.new_row]

	def elaborate(self, platform):

		m = Module()

		width_temp = Signal(16)
		height_temp = Signal(16)
		temp = Signal(1)

		with m.FSM() as fsm:

			with m.State("IDLE"):
				with m.If(self.new_input):
					m.d.sync += [
						width_temp.eq(self.width-4),
						height_temp.eq(self.height-1),
						self.new_row.eq(0),
					]
					m.next = "LOOP"

			with m.State("LOOP"):
				with m.If(self.new_input):
					with m.If(width_temp == 4):
						m.d.sync += [
							width_temp.eq(self.width),
							height_temp.eq(height_temp - 1),
							self.new_row.eq(1),
						]
					with m.Else():
						m.d.sync += [
							width_temp.eq(width_temp-4),
							self.new_row.eq(0),
						]
					with m.If((height_temp == 0) & (width_temp == 4)):
						m.d.sync += [
							self.end_of_frame.eq(1),
						]
						m.next = "END"

			with m.State("END"):
				m.d.sync += [
					self.end_of_frame.eq(1),
				]

		return m

if __name__ == "__main__":
	m = Signals()
	main(m, ports=m.ios)