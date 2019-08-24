from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import difference
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from markers import *

def markers_test_1(m):
	vcdf = open(parentdir + "/../simulations/markers_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():

			for _ in range(10):
				yield

			yield m.data_in.eq(0x123)
			yield m.valid_in.eq(1)

			for _ in range(20):
				# print((yield m.data_out))
				# print((yield m.valid_out))
				# print("")
				yield

			yield m.end_in.eq(1)

			# print(" ---------- ")
			
			for _ in range(20):
				# print((yield m.data_out))
				# print((yield m.valid_out))
				# print((yield m.end_out))
				# print("")
				yield

			print("markers_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()

if __name__ == "__main__":
	d = Markers()
	markers_test_1(d)
	main(d, ports=d.ios)