from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import difference, normalize, encode, merge, signals
import constraints
import predictor_p1_c4_px4, predictor_p1_c4_pix1_2
import core_axi_lite

class Integration1(Elaboratable):

	def __init__(self, config, cons):

		assert config['bit_depth'] >= 1
		assert config['pixels_per_cycle'] >= 1

		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']
		enc_out_bits = min(31, 16+self.bd) * self.ps

		#pixels in
		self.pixels_in = Array(Signal(self.bd, name="pixel_in") for _ in range(self.ps))

		#enc out
		self.enc_out = Signal(enc_out_bits)
		self.enc_out_ctr = Signal(max=enc_out_bits+1)

		# valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		# end
		self.end_out = Signal(1)

		if self.ps == 4:
			self.predictor = predictor_p1_c4_px4.PredictorP1C4Px4(config, cons)
		else:
			self.predictor = predictor_p1_c4_pix1_2.PredictorP1C4Pix12(config, cons)
		self.difference = difference.Difference(config, cons)
		self.normalize = normalize.Normalize(config, cons)
		self.encode = encode.Encode(config, cons)
		#create a merge layer only if more than one pixel per cycle
		if self.ps > 1:
			self.merge = merge.Merge(config, cons)
		self.signals = signals.Signals(config, cons)
		self.core_axi_lite = core_axi_lite.CoreAxiLite(config, cons)

		self.ios = \
			[pixel_in for pixel_in in self.pixels_in] + \
			[self.enc_out, self.enc_out_ctr] + \
			[self.valid_in, self.valid_out] + \
			[self.end_out]
			
	def elaborate(self, platform):

		m = Module()

		m.submodules.predictor = predictor = self.predictor
		m.submodules.difference = difference = self.difference
		m.submodules.normalize = normalize = self.normalize
		m.submodules.encode = encode = self.encode
		if self.ps > 1:
			m.submodules.merge = merge = self.merge
		m.submodules.signals = signals = self.signals
		m.submodules.core_axi_lite = core_axi_lite = self.core_axi_lite

		# signals
		m.d.comb += [
			signals.height.eq(core_axi_lite.height),
			signals.width.eq(core_axi_lite.width),
			signals.new_input.eq(self.valid_in),
		]

		# this and predictor
		m.d.comb += [pred_pixel_in.eq(pixel_in) for pred_pixel_in, pixel_in in zip(predictor.pixels_in, self.pixels_in)]
		m.d.comb += [
			predictor.new_row.eq(signals.new_row),
			predictor.end_in.eq(signals.end_of_frame),
			predictor.valid_in.eq(self.valid_in),
		]

		# predictor and difference
		m.d.comb += [pixel_in.eq(pixel_out) for pixel_in, pixel_out in zip(difference.pixels_in, predictor.pixels_out)]
		m.d.comb += [predic_in.eq(predic_out) for predic_in, predic_out in zip(difference.predics_in, predictor.predics_out)]
		m.d.comb += [
			difference.valid_in.eq(predictor.valid_out),
			difference.end_in.eq(predictor.end_out),

		]

		# difference and normalize
		m.d.comb += [val_in.eq(val_out) for val_in, val_out in zip(normalize.vals_in, difference.vals_out)]
		m.d.comb += [val_in_mns.eq(val_out_mns) for val_in_mns, val_out_mns in zip(normalize.vals_in_mns, difference.vals_out_mns)]
		m.d.comb += [
			normalize.valid_in.eq(difference.valid_out),
			normalize.end_in.eq(difference.end_out),			
		]

		# normalize and encode
		m.d.comb += [val_in.eq(val_out) for val_in, val_out in zip(encode.vals_in, normalize.vals_out)]
		m.d.comb += [ssss1.eq(ssss2) for ssss1, ssss2 in zip(encode.ssssx, normalize.ssssx)]
		m.d.comb += [
			encode.valid_in.eq(normalize.valid_out),
			encode.end_in.eq(normalize.end_out),
		]

		# core axi lite and encode
		m.d.comb += [
			core_axi_lite.rp_data.eq(encode.extern_r_port.data),
			encode.extern_r_port.addr.eq(core_axi_lite.rp_addr),
			encode.extern_w_port.addr.eq(core_axi_lite.wp_addr),
			encode.extern_w_port.data.eq(core_axi_lite.wp_data),
			encode.extern_w_port.en.eq(core_axi_lite.wp_en),
		]

		if self.ps > 1:
			# encode and merge
			m.d.comb += [enc_in.eq(enc_out) for enc_in, enc_out in zip(merge.encs_in, encode.encs_out)]
			m.d.comb += [enc_in_ctr.eq(enc_ctr) for enc_in_ctr, enc_ctr in zip(merge.encs_in_ctr, encode.encs_ctr)]
			m.d.comb += [
				merge.valid_in.eq(encode.valid_out),
				merge.end_in.eq(encode.end_out),
			]
			# merge and this
			m.d.comb += [
				self.enc_out.eq(merge.enc_out),
				self.enc_out_ctr.eq(merge.enc_out_ctr),
				self.valid_out.eq(merge.valid_out),
				self.end_out.eq(merge.end_out),
			]

		else:
			# encode and this
			m.d.comb += [
				self.enc_out.eq(encode.encs_out[0]),
				self.enc_out_ctr.eq(encode.encs_ctr[0]),
				self.valid_out.eq(encode.valid_out),
				self.end_out.eq(encode.end_out),
			]

		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 12,
		"pixels_per_cycle": 2,
		"predictor_function": 1,
		"num_of_components": 4,
	}
	cons = constraints.Constraints()
	d = Integration1(config, cons)
	main(d, ports=d.ios)