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


def normalize_test_1(m):
	vcdf = open(parentdir + "/../simulations/normalize_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:
		def testbench():

			#input 1
			yield m.val_in1.eq(0)
			yield m.val_in2.eq(1)
			yield m.val_in3.eq(2)
			yield m.val_in4.eq(3)
			yield m.valid_in.eq(1)

			yield
			
			assert 0 == (yield m.valid_out)

			#input 2
			yield m.val_in1.eq(-1)
			yield m.val_in2.eq(-2)
			yield m.val_in3.eq(-3)
			yield m.val_in4.eq(-4)
			yield m.valid_in.eq(1)

			yield
			
			#test input 1
			assert 0 == (yield m.val_out1)
			assert 1 == (yield m.val_out2)
			assert 2 == (yield m.val_out3)
			assert 3 == (yield m.val_out4)
			assert 0 == (yield m.ssss1)
			assert 1 == (yield m.ssss2)
			assert 2 == (yield m.ssss3)
			assert 2 == (yield m.ssss4)
			assert 1 == (yield m.valid_out)

			#input 3
			yield m.val_in1.eq(10)
			yield m.val_in2.eq(200)
			yield m.val_in3.eq(3000)
			yield m.val_in4.eq(65535)
			yield m.valid_in.eq(1)

			yield

			#test input 2
			assert 0 == (yield m.val_out1)
			assert 1 == (yield m.val_out2)
			assert 0 == (yield m.val_out3)
			assert 3 == (yield m.val_out4)
			assert 1 == (yield m.ssss1)
			assert 2 == (yield m.ssss2)
			assert 2 == (yield m.ssss3)
			assert 3 == (yield m.ssss4)
			assert 1 == (yield m.valid_out)

			#input 4
			yield m.val_in1.eq(-10)
			yield m.val_in2.eq(-200)
			yield m.val_in3.eq(-3000)
			yield m.val_in4.eq(-65535)
			yield m.valid_in.eq(1)

			yield

			#test input 3
			assert 10 == (yield m.val_out1)
			assert 200 == (yield m.val_out2)
			assert 3000 == (yield m.val_out3)
			assert 65535 == (yield m.val_out4)
			assert 4 == (yield m.ssss1)
			assert 8 == (yield m.ssss2)
			assert 12 == (yield m.ssss3)
			assert 16 == (yield m.ssss4)
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield

			#test input 4
			assert 5 == (yield m.val_out1)
			assert 55 == (yield m.val_out2)
			assert 1095 == (yield m.val_out3)
			assert 0 == (yield m.val_out4)
			assert 4 == (yield m.ssss1)
			assert 8 == (yield m.ssss2)
			assert 12 == (yield m.ssss3)
			assert 16 == (yield m.ssss4)
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield 

			assert 0 == (yield m.valid_out)



			print("normalize_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()


if __name__ == "__main__":
	n = Normalize()
	normalize_test_1(n)
	main(n, ports=n.ios)