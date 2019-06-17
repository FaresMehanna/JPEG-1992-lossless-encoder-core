from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import predictor
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from signals import *


def signals_test_1(m):
	vcdf = open(parentdir + "/../simulations/signals_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:

		def testbench():
			yield

			yield m.height.eq(4)
			yield m.width.eq(12)

			yield m.new_input.eq(1)
			for _ in range(4):

				yield m.new_input.eq(1)
				yield

				assert (yield m.new_row) == 1
				yield m.new_input.eq(1)
				yield

				assert (yield m.new_row) == 0
				yield m.new_input.eq(1)
				yield

			yield m.new_input.eq(0)
			yield
			assert (yield m.end_of_frame) == 1

			print("signals_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()

if __name__ == "__main__":
	config = {
		"pixels_per_cycle": 4,
	}
	p = Signals(config, constraints.Constraints())
	signals_test_1(p)
	main(p, ports=p.ios)