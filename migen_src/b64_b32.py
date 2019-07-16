'''
--------------------
Module: b64_b32
--------------------
Description: 
    - b64_b32 is a module to split 64bits chunk into
    single 32bits chunks.
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
    - this module is optional and can be used with axi_hp[reader/writer]
    and it is not related to LJ92 core.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *
from nmigen.lib.fifo import SyncFIFO

class B64B32(Elaboratable):

    def __init__(self):

        #data in
        self.data_in = Signal(64)

        #data out
        self.data_out = Signal(32)

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

        # fifo module
        fifo64 = SyncFIFO(64, 2)
        fifo32 = SyncFIFO(32, 4)
        m.submodules.fifo32 = fifo32
        m.submodules.fifo64 = fifo64

        # set replace to zero
        m.d.sync += [
            fifo32.replace.eq(0),
            fifo64.replace.eq(0),
        ]

        # register
        reg = Signal(64)

        # FIFO64 input
        with m.FSM() as FSM64:

            # FIFO64 handling
            with m.State("FIFO64_IDLE"):
                m.d.sync += [
                    fifo64.we.eq(0),
                    self.o_busy.eq(0),
                ] 
                m.next = "FIFO64_FILL"

            with m.State("FIFO64_FILL"):
                with m.If(self.valid_in):
                    with m.If(fifo64.writable):
                        m.d.sync += [
                            fifo64.din.eq(self.data_in),
                            fifo64.we.eq(1),
                            self.o_busy.eq(1),
                        ]
                        m.next = "FIFO64_IDLE"
                    with m.Else():
                        m.d.sync += [
                            reg.eq(self.data_in),
                            self.o_busy.eq(1),
                        ]
                        m.next = "HANDLE_REG"

            with m.State("HANDLE_REG"):
                with m.If(fifo64.writable):
                    m.d.sync += [
                        fifo64.din.eq(reg),
                        fifo64.we.eq(1),
                    ]
                    m.next = "FIFO64_IDLE"

        buff = Signal(32)

        # FIFO64 to FIFO32 conversion
        with m.FSM() as FSM64_TO_FSM32:
            
            with m.State("PART1"):
                with m.If((fifo32.writable==1)&(fifo64.readable==1)):
                    m.d.sync += [
                        fifo32.din.eq(fifo64.dout[32:64]),
                        buff.eq(fifo64.dout[0:32]),
                        fifo32.we.eq(1),
                        fifo64.re.eq(1),
                    ]
                    m.next = "PART2"
                with m.Elif(fifo32.writable):
                    m.d.sync += fifo32.we.eq(0)

            with m.State("PART2"):
                m.d.sync += fifo64.re.eq(0)
                with m.If(fifo32.writable):
                    m.d.sync += fifo32.din.eq(buff)
                    m.next = "PART1"

        m.d.comb += [
            self.valid_out.eq(fifo32.readable),
            self.data_out.eq(fifo32.dout),
            fifo32.re.eq(self.i_busy==0),
        ]

        return m

if __name__ == "__main__":
    d = B64B32()
    main(d, ports=d.ios)