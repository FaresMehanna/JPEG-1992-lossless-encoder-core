'''
--------------------
Module: markers
--------------------
Description: 
    - markers is an optional module that will add header and
    tailer to each frame in the stream.
    the mark is 16 bytes with 0xFF value.
--------------------
Input: 
    - 2 bytes - stream.
--------------------
Output:
    - 2 bytes - [mark - steam - mark].
--------------------
timing:
    - when first valid signal is inputted, there is 8 cycles delay at least to
    output the marker and as well as 8 cycles in the end of the frame.
--------------------
Notes :
    - this module is optional and can be used with or without the 
    header/trailer module.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *

class Markers(Elaboratable):

    def __init__(self):

        #data in
        self.data_in = Signal(16)

        #data out
        self.data_out = Signal(16)

        #signals
        self.valid_in = Signal(1)
        self.valid_out = Signal(1)

        self.end_in = Signal(1)
        self.force_end_in = Signal(1)
        self.end_out = Signal(1)

        self.o_busy = Signal(1) #prev busy
        self.i_busy = Signal(1) #next busy

        self.ios = \
            [self.valid_in, self.valid_out, self.o_busy, self.i_busy] + \
            [self.data_out, self.data_in] + \
            [self.end_in, self.end_out]

    def elaborate(self, platform):

        m = Module()

        # counter register
        counter = Signal(4)

        # default
        m.d.comb += [
            self.o_busy.eq(1),
            self.valid_out.eq(0),
            self.end_out.eq(0),
        ]

        # late_busy_i = Signal(1)
        # late_valid_i = Signal(1)
        # late_end_i = Signal(1)
        # late_data_i = Signal(16)

        end_cond = Signal(1)
        m.d.sync += end_cond.eq((self.i_busy==0)&(self.valid_in==1)&(self.end_in==1))

        # late2_busy_i = Signal(1)
        # late2_valid_i = Signal(1)
        # late2_end_i = Signal(1)

        # m.d.sync += [
        #     late_busy_i.eq(self.i_busy),
        #     late_valid_i.eq(self.valid_in),
        #     late_end_i.eq(self.end_in),
        #     ate_data_i.eq(self.data_in),
        # ]

        # m.d.sync += [
        #     late2_busy_i.eq(late_busy_i),
        #     late2_valid_i.eq(late2_valid_i),
        #     late2_end_i.eq(late2_end_i),
        # ]

        with m.FSM() as fsm:

            with m.State("IDLE"):
                m.d.sync += counter.eq(8)
                with m.If(self.valid_in):
                    m.next = "STARING_MARKER"

            with m.State("STARING_MARKER"):
                # handle output data
                m.d.comb += [
                    self.data_out.eq(0xFFFF),
                    self.valid_out.eq(1),
                ]
                # handle counter
                with m.If(self.i_busy==0):
                    m.d.sync += counter.eq(counter - 1)
                    # handle transition to frame handling
                    with m.If(counter==0):
                        m.d.sync += counter.eq(8)
                        m.d.comb += [
                            self.data_out.eq(0),
                            self.valid_out.eq(0),
                        ]
                        m.next = "FRAME_HANDLING"

            with m.State("ENDING_MARKER"):
                # handle output data
                m.d.comb += [
                    self.data_out.eq(0xFFFF),
                    self.valid_out.eq(1),
                ]
                # handle counter
                with m.If(self.i_busy==0):
                    m.d.sync += counter.eq(counter - 1)
                    # handle end signals
                    with m.If(counter==1):
                        m.d.comb += self.end_out.eq(1)
                        m.next = "DONE_NORMAL"

            with m.State("FORCE_ENDING_MARKER"):
                # handle output data
                m.d.comb += [
                    self.data_out.eq(0xFFFE),
                    self.valid_out.eq(1),
                ]
                # handle counter
                with m.If(self.i_busy==0):
                    m.d.sync += counter.eq(counter - 1)
                    # handle end signals
                    with m.If(counter==1):
                        m.d.comb += self.end_out.eq(1)
                        m.next = "DONE_FORCE"

            with m.State("FRAME_HANDLING"):
                #end detection
                # with m.If((late2_busy_i==0)&(late2_valid_i==1)&(late2_end_i==1)):
                with m.If(end_cond):
                    m.next = "ENDING_MARKER"
                with m.Elif(self.force_end_in):
                    m.next = "FORCE_ENDING_MARKER"
                with m.Else():
                    # m.d.comb += [
                    #     self.data_out.eq(late_data_i),
                    #     self.valid_out.eq(late_valid_i),
                    #     self.o_busy.eq(late_busy_i),
                    # ]
                    m.d.comb += [
                        self.data_out.eq(self.data_in),
                        self.valid_out.eq(self.valid_in),
                        self.o_busy.eq(self.i_busy),
                    ]

            with m.State("DONE_NORMAL"):
                m.d.comb += [
                    self.data_out.eq(0xFFFF),
                    self.valid_out.eq(1),
                    self.end_out.eq(1),
                ]

            with m.State("DONE_FORCE"):
                m.d.comb += [
                    self.data_out.eq(0xFFFE),
                    self.valid_out.eq(1),
                    self.end_out.eq(1),
                ]                

        return m

if __name__ == "__main__":
    d = Markers()
    main(d, ports=d.ios)