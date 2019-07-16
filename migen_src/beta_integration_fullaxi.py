from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import beta_integration, address_generator
import axihp_reader, axihp_writer
import b64_b32, b16_b64
import dma_axi_lite
import axihp_fifo

# AXI_Reader -> AXI_FIFO -> B64B32 -> LJ92 -> B16B64 -> AXI_FIFO -> AXI_Writer

class BetaIntegrationFullAxi(Elaboratable):

	def __init__(self):

		# beta core
		self.top = beta_integration.BetaIntegration()

		self.address_gen_read = address_generator.AddressGenerator(0x80)
		self.address_gen_write = address_generator.AddressGenerator(0x80)

		self.axihp_reader = axihp_reader.AxiHPReader(data_w=64)
		self.axihp_writer = axihp_writer.AxiHPWriter(data_w=64)

		self.b64_b32 = b64_b32.B64B32()
		self.b16_b64 = b16_b64.B16B64()

		self.dma_axi_lite = dma_axi_lite.DMAAxiLite()

		self.reader_fifo = axihp_fifo.AxiHPFifo()
		self.writer_fifo = axihp_fifo.AxiHPFifo()

		# reader & writer
		self.ios = \
			self.axihp_reader.axi_ios + \
			self.axihp_writer.axi_ios + \
			self.dma_axi_lite.axi_ios

		# axi lite ports
		if self.top.config['support_axi_lite']:
			self.ios += self.top.integration_3.integration_2.integration_1.core_axi_lite.axi_ios


	def elaborate(self, platform):

		m = Module()

		m.submodules.top = top = self.top

		m.submodules.address_gen_read = address_gen_read = self.address_gen_read
		m.submodules.address_gen_write = address_gen_write = self.address_gen_write

		m.submodules.axihp_reader = axihp_reader = self.axihp_reader
		m.submodules.axihp_writer = axihp_writer = self.axihp_writer

		m.submodules.b64_b32 = b64_b32 = self.b64_b32
		m.submodules.b16_b64 = b16_b64 = self.b16_b64
		
		m.submodules.dma_axi_lite = dma_axi_lite = self.dma_axi_lite

		m.submodules.reader_fifo = reader_fifo = self.reader_fifo
		m.submodules.writer_fifo = writer_fifo = self.writer_fifo


		counter_read = Signal(32)
		counter_write = Signal(32)

		read_end = Signal(1)
		write_end = Signal(1)

		with m.If((address_gen_read.address_valid==1)&(axihp_reader.addr_enable==1)):
			m.d.sync += counter_read.eq(counter_read + 1)
			with m.If(counter_read==196609):
				m.d.sync += read_end.eq(1)

		with m.If((address_gen_write.address_valid==1)&(axihp_writer.addr_enable==1)):
			m.d.sync += counter_write.eq(counter_write + 1)
			with m.If(counter_write==131072):
				m.d.sync += write_end.eq(1)

		# dma_axi_lite
		m.d.comb += [
			dma_axi_lite.in1.eq(Cat(b16_b64.end_out, b16_b64.valid_out, writer_fifo.end_out, writer_fifo.valid_out, axihp_writer.data_enable, read_end, write_end, axihp_reader.inactive, axihp_writer.inactive, axihp_writer.writer_error, axihp_reader.reader_error, axihp_writer.writer_active, axihp_reader.reader_active,  axihp_writer.writer_unconf)),
			dma_axi_lite.in2.eq(address_gen_read.address_o),
			dma_axi_lite.in3.eq(address_gen_write.address_o),
			dma_axi_lite.in4.eq(counter_read),
			dma_axi_lite.in5.eq(counter_write),
			dma_axi_lite.in6.eq(top.data_out),
			dma_axi_lite.in7.eq(b16_b64.data_out[0:32]),
			dma_axi_lite.in8.eq(b16_b64.data_out[32:64]),
			dma_axi_lite.in9.eq(b64_b32.data_out),
		]

		# address_gen_read - in
		m.d.comb += [
			address_gen_read.address_latch.eq(axihp_reader.addr_enable),
			address_gen_read.starting_address.eq(dma_axi_lite.read_addr),
		]

		# address_gen_write - in
		m.d.comb += [
			address_gen_write.address_latch.eq(axihp_writer.addr_enable),
			address_gen_write.starting_address.eq(dma_axi_lite.write_addr),
		]
		
		# axihp reader - in
		m.d.comb += [
			axihp_reader.enable.eq((dma_axi_lite.start==0xFFFFFFFF)),
			# data
			axihp_reader.data_full.eq((reader_fifo.writable16==0)),
			# address
			axihp_reader.addr_in.eq(address_gen_read.address_o),
			axihp_reader.addr_empty.eq((address_gen_read.address_valid==0)|(read_end==1)),
		]
		
		# reader_fifo
		m.d.comb += [
			reader_fifo.data_in.eq(axihp_reader.data_out),
			reader_fifo.end_in.eq(0),
			reader_fifo.valid_in.eq(axihp_reader.data_enable),
			reader_fifo.read.eq(b64_b32.o_busy==0),
		]

		# b64_b32 - in
		m.d.comb += [
			b64_b32.data_in.eq(reader_fifo.data_out),
			b64_b32.valid_in.eq(reader_fifo.valid_out),
			b64_b32.i_busy.eq(top.nready),
		]

		# top - in
		m.d.comb += [
			top.valid_in.eq((b64_b32.valid_out==1)),
			top.busy_in.eq(b16_b64.o_busy),
			top.pixel_in1.eq(b64_b32.data_out[0:12]),
			top.pixel_in2.eq(b64_b32.data_out[12:24]),
		]

		# b16_b64 - in
		m.d.comb += [
			b16_b64.data_in.eq(top.data_out),
			b16_b64.valid_in.eq(top.valid_out),
			b16_b64.i_busy.eq(writer_fifo.writable==0),
			b16_b64.end_in.eq(top.end_out),
		]

		# writer_fifo
		m.d.comb += [
			writer_fifo.data_in.eq(b16_b64.data_out),
			writer_fifo.end_in.eq(b16_b64.end_out),
			writer_fifo.valid_in.eq(b16_b64.valid_out),
			writer_fifo.read.eq(axihp_writer.data_enable),
		]

		# axihp writer - in
		m.d.comb += [
			axihp_writer.enable.eq((dma_axi_lite.start==0xFFFFFFFF)),	#keep going till end_out signal
			# data
			axihp_writer.data_in.eq(writer_fifo.data_out),
			axihp_writer.data_empty.eq((writer_fifo.readable16==0)),
			axihp_writer.write_strobe.eq(0xFF),
			# address
			axihp_writer.addr_in.eq(address_gen_write.address_o),
			axihp_writer.addr_empty.eq((address_gen_write.address_valid==0)|(write_end==1)),
		]

		return m


if __name__ == "__main__":
	d = BetaIntegrationFullAxi()
	main(d, ports=d.ios)