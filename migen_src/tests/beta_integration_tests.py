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
from beta_integration import *

TEST_NUM = int(4096*2)

def beta_integration_test_1(m, test_file, test_number, stall_in, stall_out):
	print("beta_integration_test_1_"+str(test_number)+": started for " + str(TEST_NUM) + " pixels ")
	print("Input random stall cycles: " + str(stall_in) + "%")
	print("Output random stall cycles: " + str(stall_out) + "%")
	print("Progress: ", end="")
	sys.stdout.flush()
	bytes_list = []

	vcdf = open(parentdir + "/../simulations/beta_integration_test_1_"+str(test_number)+".vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():
			with open(parentdir + test_file, "rb") as f:
				
				byte1 = f.read(1)
				ctr = 0
				old_ctr = -1
				avgbuffconsum = 0
				cycles = 0
				
				# yield m.integration_3.integration_2.integration_1.core_axi_lite.height_width.eq(0x10000c00)
				yield m.integration_3.integration_2.integration_1.core_axi_lite.height_width.eq(0x10000001)
				yield

				while byte1:

					# input logic
					if (yield m.nready) == 0:
						# stall_in% stall cycles
						if random.randint(1, 101) <= stall_in:
							yield m.valid_in.eq(0)
						else:
							byte1 = int.from_bytes(byte1, byteorder='big')
							byte2 = int.from_bytes(f.read(1), byteorder='big')
							byte3 = int.from_bytes(f.read(1), byteorder='big')

							pix1 = (byte1<<4) | ((byte2 & 0xF0)>>4)
							pix2 = ((byte2 & 0x0F)<<8) | byte3
							ctr += 2

							yield m.pixel_in1.eq(pix1)
							yield m.pixel_in2.eq(pix2)
							yield m.valid_in.eq(1)

							byte1 = f.read(1)
					
					# get data if valid
					NUM_BYTES = int(len(m.data_out)/8)			
					if ((yield m.valid_out) == 1) and ((yield m.busy_in) == 0):
						for i in range(1, (NUM_BYTES+1)):
							bytes_list.append(((yield m.data_out) >> ((NUM_BYTES*8)-i*8)) & 0xFF)
					#output logic - stall_out% stall cycles
					if random.randint(1, 101) <= stall_out:
						yield m.busy_in.eq(1)
					else:
						yield m.busy_in.eq(0)

					# cycles
					cycles += 1

					#average buff consumption
					avgbuffconsum += (yield m.integration_3.vbits_to_cbits.input_handler.buff_consum)
					
					yield

					if ctr % 1000 == 0 and ctr != old_ctr:
						if ctr % 100000 == 0:
							print(ctr/1000, end="")
						elif ctr % 10000 == 0:
							print(ctr/1000, end="")
						else:
							print(".", end="")
						old_ctr = ctr
						sys.stdout.flush()
					
					if ctr >= TEST_NUM:
						yield m.valid_in.eq(0)
						for i in range(5000):
							yield
						print("\nCycles: " + str(cycles))
						print("Avg buff consum: " + str((avgbuffconsum/cycles)))
						break

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()
	org_bin = []
	with open(parentdir + test_file +"_headerless.lj92", "rb") as f:
		for i in range (len(bytes_list)):
			byte = f.read(1)
			un = int.from_bytes(byte, byteorder='big')
			org_bin.append(un)
	print("Number of bytes to be tested is: " + str(len(bytes_list)))
	print("Average pixel bits: " + str((len(bytes_list)/(TEST_NUM*1.5))*12))
	for i in range(len(bytes_list)):
		if bytes_list[i] != org_bin[i]:
			print(org_bin[i])
			print(bytes_list[i])
			print(i)
		assert bytes_list[i] == org_bin[i]
	print("beta_integration_test_1_"+str(test_number)+": succeeded.")

if __name__ == "__main__":
	m = BetaIntegration()
	beta_integration_test_1(m, "/../test_files/portrait-gainx2-offset2047-20ms-01.raw12", 1, 10, 10)
	# print("-----")
	beta_integration_test_1(m, "/../test_files/random.raw12", 8, 1, 1)
	print("-----")
	beta_integration_test_1(m, "/../test_files/props01.raw12", 3, 0, 0)