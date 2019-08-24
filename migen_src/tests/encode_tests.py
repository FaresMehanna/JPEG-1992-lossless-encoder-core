from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from math import log, ceil

# import encoder
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from encode import *
import constraints

def encode_test_1(m):
	vcdf = open(parentdir + "/../simulations/encode_test_1.vcd", "w")
	with pysim.Simulator(m, vcd_file=vcdf) as sim:
		def testbench():

			# get current ssss values for testing
			ssss = get_ssss()

			#input 1
			input1 = [(0,0),(1,1),(2,2),(3,2)]
			yield m.vals_in[0].eq(input1[0][0])
			yield m.ssssx[0].eq(input1[0][1])
			yield m.vals_in[1].eq(input1[1][0])
			yield m.ssssx[1].eq(input1[1][1])
			yield m.vals_in[2].eq(input1[2][0])
			yield m.ssssx[2].eq(input1[2][1])
			yield m.vals_in[3].eq(input1[3][0])
			yield m.ssssx[3].eq(input1[3][1])
			yield m.valid_in.eq(1)

			yield
			
			assert 0 == (yield m.valid_out)

			#input 2
			input2 = [(0,1),(1,2),(0,2),(3,3)]
			yield m.vals_in[0].eq(input2[0][0])
			yield m.ssssx[0].eq(input2[0][1])
			yield m.vals_in[1].eq(input2[1][0])
			yield m.ssssx[1].eq(input2[1][1])
			yield m.vals_in[2].eq(input2[2][0])
			yield m.ssssx[2].eq(input2[2][1])
			yield m.vals_in[3].eq(input2[3][0])
			yield m.ssssx[3].eq(input2[3][1])
			yield m.valid_in.eq(1)

			yield

			assert 0 == (yield m.valid_out)

			#input 3
			input3 = [(10,4),(200,8),(3000,12),(65535,16)]
			yield m.vals_in[0].eq(input3[0][0])
			yield m.ssssx[0].eq(input3[0][1])
			yield m.vals_in[1].eq(input3[1][0])
			yield m.ssssx[1].eq(input3[1][1])
			yield m.vals_in[2].eq(input3[2][0])
			yield m.ssssx[2].eq(input3[2][1])
			yield m.vals_in[3].eq(input3[3][0])
			yield m.ssssx[3].eq(input3[3][1])
			yield m.valid_in.eq(1)			

			yield

			#test input 1
			enc_ctrs = [(yield m.encs_ctr[0]), (yield m.encs_ctr[1]), (yield m.encs_ctr[2]), (yield m.encs_ctr[3])]
			enc_outs = [(yield m.encs_out[0]), (yield m.encs_out[1]), (yield m.encs_out[2]), (yield m.encs_out[3])]
			ins = input1
			for l in range (0, 4):
				assert ssss[ins[l][1]][1] + ins[l][1] == enc_ctrs[l]
				assert ((ssss[ins[l][1]][0] << ins[l][1]) | ins[l][0]) == enc_outs[l]
			assert 1 == (yield m.valid_out)

			#input 4
			input4 = [(5,4),(55,8),(1095,12),(0,16)]
			yield m.vals_in[0].eq(5)
			yield m.ssssx[0].eq(4)
			yield m.vals_in[1].eq(55)
			yield m.ssssx[1].eq(8)
			yield m.vals_in[2].eq(1095)
			yield m.ssssx[2].eq(12)
			yield m.vals_in[3].eq(0)
			yield m.ssssx[3].eq(16)
			yield m.valid_in.eq(1)


			yield

			#test input 2
			enc_ctrs = [(yield m.encs_ctr[0]), (yield m.encs_ctr[1]), (yield m.encs_ctr[2]), (yield m.encs_ctr[3])]
			enc_outs = [(yield m.encs_out[0]), (yield m.encs_out[1]), (yield m.encs_out[2]), (yield m.encs_out[3])]
			ins = input2
			for l in range (0, 4):
				assert ((ssss[ins[l][1]][0] << ins[l][1]) | ins[l][0]) == enc_outs[l]
				assert ssss[ins[l][1]][1] + ins[l][1] == enc_ctrs[l]
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)
			yield

			#test input 3
			enc_ctrs = [(yield m.encs_ctr[0]), (yield m.encs_ctr[1]), (yield m.encs_ctr[2]), (yield m.encs_ctr[3])]
			enc_outs = [(yield m.encs_out[0]), (yield m.encs_out[1]), (yield m.encs_out[2]), (yield m.encs_out[3])]
			ins = input3
			for l in range (0, 3):
				assert ((ssss[ins[l][1]][0] << ins[l][1]) | ins[l][0]) == enc_outs[l]
				assert ssss[ins[l][1]][1] + ins[l][1] == enc_ctrs[l]
			assert ssss[ins[3][1]][0] == enc_outs[3]
			assert ssss[ins[3][1]][1] == enc_ctrs[3]
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)
			yield 

			#test input 4
			enc_ctrs = [(yield m.encs_ctr[0]), (yield m.encs_ctr[1]), (yield m.encs_ctr[2]), (yield m.encs_ctr[3])]
			enc_outs = [(yield m.encs_out[0]), (yield m.encs_out[1]), (yield m.encs_out[2]), (yield m.encs_out[3])]
			ins = input4
			for l in range (0, 3):
				assert ((ssss[ins[l][1]][0] << ins[l][1]) | ins[l][0]) == enc_outs[l]
				assert ssss[ins[l][1]][1] + ins[l][1] == enc_ctrs[l]
			assert ssss[ins[3][1]][0] == enc_outs[3]
			assert ssss[ins[3][1]][1] == enc_ctrs[3]
			assert 1 == (yield m.valid_out)

			yield m.valid_in.eq(0)
			yield 

			assert 0 == (yield m.valid_out)


			print("encode_test_1: succeeded.")

		sim.add_clock(1e-8)
		sim.add_sync_process(testbench())
		sim.run()


if __name__ == "__main__":
	config = {
		"bit_depth" : 16,
		"pixels_per_cycle": 4,
		"support_axi_lite": False,
	}
	e = Encode(config, constraints.Constraints())
	encode_test_1(e)
	main(e, ports=e.ios)