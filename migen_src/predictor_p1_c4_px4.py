'''
--------------------
Module: Predictor_p1_c4_px4
--------------------
Description: 
    - Predictor_p1_c4_px4 is a module implements a predictor 
    functionality for the inputted pixels.The first step in 
    LJ92 encoding to the pixel is to use the neighbor pixels to
    predict its value, and that what this module is doing.
--------------------
Input: 
    - 4 pixels.
--------------------
Output:
    - the same 4 pixels.
    - the predicted value for those 4 pixels.
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
    - This predictor can only be used with 4 input pixels.
    - The module uses traveling valid signal with no handshake.
    - The module is a MUST in LJ92 pipeline.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

#constants
COMPONENTS_NUM = 4
PREDICTOR_FUNCTION = 1

class PredictorP1C4Px4(Elaboratable):

	def __init__(self, config, constraints):

		# config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] == 4
		assert config['predictor_function'] == PREDICTOR_FUNCTION
		assert config['num_of_components'] == COMPONENTS_NUM

		# save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']

		# update constraints
		constraints.update_width(config['pixels_per_cycle'], "Predictor")
		constraints.update_width_multiple(config['pixels_per_cycle'], "Predictor")

		# pixels in
		self.pixels_in = Array(Signal(self.bd, name="pixel_in") for _ in range(self.ps))

		# new row signal
		self.new_row = Signal(1)

		# same pixels in
		self.pixels_out = Array(Signal(self.bd, name="pixel_out") for _ in range(self.ps))

		# prediction using P1
		self.predics_out = Array(Signal(self.bd, name="predic_out") for _ in range(self.ps))

		# valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		# end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.ios = \
			[predic_out for predic_out in self.predics_out] + \
			[pixel_out for pixel_out in self.pixels_out] + \
			[pixel_in for pixel_in in self.pixels_in] + \
			[self.valid_in, self.valid_out] + \
			[self.end_in, self.end_out]

	def elaborate(self, platform):

		m = Module()

		# buffer values
		# those are always four registers with a size of bitdepth, those used
		# to buffer last 4 pixels in the same row to be used later for prediction.
		buffs = Array(Signal(self.bd, reset=2**(self.bd-1), name="buff") for _ in range(COMPONENTS_NUM))

		# last row buffer
		# those are always four registers with a size of bitdepth, those used
		# to buffer first 4 pixels in the current row to be used when predicting
		# first 4 pixels in the next row.
		lbuffs = Array(Signal(self.bd, reset=2**(self.bd-1), name="lbuff") for _ in range(COMPONENTS_NUM))

		with m.If(self.valid_in):

			# handle pixel_out
			m.d.sync += [pixel_out.eq(pixel_in) for pixel_out, pixel_in in zip(self.pixels_out, self.pixels_in)]

			#handle prediction
			with m.If(self.new_row):
				m.d.sync += [predic_out.eq(lbuff) for predic_out, lbuff in zip(self.predics_out, lbuffs)]
			with m.Else():
				m.d.sync += [predic_out.eq(buff) for predic_out, buff in zip(self.predics_out, buffs)]

			#handle row-buffer (lbuff) update
			with m.If(self.new_row):
				m.d.sync += [lbuff.eq(pixel_in) for lbuff, pixel_in in zip(lbuffs, self.pixels_in)]

			#handle ordinary-buffers (buffs)
			m.d.sync += [buff.eq(pixel_in) for buff, pixel_in in zip(buffs, self.pixels_in)]

		#if valid data
		m.d.sync += self.valid_out.eq(self.valid_in)

		# end
		m.d.sync += self.end_out.eq(self.end_in)

		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 4,
		"predictor_function": 1,
		"num_of_components": 4,
	}
	p = PredictorP1C4Px4(config, constraints.Constraints())
	main(p, ports=p.ios)