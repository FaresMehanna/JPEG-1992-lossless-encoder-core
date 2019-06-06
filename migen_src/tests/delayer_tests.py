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
from delayer import *

#delay steps
DELAY = 8

def delayer_test_1(m):
	vcdf = open(parentdir + "/../simulations/delayer_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:
		def testbench():

			yield m.in_sig.eq(1)
			yield

			for _ in range(DELAY):
				assert (yield m.out_sig) == 0
				yield

			for _ in range(10):
				assert (yield m.out_sig) == 1
				yield
				
			print("delayer_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()


if __name__ == "__main__":
	n = Delayer(DELAY)
	delayer_test_1(n)
	main(n, ports=n.ios)