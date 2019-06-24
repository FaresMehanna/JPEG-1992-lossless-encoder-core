from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

class Signals(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['pixels_per_cycle'] >= 1

		#save needed configs
		self.ps = config['pixels_per_cycle']

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
						width_temp.eq(self.width-self.ps),
						height_temp.eq(self.height-1),
						self.new_row.eq(0),
					]
					m.next = "LOOP"

			with m.State("LOOP"):
				with m.If(self.new_input):
					with m.If(width_temp == self.ps):
						m.d.sync += [
							width_temp.eq(self.width),
							height_temp.eq(height_temp - 1),
							self.new_row.eq(1),
						]
					with m.Else():
						m.d.sync += [
							width_temp.eq(width_temp-self.ps),
							self.new_row.eq(0),
						]
					with m.If((height_temp == 0) & (width_temp == 2*self.ps)):
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
	config = {
		"pixels_per_cycle": 2,
	}
	m = Signals(config, constraints.Constraints())
	main(m, ports=m.ios)