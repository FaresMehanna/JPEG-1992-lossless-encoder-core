from nmigen import *
from nmigen.cli import main
from nmigen.back import *

# From: https://github.com/apertus-open-source-cinema/axiom-beta-firmware/blob/master/peripherals/soc_main/axi3_lite_pkg.vhd

'''
	axi3ml_pkg
'''
# read address - read data
axi3ml_read_in_r = \
	[("arready", 1)] + \
	[("rdata", 32), ("rresp", 2), ("rvalid", 1)]

# read address - read data
axi3ml_read_out_r = \
	[("araddr", 32), ("arprot", 3), ("arvalid", 1)] + \
	[("rready", 1)]

# write address - write data - write response
axi3ml_write_in_r = \
	[("awready", 1)] + \
	[("wready", 1)] + \
	[("bresp", 2), ("bvalid", 1)]

# write address - write data - write response
axi3ml_write_out_r = \
	[("awaddr", 32), ("awprot", 3), ("awvalid", 1)] + \
	[("wdata", 32), ("wstrb", 4), ("wvalid", 1)] + \
	[("bready", 1)]

'''
	axi3sl_pkg
'''
# read address - read data
axi3sl_read_in_r = \
	[("araddr", 32), ("arprot", 3), ("arvalid", 1)] + \
	[("rready", 1)]

# read address - read data
axi3sl_read_out_r = \
	[("arready", 1)] + \
	[("rdata", 64), ("rresp", 2), ("rvalid", 1)]

# write address - write data - write response
axi3sl_write_in_r = \
	[("awaddr", 32), ("awprot", 3), ("awvalid", 1)] + \
	[("wdata", 64), ("wstrb", 8), ("wvalid", 1)] + \
	[("bready", 1)]

# write address - write data - write response
axi3sl_write_out_r = \
	[("awready", 1)] + \
	[("wready", 1)] + \
	[("bresp", 2), ("bvalid", 1)]