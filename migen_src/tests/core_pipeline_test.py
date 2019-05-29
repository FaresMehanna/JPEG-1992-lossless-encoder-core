import sys
from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import struct

# import encoder
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from  lj92_pipeline import *

TEST_NUM = int(4096*10)

def lj92_pipeline_test_1(m):
	print("lj92_pipeline_test_1: started for " + str(TEST_NUM) + " pixels ", end = "")
	sys.stdout.flush()
	bytes_list = []

	vcdf = open(parentdir + "/../simulations/lj92_pipeline_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():
			with open(parentdir + "/../test_files/portrait-gainx2-offset2047-20ms-01.raw12", "rb") as f:
				
				byte1 = f.read(1)
				ctr = 0
				total_num = 0
				buffer_bits = 0

				while byte1:

					byte1 = int.from_bytes(byte1, byteorder='big')
					byte2 = int.from_bytes(f.read(1), byteorder='big')
					byte3 = int.from_bytes(f.read(1), byteorder='big')
					byte4 = int.from_bytes(f.read(1), byteorder='big')
					byte5 = int.from_bytes(f.read(1), byteorder='big')
					byte6 = int.from_bytes(f.read(1), byteorder='big')
					ctr += 4

					pix1 = (byte1<<4) | ((byte2 & 0xF0)>>4)
					pix2 = ((byte2 & 0x0F)<<8) | byte3
					pix3 = (byte4<<4) | ((byte5 & 0xF0)>>4)
					pix4 = ((byte5 & 0x0F)<<8) | byte6

					yield m.pixel_in1.eq(pix1)
					yield m.pixel_in2.eq(pix2)
					yield m.pixel_in3.eq(pix3)
					yield m.pixel_in4.eq(pix4)
					yield m.valid_in.eq(1)

					yield

					if (yield m.valid_out):
						buffer_bits = (buffer_bits << (yield m.enc_out_ctr)) | (yield m.enc_out)
						total_num += (yield m.enc_out_ctr)
						while total_num >= 8:
							bytes_list.append(((buffer_bits>>(total_num-8)) & 0xFF))
							total_num -= 8
						buffer_bits = buffer_bits & ((2**total_num) - 1)

					if ctr % 1000 == 0:
						print(".", end="")
						sys.stdout.flush()
					
					if ctr % TEST_NUM == 0:
						yield m.valid_in.eq(0)
						yield
						while (yield m.valid_out) == 1:
							buffer_bits = (buffer_bits << (yield m.enc_out_ctr)) | (yield m.enc_out)
							total_num += (yield m.enc_out_ctr)
							while total_num >= 8:
								bytes_list.append(((buffer_bits>>(total_num-8)) & 0xFF))
								total_num -= 8
							buffer_bits = buffer_bits & ((2**total_num) - 1)
							yield
						yield
						break

					byte1 = f.read(1)

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()
		return bytes_list

if __name__ == "__main__":
	m = LJ92Pipeline()
	core_bin = lj92_pipeline_test_1(m)
	org_bin = []

	with open(parentdir + "/../test_files/portrait-gainx2-offset2047-20ms-01.raw12_headerless_nofix.lj92", "rb") as f:
		for i in range (len(core_bin)):
			byte = f.read(1)
			un = int.from_bytes(byte, byteorder='big')
			org_bin.append(un)
	
	print("\nNumber of bytes to be tested is: " + str(len(core_bin)))
	print("Average pixel bits: " + str((len(core_bin)/(TEST_NUM*1.5))*12))

	for i in range(len(core_bin)):
		assert core_bin[i] == org_bin[i]

	print("lj92_pipeline_test_1: succeeded.")
