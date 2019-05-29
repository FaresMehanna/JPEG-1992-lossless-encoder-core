from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import predictor
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from predictor import *


def predictor_test_1(m):
	vcdf = open(parentdir + "/../simulations/predictor_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():

			yield m.pixel_in1.eq(100)
			yield m.pixel_in2.eq(1000)
			yield m.pixel_in3.eq(500)
			yield m.pixel_in4.eq(900)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(1)
			
			yield

			yield m.pixel_in1.eq(200)
			yield m.pixel_in2.eq(2000)
			yield m.pixel_in3.eq(700)
			yield m.pixel_in4.eq(800)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(0)

			yield

			st = 2**(BIT_DEPTH-1)

			assert 100 == (yield m.pixel_out1)
			assert 1000 == (yield m.pixel_out2)
			assert 500 == (yield m.pixel_out3)
			assert 900 == (yield m.pixel_out4)
			assert st == (yield m.predic_out1)
			assert st == (yield m.predic_out2)
			assert st == (yield m.predic_out3)
			assert st == (yield m.predic_out4)
			assert 1 == (yield m.valid_out)

			yield m.pixel_in1.eq(300)
			yield m.pixel_in2.eq(3000)
			yield m.pixel_in3.eq(300)
			yield m.pixel_in4.eq(350)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(1)

			yield

			assert 200 == (yield m.pixel_out1)
			assert 2000 == (yield m.pixel_out2)
			assert 700 == (yield m.pixel_out3)
			assert 800 == (yield m.pixel_out4)
			assert 100 == (yield m.predic_out1)
			assert 1000 == (yield m.predic_out2)
			assert 500 == (yield m.predic_out3)
			assert 900 == (yield m.predic_out4)
			assert 1 == (yield m.valid_out)

			yield m.pixel_in1.eq(700)
			yield m.pixel_in2.eq(7000)
			yield m.pixel_in3.eq(700)
			yield m.pixel_in4.eq(750)
			yield m.valid_in.eq(1)
			yield m.new_row.eq(0)

			yield

			assert 300 == (yield m.pixel_out1)
			assert 3000 == (yield m.pixel_out2)
			assert 300 == (yield m.pixel_out3)
			assert 350 == (yield m.pixel_out4)
			assert 100 == (yield m.predic_out1)
			assert 1000 == (yield m.predic_out2)
			assert 500 == (yield m.predic_out3)
			assert 900 == (yield m.predic_out4)
			assert 1 == (yield m.valid_out)

			yield

			assert 700 == (yield m.pixel_out1)
			assert 7000 == (yield m.pixel_out2)
			assert 700 == (yield m.pixel_out3)
			assert 750 == (yield m.pixel_out4)
			assert 300 == (yield m.predic_out1)
			assert 3000 == (yield m.predic_out2)
			assert 300 == (yield m.predic_out3)
			assert 350 == (yield m.predic_out4)
			assert 1 == (yield m.valid_out)
			
			print("predictor_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()

if __name__ == "__main__":
	p = Predictor()
	predictor_test_1(p)
	main(p, ports=p.ios)