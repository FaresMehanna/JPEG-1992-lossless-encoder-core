import sys
from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil
import struct
import random

# import encoder
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from integration_1 import *

TEST_NUM = int(4096*1)

def integration_1_test_1(m, test_file, test_number, stall_in):

	print("integration_1_test_1_"+str(test_number)+": started for " + str(TEST_NUM) + " pixels ")
	print("Input random stall cycles: " + str(stall_in) + "%")
	print("Progress: ", end="")
	sys.stdout.flush()
	bytes_list = []

	vcdf = open(parentdir + "/../simulations/integration_1_test_1_"+str(test_number)+".vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():
			with open(parentdir + test_file, "rb") as f:
				
				byte1 = f.read(1)
				ctr = 0
				old_ctr = -1
				total_num = 0
				buffer_bits = 0
				cycles = 0

				while byte1:
					
					# input logic
					# stall_in% stall cycles
					if random.randint(1, 101) <= stall_in:
						yield m.valid_in.eq(0)
					else:
						byte1 = int.from_bytes(byte1, byteorder='big')
						byte2 = int.from_bytes(f.read(1), byteorder='big')
						byte3 = int.from_bytes(f.read(1), byteorder='big')
						byte4 = int.from_bytes(f.read(1), byteorder='big')
						byte5 = int.from_bytes(f.read(1), byteorder='big')
						byte6 = int.from_bytes(f.read(1), byteorder='big')
						ctr += 2
						pix1 = (byte1<<4) | ((byte2 & 0xF0)>>4)
						pix2 = ((byte2 & 0x0F)<<8) | byte3
						pix3 = (byte4<<4) | ((byte5 & 0xF0)>>4)
						pix4 = ((byte5 & 0x0F)<<8) | byte6
						yield m.pixels_in[0].eq(pix1)
						yield m.pixels_in[1].eq(pix2)
						yield m.pixels_in[2].eq(pix3)
						yield m.pixels_in[3].eq(pix4)
						yield m.valid_in.eq(1)
						byte1 = f.read(1)

					#output logic
					if (yield m.valid_out):
						buffer_bits = (buffer_bits << (yield m.enc_out_ctr)) | (yield m.enc_out)
						total_num += (yield m.enc_out_ctr)
						while total_num >= 8:
							bytes_list.append(((buffer_bits>>(total_num-8)) & 0xFF))
							total_num -= 8
						buffer_bits = buffer_bits & ((2**total_num) - 1)

					# cycles
					cycles += 1
					yield

					if ctr % 1000 == 0 and ctr != old_ctr:
						old_ctr = ctr
						print(".", end="")
						sys.stdout.flush()
					
					if ctr >= TEST_NUM:
						print("\nCycles: " + str(cycles))
						break

					

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()

	# validate the results
	org_bin = []
	with open(parentdir + test_file + "_headerless_nofix.lj92", "rb") as f:
		for i in range (len(bytes_list)):
			byte = f.read(1)
			un = int.from_bytes(byte, byteorder='big')
			org_bin.append(un)
	print("Number of bytes to be tested is: " + str(len(bytes_list)))
	print("Average pixel bits: " + str((len(bytes_list)/(TEST_NUM*1.5))*12))
	for i in range(len(bytes_list)):
		assert bytes_list[i] == org_bin[i]
	print("integration_1_test_1_"+str(test_number)+": succeeded.")

if __name__ == "__main__":
	#Integration 1 configuration
	config = {
		"bit_depth" : 12,
		"pixels_per_cycle": 4,
		"predictor_function": 1,
		"num_of_components": 4,
		"pipeline_reg": False,
	}
	cons = constraints.Constraints()
	#object
	m = Integration1(config, cons)
	#tests
	integration_1_test_1(m, "/../test_files/portrait-gainx2-offset2047-20ms-01.raw12", 1, 2)
	print("-----")
	integration_1_test_1(m, "/../test_files/random.raw12", 2, 5)
	print("-----")
	integration_1_test_1(m, "/../test_files/IT8Chart15ms.raw12", 3, 1)