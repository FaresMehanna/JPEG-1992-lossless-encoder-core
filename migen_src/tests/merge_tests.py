from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import encoder
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from merge import *
import constraints

def merge_test_1(m):
	vcdf = open(parentdir + "/../simulations/merge_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:
		def testbench():

			# input 1
			yield m.encs_in[0].eq(0b11001111)
			yield m.encs_in_ctr[0].eq(8)

			yield m.encs_in[1].eq(0b0)
			yield m.encs_in_ctr[1].eq(1)

			yield m.encs_in[2].eq(0b1010101010101010101011010101010)
			yield m.encs_in_ctr[2].eq(31)

			yield m.encs_in[3].eq(0b000011110)
			yield m.encs_in_ctr[3].eq(9)

			yield m.valid_in.eq(1)

			yield

			assert 0 == (yield m.valid_out)

			#input 2
			yield m.encs_in[0].eq(0b1100)
			yield m.encs_in_ctr[0].eq(4)

			yield m.encs_in[1].eq(0b00000)
			yield m.encs_in_ctr[1].eq(5)

			yield m.encs_in[2].eq(0b10)
			yield m.encs_in_ctr[2].eq(2)

			yield m.encs_in[3].eq(0b0)
			yield m.encs_in_ctr[3].eq(1)

			yield m.valid_in.eq(1)

			yield

			# input 3
			yield m.encs_in[0].eq(0b1011001101101111000101010101011)
			yield m.encs_in_ctr[0].eq(31)

			yield m.encs_in[1].eq(0b0000111110101101010111111110100)
			yield m.encs_in_ctr[1].eq(31)

			yield m.encs_in[2].eq(0b1010101010101010101011010101010)
			yield m.encs_in_ctr[2].eq(31)

			yield m.encs_in[3].eq(0b0000111100010010110101010101010)
			yield m.encs_in_ctr[3].eq(31)

			yield m.valid_in.eq(1)
			assert 0 == (yield m.valid_out)

			yield

			#validate test 1
			assert 1 == (yield m.valid_out)
			assert 0b1100111101010101010101010101011010101010000011110 == (yield m.enc_out)
			assert 49 == (yield m.enc_out_ctr)

			yield m.valid_in.eq(0)

			yield

			#validate test 2
			assert 1 == (yield m.valid_out)
			assert 0b110000000100 == (yield m.enc_out)
			assert 12 == (yield m.enc_out_ctr)

			yield

			#validate test 3
			assert 1 == (yield m.valid_out)
			assert 0b1011001101101111000101010101011000011111010110101011111111010010101010101010101010110101010100000111100010010110101010101010 == (yield m.enc_out)
			assert 124 == (yield m.enc_out_ctr)

			yield

			assert 0 == (yield m.valid_out)

			print("merge_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 4,
	}
	m = Merge(config, constraints.Constraints())
	merge_test_1(m)
	main(m, ports=m.ios)