from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import normalizer
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from normalize import *
import constraints

def normalize_test_1(m):
	vcdf = open(parentdir + "/../simulations/normalize_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:
		def testbench():

			#input 1
			yield m.vals_in[0].eq(0)
			yield m.vals_in[1].eq(1)
			yield m.vals_in[2].eq(2)
			yield m.vals_in[3].eq(3)
			yield m.vals_in_mns[0].eq(-1)
			yield m.vals_in_mns[1].eq(0)
			yield m.vals_in_mns[2].eq(1)
			yield m.vals_in_mns[3].eq(2)
			yield m.valid_in.eq(1)

			yield
			
			assert 0 == (yield m.valid_out)

			#input 2
			yield m.vals_in[0].eq(-1)
			yield m.vals_in[1].eq(-2)
			yield m.vals_in[2].eq(-3)
			yield m.vals_in[3].eq(-4)
			yield m.vals_in_mns[0].eq(-2)
			yield m.vals_in_mns[1].eq(-3)
			yield m.vals_in_mns[2].eq(-4)
			yield m.vals_in_mns[3].eq(-5)
			yield m.valid_in.eq(1)

			yield
			
			#test input 1
			assert 0 == (yield m.vals_out[0])
			assert 1 == (yield m.vals_out[1])
			assert 2 == (yield m.vals_out[2])
			assert 3 == (yield m.vals_out[3])
			assert 0 == (yield m.ssssx[0])
			assert 1 == (yield m.ssssx[1])
			assert 2 == (yield m.ssssx[2])
			assert 2 == (yield m.ssssx[3])
			assert 1 == (yield m.valid_out)

			#input 3
			yield m.vals_in[0].eq(10)
			yield m.vals_in[1].eq(200)
			yield m.vals_in[2].eq(3000)
			yield m.vals_in[3].eq(65535)
			yield m.vals_in_mns[0].eq(9)
			yield m.vals_in_mns[1].eq(199)
			yield m.vals_in_mns[2].eq(2999)
			yield m.vals_in_mns[3].eq(65534)
			yield m.valid_in.eq(1)

			yield

			#test input 2
			assert 0 == (yield m.vals_out[0])
			assert 1 == (yield m.vals_out[1])
			assert 0 == (yield m.vals_out[2])
			assert 3 == (yield m.vals_out[3])
			assert 1 == (yield m.ssssx[0])
			assert 2 == (yield m.ssssx[1])
			assert 2 == (yield m.ssssx[2])
			assert 3 == (yield m.ssssx[3])
			assert 1 == (yield m.valid_out)

			#input 4
			yield m.vals_in[0].eq(-10)
			yield m.vals_in[1].eq(-200)
			yield m.vals_in[2].eq(-3000)
			yield m.vals_in[3].eq(-65535)
			yield m.vals_in_mns[0].eq(-11)
			yield m.vals_in_mns[1].eq(-201)
			yield m.vals_in_mns[2].eq(-3001)
			yield m.vals_in_mns[3].eq(-65536)
			yield m.valid_in.eq(1)

			yield

			#test input 3
			assert 10 == (yield m.vals_out[0])
			assert 200 == (yield m.vals_out[1])
			assert 3000 == (yield m.vals_out[2])
			assert 65535 == (yield m.vals_out[3])
			assert 4 == (yield m.ssssx[0])
			assert 8 == (yield m.ssssx[1])
			assert 12 == (yield m.ssssx[2])
			assert 16 == (yield m.ssssx[3])
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield

			#test input 4
			assert 5 == (yield m.vals_out[0])
			assert 55 == (yield m.vals_out[1])
			assert 1095 == (yield m.vals_out[2])
			assert 0 == (yield m.vals_out[3])
			assert 4 == (yield m.ssssx[0])
			assert 8 == (yield m.ssssx[1])
			assert 12 == (yield m.ssssx[2])
			assert 16 == (yield m.ssssx[3])
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield 

			assert 0 == (yield m.valid_out)



			print("normalize_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 4,
	}
	n = Normalize(config, constraints.Constraints())
	normalize_test_1(n)
	main(n, ports=n.ios)