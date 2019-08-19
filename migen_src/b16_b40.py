'''
--------------------
Module: b16_b40
--------------------
Description: 
    - b16_b40 is a module to combine 2.5x 16bits chunks into
    single 40bits chunk.
--------------------
Input: 
    - 2 bytes - stream.
--------------------
Output:
    - 5 bytes - stream.
--------------------
timing:
    - This module guarantee that no extra overhead will be 
    introduced.
--------------------
Notes :
    - this module is optional and can be used with axi_hp[reader/writer]
    and it is not directly related to LJ92 core.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *

class B16B40(Elaboratable):

    def __init__(self):

        #data in
        self.data_in = Signal(16)

        #data out
        self.data_out = Signal(40)

        #signals
        self.valid_in = Signal(1)
        self.valid_out = Signal(1)

        self.o_busy = Signal(1) #I'm busy
        self.i_busy = Signal(1) #next busy

        self.ios = \
            [self.valid_in, self.valid_out, self.o_busy, self.i_busy] + \
            [self.data_out, self.data_in]

    def elaborate(self, platform):

        m = Module()

        # buffer 1 data
        buffer1 = Signal(40)
        buffer1_valid = Signal(1)

        # buffer 2 data
        buffer2 = Signal(40)
        buffer2_valid = Signal(1)

        # which buffer currently used
        buff_chs = Signal(1)

        # is valid correct?
        is_valid = Signal(1)
        m.d.comb += is_valid.eq(1)

        # buffer for the 0.5*input size
        temp_8 = Signal(1)

        # handle data_out
        with m.If(buff_chs==0):
            m.d.comb += self.data_out.eq(buffer1)
        with m.Else():
            m.d.comb += self.data_out.eq(buffer2)

        # handle valid_out
        m.d.sync += self.valid_out.eq(((buffer1_valid==1)|(buffer2_valid==1))&(is_valid==1))

        # out transaction happened - switch buffers!
        with m.If((self.valid_out==1)&(self.i_busy==0)):
            m.d.comb += is_valid.eq(0)
            m.d.sync += buff_chs.eq(buff_chs==0)
            with m.If(buff_chs==0):
                m.d.sync += buffer1_valid.eq(0)
            with m.If(buff_chs==1):
                m.d.sync += buffer2_valid.eq(0)

        # fsm
        with m.FSM() as fsm:

            # buffer 1 handling
            with m.State("BUFF1_IDLE"):
                # wait until buffer1 data become invalid
                with m.If(buffer1_valid==0):
                    m.d.sync += self.o_busy.eq(0)
                    m.next = "BUFF1_FILL_1"

            with m.State("BUFF1_FILL_1"):
                with m.If(self.valid_in):
                    m.d.sync += buffer1[24:40].eq(self.data_in)
                    m.next = "BUFF1_FILL_2"

            with m.State("BUFF1_FILL_2"):
                with m.If(self.valid_in):
                    m.d.sync += buffer1[8:24].eq(self.data_in)
                    m.next = "BUFF1_FILL_3"

            with m.State("BUFF1_FILL_3"):
                with m.If(self.valid_in):
                    m.d.sync += [
                        buffer1[0:8].eq(self.data_in[8:16]),
                        buffer1_valid.eq(1),
                    ]
                    # is buffer2 data is invalid?
                    # if invalid then start filling
                    with m.If(buffer2_valid==0):
                        m.d.sync += buffer2[32:40].eq(self.data_in[0:8])
                        m.next = "BUFF2_FILL_1"
                    # if data still valid to wait until invalid
                    with m.Else():
                        m.d.sync += [
                            temp_8.eq(self.data_in[0:8]),
                            self.o_busy.eq(1),
                        ]
                        m.next = "BUFF2_IDLE"


            # buffer 2 handling
            with m.State("BUFF2_IDLE"):
                # wait until buffer2 data become invalid
                with m.If(buffer2_valid==0):
                    m.d.sync += buffer2[32:40].eq(temp_8)
                    m.d.sync += self.o_busy.eq(0)
                    m.next = "BUFF2_FILL_1"

            with m.State("BUFF2_FILL_1"):
                with m.If(self.valid_in):
                    m.d.sync += buffer2[16:32].eq(self.data_in)
                    m.next = "BUFF2_FILL_2"

            with m.State("BUFF2_FILL_2"):
                with m.If(self.valid_in):
                    m.d.sync += [
                        buffer2[0:16].eq(self.data_in),
                        buffer2_valid.eq(1),
                    ]
                    # is buffer1 data is invalid?
                    # if invalid then start filling
                    with m.If(buffer1_valid==0):
                        m.next = "BUFF1_FILL_1"
                    # if data still valid to wait until invalid
                    with m.Else():
                        m.d.sync += self.o_busy.eq(1)
                        m.next = "BUFF1_IDLE"
        return m

if __name__ == "__main__":
    d = B16B40()
    main(d, ports=d.ios)