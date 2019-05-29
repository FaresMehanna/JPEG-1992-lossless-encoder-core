from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
from constants import *

def get_ssss():
	return [(0b1110, 4),(0b000, 3),\
	(0b001, 3),(0b010, 3),(0b011, 3),\
	(0b100, 3),(0b101, 3),(0b110, 3),\
	(0b11110, 5),(0b111110, 6),(0b1111110, 7),\
	(0b11111110, 8),(0b111111110, 9),(0b1111111110, 10),\
	(0b11111111110, 11),(0b111111111110, 12),\
	(0b1111111111110, 13)]

def init_huff_table():
	ssss = get_ssss()
	assert (len(ssss) == 17),"You must provide 17 values in ssss list!"
	memory_data = []
	for sx in ssss:
		assert (sx[1] <= 16), "ssss value must be represented within 16 bits."
		memory_data.append((sx[0]<<5)|(sx[1]))
	return memory_data

class SingleEncoder(Elaboratable):

	def __init__(self):

		self.val_in = Signal(16)
		self.ssss = Signal(5)
		self.enc_out = Signal(31)
		self.enc_ctr = Signal(5)
		self.valid = Signal(1)

		self.ios = \
			[self.val_in, self.enc_out, self.enc_ctr, self.ssss, self.valid]

	def elaborate(self, platform):
		m = Module()

		# memory & read port
		# width = 21 = 16(value) + 5(count) 
		# depth = 17 different class of ssss
		mem = Memory(21, 17, init_huff_table())
		m.submodules.rp = rp = mem.read_port()

		# latch valid
		valid_late = Signal()
		m.d.sync += valid_late.eq(self.valid)

		# latch ssss & val_in
		ssss_late = Signal(5)
		m.d.sync += ssss_late.eq(self.ssss)
		val_in_late = Signal(16)
		m.d.sync += val_in_late.eq(self.val_in)

		#read port wiring
		m.d.comb += [
			rp.addr.eq(self.ssss),
		]

		#logic
		with m.If(valid_late):
			with m.If(ssss_late == 16):
				m.d.sync += [
						self.enc_out.eq(rp.data[5:21]),
						self.enc_ctr.eq(rp.data[0:5]),
					]
			with m.Else():
				m.d.sync += [
					self.enc_out.eq((rp.data[5:21]<<ssss_late) | val_in_late),
					self.enc_ctr.eq(rp.data[0:5] + ssss_late),
				]

		return m

class Encode(Elaboratable):

	def __init__(self):

		self.val_in1 = Signal(16)
		self.val_in2 = Signal(16)
		self.val_in3 = Signal(16)
		self.val_in4 = Signal(16)

		self.ssss1 = Signal(5)
		self.ssss2 = Signal(5)
		self.ssss3 = Signal(5)
		self.ssss4 = Signal(5)

		self.enc_out1 = Signal(31)
		self.enc_out2 = Signal(31)
		self.enc_out3 = Signal(31)
		self.enc_out4 = Signal(31)

		self.enc_ctr1 = Signal(5)
		self.enc_ctr2 = Signal(5)
		self.enc_ctr3 = Signal(5)
		self.enc_ctr4 = Signal(5)

		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		self.pixel1 = SingleEncoder()
		self.pixel2 = SingleEncoder()
		self.pixel3 = SingleEncoder()
		self.pixel4 = SingleEncoder()

		self.ios = \
			[self.val_in1, self.val_in2, self.val_in3, self.val_in4] + \
			[self.enc_out1, self.enc_out2, self.enc_out3, self.enc_out4] + \
			[self.enc_ctr1, self.enc_ctr2, self.enc_ctr3, self.enc_ctr4] + \
			[self.ssss1, self.ssss2, self.ssss3, self.ssss4] + \
			[self.valid_in, self.valid_out]

	def elaborate(self, platform):

		m = Module()

		m.submodules.pixel1 = pixel1 = self.pixel1
		m.submodules.pixel2 = pixel2 = self.pixel2
		m.submodules.pixel3 = pixel3 = self.pixel3
		m.submodules.pixel4 = pixel4 = self.pixel4

		m.d.comb += [
			pixel1.val_in.eq(self.val_in1),
			pixel1.valid.eq(self.valid_in),
			pixel1.ssss.eq(self.ssss1),
			self.enc_out1.eq(pixel1.enc_out),
			self.enc_ctr1.eq(pixel1.enc_ctr),
			pixel2.val_in.eq(self.val_in2),
			pixel2.valid.eq(self.valid_in),
			pixel2.ssss.eq(self.ssss2),
			self.enc_out2.eq(pixel2.enc_out),
			self.enc_ctr2.eq(pixel2.enc_ctr),
			pixel3.val_in.eq(self.val_in3),
			pixel3.valid.eq(self.valid_in),
			pixel3.ssss.eq(self.ssss3),
			self.enc_out3.eq(pixel3.enc_out),
			self.enc_ctr3.eq(pixel3.enc_ctr),
			pixel4.val_in.eq(self.val_in4),
			pixel4.valid.eq(self.valid_in),
			pixel4.ssss.eq(self.ssss4),
			self.enc_out4.eq(pixel4.enc_out),
			self.enc_ctr4.eq(pixel4.enc_ctr),
		]

		#if valid data
		valid_late = Signal()
		m.d.sync += valid_late.eq(self.valid_in)
		m.d.sync += self.valid_out.eq(valid_late)

		return m

if __name__ == "__main__":
	e = Encode()
	main(e, ports=e.ios)