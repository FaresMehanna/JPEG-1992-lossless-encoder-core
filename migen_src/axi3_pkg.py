from nmigen import *
from nmigen.cli import main
from nmigen.back import *

# From: https://github.com/apertus-open-source-cinema/axiom-beta-firmware/blob/master/peripherals/soc_main/axi3_pkg.vhd

'''
	axi3m_pkg
'''
# read address - read data
axi3m_read_in_r = \
	[("arready", 1)] + \
	[("rid", 12), ("rdata", 32), ("rlast", 1), ("rresp", 2), ("rvalid", 1)]

# read address - read data
axi3m_read_out_r = \
	[("arid", 12), ("araddr", 32), ("arburst", 2), ("arlen", 4), ("arsize", 2), ("arprot", 3), ("arvalid", 1)] + \
	[("rready", 1)]

# write address - write data - write response
axi3m_write_in_r = \
	[("awready", 1)] + \
	[("wready", 1)] + \
	[("bid", 12), ("bresp", 2), ("bvalid", 1)]

# write address - write data - write response
axi3m_write_out_r = \
	[("awid", 12), ("awaddr", 32), ("awburst", 2), ("awlen", 4), ("awsize", 2), ("awprot", 3), ("awvalid", 1)] + \
	[("wid", 12), ("wdata", 32), ("wstrb", 4), ("wlast", 1), ("wvalid", 1)] + \
	[("bready", 1)]

'''
	axi3s_pkg
'''
# read address - read data
axi3s_read_in_r = \
	[("arid", 6), ("araddr", 32), ("arburst", 2), ("arlen", 4), ("arsize", 2), ("arprot", 3), ("arvalid", 1)] + \
	[("rready", 1)]

# read address - read data
axi3s_read_out_r = \
	[("arready", 1), ("racount", 1)] + \
	[("rid", 6), ("rdata", 64), ("rlast", 1), ("rresp", 2), ("rvalid", 1), ("rcount", 8)]

# write address - write data - write response
axi3s_write_in_r = \
	[("awid", 6), ("awaddr", 32), ("awburst", 2), ("awlen", 4), ("awsize", 2), ("awprot", 3), ("awvalid", 1)] + \
	[("wid", 6), ("wdata", 64), ("wstrb", 8), ("wlast", 1), ("wvalid", 1)] + \
	[("bready", 1)]

# write address - write data - write response
axi3s_write_out_r = \
	[("awready", 1), ("wacount", 6)] + \
	[("wready", 1), ("wcount", 8)] + \
	[("bid", 6), ("bresp", 2), ("bvalid", 1)]