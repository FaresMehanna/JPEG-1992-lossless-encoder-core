from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import difference
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from difference import *
import constraints

def diff_test_1(m):
	vcdf = open(parentdir + "/../simulations/diff_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():

			#input 1
			yield m.pixels_in[0].eq(100)
			yield m.pixels_in[1].eq(1000)
			yield m.pixels_in[2].eq(500)
			yield m.pixels_in[3].eq(900)
			yield m.predics_in[0].eq(100)
			yield m.predics_in[1].eq(1000)
			yield m.predics_in[2].eq(500)
			yield m.predics_in[3].eq(900)
			yield m.valid_in.eq(1)

			yield

			assert 0 == (yield m.valid_out)

			#input 2
			yield m.pixels_in[0].eq(200)
			yield m.pixels_in[1].eq(2000)
			yield m.pixels_in[2].eq(700)
			yield m.pixels_in[3].eq(800)
			yield m.predics_in[0].eq(100)
			yield m.predics_in[1].eq(1000)
			yield m.predics_in[2].eq(500)
			yield m.predics_in[3].eq(900)
			yield m.valid_in.eq(1)

			yield

			#test input 1
			assert 0 == (yield m.vals_out[0])
			assert 0 == (yield m.vals_out[1])
			assert 0 == (yield m.vals_out[2])
			assert 0 == (yield m.vals_out[3])
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield

			#test input 2
			assert 100 == (yield m.vals_out[0])
			assert 1000 == (yield m.vals_out[1])
			assert 200 == (yield m.vals_out[2])
			assert 0x1FF9C == (yield m.vals_out[3])
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield

			assert 0 == (yield m.valid_out)
			
			print("diff_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()

if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 4,
	}
	d = Difference(config, constraints.Constraints())
	diff_test_1(d)
	main(d, ports=d.ios)