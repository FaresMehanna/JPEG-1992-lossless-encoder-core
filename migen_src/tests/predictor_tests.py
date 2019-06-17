from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import predictor
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from predictor_p1_c4_px4 import *
import constraints

def predictor_test_1(m):
	vcdf = open(parentdir + "/../simulations/predictor_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():

			yield m.pixels_in[0].eq(100)
			yield m.pixels_in[1].eq(1000)
			yield m.pixels_in[2].eq(500)
			yield m.pixels_in[3].eq(900)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(1)
			
			yield

			yield m.pixels_in[0].eq(200)
			yield m.pixels_in[1].eq(2000)
			yield m.pixels_in[2].eq(700)
			yield m.pixels_in[3].eq(800)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(0)

			yield

			st = 2**(12-1)

			assert 100 == (yield m.pixels_out[0])
			assert 1000 == (yield m.pixels_out[1])
			assert 500 == (yield m.pixels_out[2])
			assert 900 == (yield m.pixels_out[3])
			assert st == (yield m.predics_out[0])
			assert st == (yield m.predics_out[1])
			assert st == (yield m.predics_out[2])
			assert st == (yield m.predics_out[3])
			assert 1 == (yield m.valid_out)

			yield m.pixels_in[0].eq(300)
			yield m.pixels_in[1].eq(3000)
			yield m.pixels_in[2].eq(300)
			yield m.pixels_in[3].eq(350)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(1)

			yield

			assert 200 == (yield m.pixels_out[0])
			assert 2000 == (yield m.pixels_out[1])
			assert 700 == (yield m.pixels_out[2])
			assert 800 == (yield m.pixels_out[3])
			assert 100 == (yield m.predics_out[0])
			assert 1000 == (yield m.predics_out[1])
			assert 500 == (yield m.predics_out[2])
			assert 900 == (yield m.predics_out[3])
			assert 1 == (yield m.valid_out)

			yield m.pixels_in[0].eq(700)
			yield m.pixels_in[1].eq(3955)
			yield m.pixels_in[2].eq(700)
			yield m.pixels_in[3].eq(750)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(0)

			yield

			assert 300 == (yield m.pixels_out[0])
			assert 3000 == (yield m.pixels_out[1])
			assert 300 == (yield m.pixels_out[2])
			assert 350 == (yield m.pixels_out[3])
			assert 100 == (yield m.predics_out[0])
			assert 1000 == (yield m.predics_out[1])
			assert 500 == (yield m.predics_out[2])
			assert 900 == (yield m.predics_out[3])
			assert 1 == (yield m.valid_out)

			yield

			assert 700 == (yield m.pixels_out[0])
			assert 3955 == (yield m.pixels_out[1])
			assert 700 == (yield m.pixels_out[2])
			assert 750 == (yield m.pixels_out[3])
			assert 300 == (yield m.predics_out[0])
			assert 3000 == (yield m.predics_out[1])
			assert 300 == (yield m.predics_out[2])
			assert 350 == (yield m.predics_out[3])
			assert 1 == (yield m.valid_out)
			
			print("predictor_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()

if __name__ == "__main__":
	config = {
		"bit_depth" : 12,
		"pixels_per_cycle": 4,
		"predictor_function": 1,
		"num_of_components": 4,
	}
	p = PredictorP1C4Px4(config, constraints.Constraints())
	predictor_test_1(p)
	main(p, ports=p.ios)