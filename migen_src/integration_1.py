from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *
import predictor, difference, normalize, encode, merge, signals, register_file

class Integration1(Elaboratable):

	def __init__(self):

		#pixels in
		self.pixel_in1 = Signal(16)
		self.pixel_in2 = Signal(16)
		self.pixel_in3 = Signal(16)
		self.pixel_in4 = Signal(16)

		self.enc_out = Signal(124)
		self.enc_out_ctr = Signal(7)

		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.ios = \
			[self.valid_in, self.valid_out] + \
			[self.pixel_in1, self.pixel_in2, self.pixel_in3] + \
			[self.enc_out, self.enc_out_ctr, self.pixel_in4]

		self.predictor = predictor.Predictor()
		self.difference = difference.Difference()
		self.normalize = normalize.Normalize()
		self.encode = encode.Encode()
		self.merge = merge.Merge()
		self.signals = signals.Signals()
		self.register_file = register_file.RegisterFile()

	def elaborate(self, platform):

		m = Module()

		m.submodules.predictor = predictor = self.predictor
		m.submodules.difference = difference = self.difference
		m.submodules.normalize = normalize = self.normalize
		m.submodules.encode = encode = self.encode
		m.submodules.merge = merge = self.merge
		m.submodules.signals = signals = self.signals
		m.submodules.register_file = register_file = self.register_file

		# signals
		m.d.comb += [
			signals.height.eq(register_file.height),
			signals.width.eq(register_file.width),
			signals.new_input.eq(self.valid_in),
		]

		# this and predictor
		m.d.comb += [
			predictor.pixel_in1.eq(self.pixel_in1),
			predictor.pixel_in2.eq(self.pixel_in2),
			predictor.pixel_in3.eq(self.pixel_in3),
			predictor.pixel_in4.eq(self.pixel_in4),
			predictor.new_row.eq(signals.new_row),
			predictor.valid_in.eq(self.valid_in),
		]

		# predictor and difference
		m.d.comb += [
			difference.pixel_in1.eq(predictor.pixel_out1),
			difference.pixel_in2.eq(predictor.pixel_out2),
			difference.pixel_in3.eq(predictor.pixel_out3),
			difference.pixel_in4.eq(predictor.pixel_out4),
			difference.predic_in1.eq(predictor.predic_out1),
			difference.predic_in2.eq(predictor.predic_out2),
			difference.predic_in3.eq(predictor.predic_out3),
			difference.predic_in4.eq(predictor.predic_out4),
			difference.valid_in.eq(predictor.valid_out),
		]

		# difference and normalize
		m.d.comb += [
			normalize.val_in1.eq(difference.val_out1),
			normalize.val_in2.eq(difference.val_out2),
			normalize.val_in3.eq(difference.val_out3),
			normalize.val_in4.eq(difference.val_out4),
			normalize.valid_in.eq(difference.valid_out),
		]

		# normalize and encode
		m.d.comb += [
			encode.val_in1.eq(normalize.val_out1),
			encode.val_in2.eq(normalize.val_out2),
			encode.val_in3.eq(normalize.val_out3),
			encode.val_in4.eq(normalize.val_out4),
			encode.ssss1.eq(normalize.ssss1),
			encode.ssss2.eq(normalize.ssss2),
			encode.ssss3.eq(normalize.ssss3),
			encode.ssss4.eq(normalize.ssss4),
			encode.valid_in.eq(normalize.valid_out),
		]

		# encode and merge
		m.d.comb += [
			merge.enc_in1.eq(encode.enc_out1),
			merge.enc_in2.eq(encode.enc_out2),
			merge.enc_in3.eq(encode.enc_out3),
			merge.enc_in4.eq(encode.enc_out4),
			merge.enc_in_ctr1.eq(encode.enc_ctr1),
			merge.enc_in_ctr2.eq(encode.enc_ctr2),
			merge.enc_in_ctr3.eq(encode.enc_ctr3),
			merge.enc_in_ctr4.eq(encode.enc_ctr4),
			merge.valid_in.eq(encode.valid_out),
		]

		# merge and this
		m.d.comb += [
			self.enc_out.eq(merge.enc_out),
			self.enc_out_ctr.eq(merge.enc_out_ctr),
			self.valid_out.eq(merge.valid_out),
		]

		return m


if __name__ == "__main__":
	d = Integration1()
	main(d, ports=d.ios)