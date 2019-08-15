'''
--------------------
Module: b64_b32_2
--------------------
Description: 
    - b64_b32 is a module to split 64bits chunk into
    two 32bits chunks.
--------------------
Input: 
    - 8 bytes - stream.
--------------------
Output:
    - 4 bytes - stream.
--------------------
timing:
    - This module guarantee that no extra overhead will be 
    introduced.
--------------------
Notes :
    - the module assume that it reads data from FIFO, which mean that
    whenever the valid signal is 1, it will always be one till latching it.
    - the module assume that it write data to AXI stream interface, data only
    transfered when both valid_out=1 and i_busy=0.
    - this module is optional and can be used with axi_hp[reader/writer]
    and it is not related to LJ92 core.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
import clk_domains

class B64B32_2(Elaboratable):

    def __init__(self):

        #data in
        self.data_in = Signal(64)

        #data out
        self.data_out = Signal(24)

        #signals
        self.valid_in = Signal(1)
        self.valid_out = Signal(1)

        self.o_busy = Signal(1, reset=1) #I'm busy
        self.i_busy = Signal(1) #next busy

        self.ios = \
            [self.valid_in, self.valid_out, self.o_busy, self.i_busy] + \
            [self.data_out, self.data_in]

    def elaborate(self, platform):

        m = Module()

        clk_domains.load_clk(m)

        # register to hold data
        reg = Signal(64)
        reg_valid = Signal(1)
        reg_tobe_invalid = Signal(1)
        half_latched = Signal(1)

        # wire o_busy
        wire_obusy = Signal(1)
        m.d.full += self.o_busy.eq(wire_obusy)

        m.d.comb += [
            reg_tobe_invalid.eq(0),
            # ordinary this module is busy and will only go to un-busy
            # if data is present in fifo and the register is empty.
            wire_obusy.eq(1),
        ]

        # valid input data, and there is no data in register or this data
        # will not be needed next cycle, then register the data.
        with m.If((self.valid_in==1) & ((reg_valid==0) | (reg_tobe_invalid==1))):
            m.d.full += [
                reg.eq(self.data_in),
                reg_valid.eq(1),
            ]
            m.d.comb += [
                wire_obusy.eq(0),
            ]

        # if there is valid data in the register but there is no valid data in the
        # output, out the first half and set valid_out to 1.
        with m.If((reg_valid==1) & (self.valid_out==0) & (half_latched==0)):
                m.d.full += [
                    self.data_out.eq(reg[40:64]),
                    self.valid_out.eq(1),
                    half_latched.eq(1),
                ]

        # if and output operation occurred [(self.i_busy==0) and (self.valid_out==1)]
        # and there is valid data in register, then output the correct half.
        with m.If((reg_valid==1) & (self.i_busy==0) & (self.valid_out==1)):
            with m.If(half_latched==1):
                m.d.full += [
                    self.data_out.eq(reg[16:40]),
                    self.valid_out.eq(1),
                    half_latched.eq(0),
                ]
                # in the last half, if there is no valid data ready the the 
                # reg_valid will turn to be 0.
                m.d.comb += [
                    reg_tobe_invalid.eq(1),
                ]
                with m.If(self.valid_in==0):
                    m.d.full += [
                        reg_valid.eq(0),
                    ]
            with m.Else():
                m.d.full += [
                    self.data_out.eq(reg[40:64]),
                    self.valid_out.eq(1),
                    half_latched.eq(1),
                ]

        # if output operation occurred, and the reg_valid remains 0, then
        # valid_out will turn to be 0.
        with m.If((reg_valid==0) & (self.i_busy==0) & (self.valid_out==1)):
            m.d.full += [
                self.valid_out.eq(0),
            ]

        return m

if __name__ == "__main__":
    d = B64B32_2()
    main(d, ports=d.ios)