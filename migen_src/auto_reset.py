'''
--------------------
Module: auto_reset
--------------------
Description: 
    - auto_reset is to auto-reset the core after every frame fully
    encoded and transfered.
--------------------
Input: 
    - output signals from the core that indicate frame ending
    and transfers.
--------------------
Output:
    - reset signal.
--------------------
timing:
    - Once the last transfer occurs, the reset signal will be 1 for exactly
    one cycle.
--------------------
Notes :
    - this module is optional.
--------------------
'''

from nmigen import *
from nmigen.cli import main
from nmigen.back import *

class AutoReset(Elaboratable):

    def __init__(self):

        #end signal from the core
        self.end_in = Signal(1)

        # hand shake 1 from the core
        self.hs1_in = Signal(1)

        # hand shake 2 from the receiver
        self.hs2_in = Signal(1)

        # reset signal for the core
        self.reset_out = Signal(1)

        self.ios = \
            [self.end_in, self.hs1_in, self.hs2_in, self.reset_out]

    def elaborate(self, platform):

        m = Module()

        # this signal will reset this module as well, so it will get back to
        # 0 in the next cycle.
        with m.If((self.hs1_in==1)&(self.hs2_in==1)&(self.end_in==1)):
            m.d.sync += self.reset_out.eq(1)
        
        return m

if __name__ == "__main__":
    d = AutoReset()
    main(d, ports=d.ios)