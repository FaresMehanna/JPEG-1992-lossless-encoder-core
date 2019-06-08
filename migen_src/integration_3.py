from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *
import predictor, difference, normalize, encode, merge
import signals, register_file, delayer, converter48
import lj92_pipeline_fifo, converter_fifo, vbits_to_cbits

class Integration3(Elaboratable):

	def __init__(self):

		#pixels in
		self.pixel_in1 = Signal(16)
		self.pixel_in2 = Signal(16)
		self.pixel_in3 = Signal(16)
		self.pixel_in4 = Signal(16)
		self.nready = Signal(1)

		self.data_out = Signal(64)
		self.busy_in = Signal(1)

		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)
		self.end_out = Signal(1)

		self.ios = \
			[self.valid_in, self.valid_out, self.end_out] + \
			[self.pixel_in1, self.pixel_in2, self.pixel_in3] + \
			[self.data_out, self.busy_in, self.pixel_in4, self.nready]

		self.predictor = predictor.Predictor()
		self.difference = difference.Difference()
		self.normalize = normalize.Normalize()
		self.encode = encode.Encode()
		self.merge = merge.Merge()
		self.signals = signals.Signals()
		self.register_file = register_file.RegisterFile()
		self.lj92_pipeline_fifo = lj92_pipeline_fifo.LJ92PipelineFifo(128)
		self.converter = converter48.Converter48()
		self.converter_fifo = converter_fifo.ConverterFifo(256)
		self.vbits_to_cbits = vbits_to_cbits.VBitsToCBits()
		self.end_delayer = delayer.Delayer(6)

	def elaborate(self, platform):

		m = Module()

		m.submodules.predictor = predictor = self.predictor
		m.submodules.difference = difference = self.difference
		m.submodules.normalize = normalize = self.normalize
		m.submodules.encode = encode = self.encode
		m.submodules.merge = merge = self.merge
		m.submodules.signals = signals = self.signals
		m.submodules.register_file = register_file = self.register_file
		m.submodules.lj92_pipeline_fifo = lj92_pipeline_fifo = self.lj92_pipeline_fifo
		m.submodules.converter = converter = self.converter
		m.submodules.converter_fifo = converter_fifo = self.converter_fifo
		m.submodules.vbits_to_cbits = vbits_to_cbits = self.vbits_to_cbits
		m.submodules.end_delayer = end_delayer = self.end_delayer

		# signals
		m.d.comb += [
			signals.height.eq(register_file.height),
			signals.width.eq(register_file.width),
			signals.new_input.eq((self.valid_in == 1) & (lj92_pipeline_fifo.close_full == 0)),
			end_delayer.in_sig.eq(signals.end_of_frame),
		]

		# this and predictor
		m.d.comb += [
			predictor.pixel_in1.eq(self.pixel_in1),
			predictor.pixel_in2.eq(self.pixel_in2),
			predictor.pixel_in3.eq(self.pixel_in3),
			predictor.pixel_in4.eq(self.pixel_in4),
			predictor.new_row.eq(signals.new_row),
			predictor.valid_in.eq((self.valid_in == 1) & (lj92_pipeline_fifo.close_full == 0)),
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

		# merge and lj92_pipeline_fifo
		m.d.comb += [
			lj92_pipeline_fifo.enc_in.eq(merge.enc_out),
			lj92_pipeline_fifo.enc_in_ctr.eq(merge.enc_out_ctr),
			lj92_pipeline_fifo.in_end.eq(end_delayer.out_sig),
			lj92_pipeline_fifo.valid_in.eq(merge.valid_out),
		]

		# lj92_pipeline_fifo and converter
		m.d.comb += [
			lj92_pipeline_fifo.latch_output.eq(converter.latch_output),
			converter.enc_out.eq(lj92_pipeline_fifo.enc_out),
			converter.enc_out_ctr.eq(lj92_pipeline_fifo.enc_out_ctr),
			converter.out_end.eq(lj92_pipeline_fifo.out_end),
			converter.valid_out.eq(lj92_pipeline_fifo.valid_out),
		]

		# converter and converter_fifo
		m.d.comb += [
			converter_fifo.enc_in.eq(converter.enc_in),
			converter_fifo.enc_in_ctr.eq(converter.enc_in_ctr),
			converter_fifo.in_end.eq(converter.in_end),
			converter_fifo.valid_in.eq(converter.valid_in),
			converter.close_full.eq(converter_fifo.close_full),
		]

		# converter_fifo and vbits_to_cbits
		m.d.comb += [
			converter_fifo.latch_output.eq(vbits_to_cbits.latch_input),
			vbits_to_cbits.enc_in.eq(converter_fifo.enc_out),
			vbits_to_cbits.enc_in_ctr.eq(converter_fifo.enc_out_ctr),
			vbits_to_cbits.in_end.eq(converter_fifo.out_end),
			vbits_to_cbits.valid_in.eq(converter_fifo.valid_out),
			vbits_to_cbits.busy_in.eq(self.busy_in),
		]

		# vbits_to_cbits and this
		m.d.comb += [
			self.data_out.eq(vbits_to_cbits.data_out),
			self.valid_out.eq(vbits_to_cbits.valid_out),
			self.end_out.eq(vbits_to_cbits.end_out),
		]

		# self.busy
		m.d.comb += [
			self.nready.eq(lj92_pipeline_fifo.close_full),
		]

		return m


if __name__ == "__main__":
	d = Integration3()
	main(d, ports=d.ios)