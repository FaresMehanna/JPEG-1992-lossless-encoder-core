from nmigen import *

accessed = False
FULL = ClockDomain("full")
CORE = ClockDomain("sync")

def load_clk(m):

    global accessed
    global FULL
    global CORE
    global clk

    if accessed == False:
        m.domains += CORE
        m.domains += FULL
        # clk domains
        m.d.comb += [
            CORE.clk.eq(FULL.clk),
        ]
        accessed = True