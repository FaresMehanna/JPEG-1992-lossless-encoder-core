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


def diff_test_1(m):
	vcdf = open(parentdir + "/../simulations/diff_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():

			#input 1
			yield m.pixel_in1.eq(100)
			yield m.pixel_in2.eq(1000)
			yield m.pixel_in3.eq(500)
			yield m.pixel_in4.eq(900)
			yield m.predic_in1.eq(100)
			yield m.predic_in2.eq(1000)
			yield m.predic_in3.eq(500)
			yield m.predic_in4.eq(900)
			yield m.valid_in.eq(1)

			yield

			assert 0 == (yield m.valid_out)

			#input 2
			yield m.pixel_in1.eq(200)
			yield m.pixel_in2.eq(2000)
			yield m.pixel_in3.eq(700)
			yield m.pixel_in4.eq(800)
			yield m.predic_in1.eq(100)
			yield m.predic_in2.eq(1000)
			yield m.predic_in3.eq(500)
			yield m.predic_in4.eq(900)
			yield m.valid_in.eq(1)

			yield

			#test input 1
			assert 0 == (yield m.val_out1)
			assert 0 == (yield m.val_out2)
			assert 0 == (yield m.val_out3)
			assert 0 == (yield m.val_out4)
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield

			#test input 2
			assert 100 == (yield m.val_out1)
			assert 1000 == (yield m.val_out2)
			assert 200 == (yield m.val_out3)
			assert 0x1FF9C == (yield m.val_out4)
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)

			yield

			assert 0 == (yield m.valid_out)
			
			print("diff_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()

if __name__ == "__main__":
	p = Difference()
	diff_test_1(p)
	main(p, ports=p.ios)