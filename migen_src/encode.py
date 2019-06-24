from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import constraints

def get_ssss():
	return [(0b1110, 4),(0b000, 3),\
	(0b001, 3),(0b010, 3),(0b011, 3),\
	(0b100, 3),(0b101, 3),(0b110, 3),\
	(0b11110, 5),(0b111110, 6),(0b1111110, 7),\
	(0b11111110, 8),(0b111111110, 9),(0b1111111110, 10),\
	(0b11111111110, 11),(0b111111111110, 12),\
	(0b1111111111110, 13)]

def init_huff_table(bd):
	ssss = get_ssss()[0:bd+1]
	assert (len(ssss) == (bd+1)),"You must provide all values in ssss list for wanted bit_depth!"
	memory_data = []
	for ind, sx in enumerate(ssss):
		assert (sx[1] <= 16), "ssss value must be represented within 16 bits."
		if ind == 16:	#last one is special
			memory_data.append((sx[1] << (16+bd)) | sx[0])
		else:
			memory_data.append((sx[1] << (16+bd)) | (sx[0] << ind))
	return memory_data

class SingleEncoder(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		#save needed configs
		self.bd = config['bit_depth']
		self.rp_addr = Signal(5)
		self.rp_data = Signal(self.bd+21)

		self.val_in = Signal(self.bd)
		self.ssss = Signal(5)
		self.enc_out = Signal(min(16+self.bd, 31))
		self.enc_ctr = Signal(5)

		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		#end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.ios = \
			[self.val_in, self.enc_out, self.enc_ctr, self.ssss] + \
			[self.valid_in, self.valid_out] + \
			[self.end_in, self.end_out]

	def elaborate(self, platform):
		m = Module()

		# register valid
		valid_late = Signal()
		m.d.sync += valid_late.eq(self.valid_in)
		m.d.sync += self.valid_out.eq(valid_late)

		# register end
		end_late = Signal()
		m.d.sync += end_late.eq(self.end_in)
		m.d.sync += self.end_out.eq(end_late)

		# latch ssss & val_in
		ssss_late = Signal(5)
		m.d.sync += ssss_late.eq(self.ssss)
		val_in_late = Signal(self.bd)
		m.d.sync += val_in_late.eq(self.val_in)

		#read port wiring
		m.d.comb += [
			self.rp_addr.eq(self.ssss),
		]

		sx_ctr_offset = 16+self.bd

		#logic
		with m.If(valid_late):
			#only need this branch if the sensor support 16bits depth
			if self.bd == 16:
				with m.If(ssss_late == 16):
					m.d.sync += [
						self.enc_out.eq(self.rp_data),
						self.enc_ctr.eq(self.rp_data[sx_ctr_offset:sx_ctr_offset+5]),
					]
				with m.Else():
					m.d.sync += [
						self.enc_out.eq(self.rp_data | val_in_late),
						self.enc_ctr.eq(self.rp_data[sx_ctr_offset:sx_ctr_offset+5] + ssss_late[0:4]),
					]
			else:
				m.d.sync += [
					self.enc_out.eq(self.rp_data | val_in_late),
					self.enc_ctr.eq(self.rp_data[sx_ctr_offset:sx_ctr_offset+5] + ssss_late[0:4]),
				]

		return m

class Encode(Elaboratable):

	def __init__(self, config, constraints):

		#config assertions
		assert config['bit_depth'] >= 2 and config['bit_depth'] <= 16
		assert config['pixels_per_cycle'] >= 1

		#save needed configs
		self.bd = config['bit_depth']
		self.ps = config['pixels_per_cycle']

		#in
		self.vals_in = Array(Signal(self.bd, name="val_in") for _ in range(self.ps))
		self.ssssx = Array(Signal(5, name="ssss") for _ in range(self.ps))
		
		#out
		self.encs_out = Array(Signal(min(16+self.bd, 31), name="enc_out") for _ in range(self.ps))
		self.encs_ctr = Array(Signal(5, name="enc_ctr") for _ in range(self.ps))

		#valid in & out
		self.valid_in = Signal(1)
		self.valid_out = Signal(1)

		#end in & out
		self.end_in = Signal(1)
		self.end_out = Signal(1)

		self.mem = Memory(self.bd+21, self.bd+1, init_huff_table(self.bd))
		self.read_ports = [self.mem.read_port() for _ in range(self.ps)]

		self.pixels = [SingleEncoder(config, constraints) for _ in range(self.ps)]

		self.ios = \
			[enc_out for enc_out in self.encs_out] + \
			[enc_ctr for enc_ctr in self.encs_ctr] + \
			[val_in for val_in in self.vals_in] + \
			[self.valid_in, self.valid_out] + \
			[ssss for ssss in self.ssssx] + \
			[self.end_in, self.end_out]

	def elaborate(self, platform):

		m = Module()

		m.submodules += self.pixels
		m.submodules += self.read_ports

		for pixel, val_in, enc_out, enc_ctr, ssss, read_port in zip(self.pixels, self.vals_in, self.encs_out, self.encs_ctr, self.ssssx, self.read_ports):
			m.d.comb += [
				pixel.val_in.eq(val_in),
				pixel.end_in.eq(self.end_in),
				pixel.valid_in.eq(self.valid_in),
				pixel.ssss.eq(ssss),
				read_port.addr.eq(pixel.rp_addr),
				pixel.rp_data.eq(read_port.data),
				enc_out.eq(pixel.enc_out),
				enc_ctr.eq(pixel.enc_ctr),
			]

		#if valid data
		m.d.comb += self.valid_out.eq(self.pixels[0].valid_out)
		m.d.comb += self.end_out.eq(self.pixels[0].end_out)

		return m

if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 1,
	}
	e = Encode(config, constraints.Constraints())
	main(e, ports=e.ios)