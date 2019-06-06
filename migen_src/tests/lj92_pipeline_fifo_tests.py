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
from  lj92_pipeline_fifo import *


def lj92_pipeline_fifo_test_1(m):
	vcdf = open(parentdir + "/../simulations/lj92_pipeline_fifo_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:
		def testbench():

			assert (yield m.valid_out) == 0

			yield

			assert (yield m.valid_out) == 0

			# in1
			yield m.enc_in.eq(0x176524619FF)
			yield m.enc_in_ctr.eq(41)
			yield m.in_end.eq(0)
			yield m.valid_in.eq(1)

			yield

			assert (yield m.valid_out) == 0

			# in2
			yield m.enc_in.eq(0xFF23452431FF23452431FF234524318)
			yield m.enc_in_ctr.eq(124)
			yield m.in_end.eq(1)
			yield m.valid_in.eq(1)

			yield
			yield m.valid_in.eq(0)
			yield

			#test input 1
			assert (yield m.enc_out) == 0x176524619FF
			assert (yield m.enc_out_ctr) == 41
			assert (yield m.out_end) == 0
			assert (yield m.valid_out) == 1

			yield m.valid_in.eq(0)
			yield m.latch_output.eq(1)

			yield
			yield m.latch_output.eq(0)
			yield

			#test input 2
			assert (yield m.enc_out) == 0xFF23452431FF23452431FF234524318
			assert (yield m.enc_out_ctr) == 124
			assert (yield m.out_end) == 1
			assert (yield m.valid_out) == 1

			yield m.valid_in.eq(0)
			yield m.latch_output.eq(1)


			yield

			yield m.valid_in.eq(0)
			yield m.latch_output.eq(0)

			yield
			yield

			for _ in range(51):
				yield m.enc_in.eq(0x176524619FF)
				yield m.enc_in_ctr.eq(41)
				yield m.in_end.eq(0)
				yield m.valid_in.eq(1)
				yield

			yield m.valid_in.eq(0)
			yield
			yield

			assert (yield m.close_full) == 1

			yield m.latch_output.eq(1)
			yield
			yield m.latch_output.eq(0)
			yield
			yield
			assert (yield m.close_full) == 0


			print("lj92_pipeline_fifo_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()


if __name__ == "__main__":
	n = LJ92PipelineFifo(100)
	lj92_pipeline_fifo_test_1(n)
	main(n, ports=n.ios)