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
from core_axi_lite import *
import constraints

def core_axi_lite_test_1(m):
	vcdf = open(parentdir + "/../simulations/core_axi_lite_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:
		def testbench():

			yield m.s_axi_ri.rready.eq(1)
			yield m.s_axi_ri.arvalid.eq(1)
			yield m.s_axi_ri.araddr.eq(260)
			yield
			yield m.s_axi_ri.arvalid.eq(0)
			for i in range(10):
				yield

			print("core_axi_lite_test_1: succeeded.")

		sim.add_clock(1e-8, domain="full")
		sim.add_sync_process(testbench())
		sim.run()


if __name__ == "__main__":
	config = {
		"bit_depth" : 12,
		"axi_lite_debug": False,
	}
	n = CoreAxiLite(config, constraints.Constraints())
	core_axi_lite_test_1(n)
	main(n, ports=n.ios)