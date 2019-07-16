'''
--------------------
Module: Predictor_p1_c4_pix1_2
--------------------
Description: 
    - Predictor_p1_c4_pix1_2 is a module implements a predictor 
    functionality for the inputted pixels.The first step in 
    LJ92 encoding to the pixel is to use the neighbor pixels to
    predict its value, and that what this module is doing.
--------------------
Input: 
    - 1 or 2 pixels.
--------------------
Output:
    - the same 1 or 2 pixels.
    - the predicted value for those 1 or 2 pixels.
--------------------
timing:
    - the prediction always calculated within the same
    cycle to be available in the next rising edge.
--------------------
Notes :
    - Predictor module is the first step in LJ92 pipeline.
    - Input is the pixels value and the output the same pixel values and
    the predicted values for these pixels.
    - This predictor implements function 1 in LJ92 standard.
    - This predictor is assume the image contains 4 components.
    - This predictor can only be used with 1 or 2 input pixels.
    - The module uses traveling valid signal with no handshake.
    - The module is a MUST in LJ92 pipeline.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

# constants
PREDICTOR_FUNCTION = 1
COMPONENTS_NUM = 4

class PredictorP1C4Pix12(Elaboratable):

	def __init__(self, config, constraints):

		# config assertions
		assert config['pixels_per_cycle'] == 1 or config['pixels_per_cycle'] == 2
		assert config['predictor_function'] == PREDICTOR_FUNCTION
		assert config['num_of_components'] == COMPONENTS_NUM
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16

		# update constraints
		constraints.update_width(config['pixels_per_cycle'], "Predictor")
		constraints.update_width_multiple(config['pixels_per_cycle'], "Predictor")

		# save configurations
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']
		self.gb = int(COMPONENTS_NUM / config['pixels_per_cycle'])

		# pixels in
		self.pixels_in = Array(Signal(self.bd, name="pixel_in") for _ in range(self.ps))

		# same pixels in
		self.pixels_out = Array(Signal(self.bd, name="pixel_out") for _ in range(self.ps))

		# prediction using P1
		self.predics_out = Array(Signal(self.bd, name="predic_out") for _ in range(self.ps))

		# new row signal
		self.new_row = Signal(1)

		# valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		# end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		# debug counter
		self.debug_counter = Signal(32)

		self.ios = \
			[pixel_in for pixel_in in self.pixels_in] + \
			[pixel_out for pixel_out in self.pixels_out] + \
			[predic_out for predic_out in self.predics_out] + \
			[self.valid_in, self.valid_out, self.new_row] + \
			[self.end_in, self.end_out, self.debug_counter]

	def elaborate(self, platform):

		m = Module()

		# buffer values.
		# those are always four registers with a size of bitdepth, those used
		# to buffer last 4 pixels in the same row to be used later for prediction.
		buffs = Array(Array(Signal(self.bd, reset=2**(self.bd-1), name="buff") for _ in range(self.ps)) for _ in range(self.gb))

		# last row buffer.
		# those are always four registers with a size of bitdepth, those used
		# to buffer first 4 pixels in the current row to be used when predicting
		# first 4 pixels in the next row.
		lbuffs = Array(Array(Signal(self.bd, reset=2**(self.bd-1), name="lbuff") for _ in range(self.ps)) for _ in range(self.gb))

		buff_ctr = Signal(max=self.gb)
		lbuff_ctr = Signal(max=self.gb)

		new_row_reg = Signal(1)
		new_row_latch = Signal(1)

		#register new_row to last for self.gb cycles
		with m.If((self.valid_in==1) & (self.new_row==1)):
			m.d.sync += new_row_reg.eq(1)
		with m.Elif((self.valid_in==1) & (lbuff_ctr==self.gb-1)):
			m.d.sync += new_row_reg.eq(0)
		m.d.comb += new_row_latch.eq(self.new_row | new_row_reg)


		with m.If(self.valid_in):

			m.d.sync  += self.debug_counter.eq(self.debug_counter + 1)
			
			#handle pixels_out
			m.d.sync += [pixel_out.eq(pixel_in) for pixel_out, pixel_in in zip(self.pixels_out, self.pixels_in)]

			#handle buff update
			m.d.sync += buff_ctr.eq(buff_ctr+1)
			with m.Switch(buff_ctr):
				for i in range(self.gb):
					with m.Case(i):
						m.d.sync += [buff.eq(pixel_in) for buff, pixel_in in zip(buffs[i], self.pixels_in)]

			#handle lbuff update
			with m.If(new_row_latch):
				m.d.sync += lbuff_ctr.eq(lbuff_ctr+1)
				with m.Switch(lbuff_ctr):
					for i in range(self.gb):
						with m.Case(i):
							m.d.sync += [lbuff.eq(pixel_in) for lbuff, pixel_in in zip(lbuffs[i], self.pixels_in)]

			#handle prediction
			with m.If(new_row_latch):
				with m.Switch(lbuff_ctr):
					for i in range(self.gb):
						with m.Case(i):
							m.d.sync += [predic_out.eq(lbuff) for predic_out, lbuff in zip(self.predics_out, lbuffs[i])]
			with m.Else():
				with m.Switch(buff_ctr):
					for i in range(self.gb):
						with m.Case(i):
							m.d.sync += [predic_out.eq(buff) for predic_out, buff in zip(self.predics_out, buffs[i])]

		#if valid data
		m.d.sync += self.valid_out.eq(self.valid_in)

		# end
		m.d.sync += self.end_out.eq(self.end_in)

		return m


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 2,
		"predictor_function": 1,
		"num_of_components": 4,
	}
	p = PredictorP1C4Pix12(config, constraints.Constraints())
	main(p, ports=p.ios)