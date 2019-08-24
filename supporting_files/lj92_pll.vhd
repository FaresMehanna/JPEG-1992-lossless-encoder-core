----------------------------------------------------------------------------
--  lj92_pll.vhd
--	AXIOM Alpha LJ92 related PLLs
--	Version 1.0
----------------------------------------------------------------------------

library IEEE;
use IEEE.std_logic_1164.ALL;
use IEEE.numeric_std.ALL;

library unisim;
use unisim.VCOMPONENTS.ALL;

entity lj92_pll is
    port (
	ref_clk_in : in std_logic;		-- input clock to FPGA
	--
	pll_reset : in std_logic;		-- PLL reset
	pll_pwrdwn : in std_logic;		-- PLL power down
	pll_locked : out std_logic;		-- PLL locked
	--
	lj92_clk : out std_logic		-- regenerated clock
    );

end entity lj92_pll;


architecture RTL_215MHZ of lj92_pll is

    signal pll_fbout : std_logic;
    signal pll_fbin : std_logic;

    signal pll_lj92_clk : std_logic;

begin
    pll_inst : PLLE2_BASE
    generic map (
	CLKIN1_PERIOD => 10.000,
	CLKFBOUT_MULT => 43,
	CLKOUT0_DIVIDE => 5, -- 215MHz LJ92 clock
	--
	CLKOUT0_PHASE => 0.0,
	--
	DIVCLK_DIVIDE => 4)
    port map (
	CLKIN1 => ref_clk_in,
	CLKFBOUT => pll_fbout,
	CLKFBIN => pll_fbin,
	--
	CLKOUT0 => pll_lj92_clk,

	LOCKED => pll_locked,
	PWRDWN => pll_pwrdwn,
	RST => pll_reset );

    pll_fbin <= pll_fbout; -- internal feedback

    BUFG_lj92_inst : BUFG
	port map (
	    I => pll_lj92_clk,
	    O => lj92_clk );

end RTL_215MHZ;


architecture RTL_200MHZ of lj92_pll is

    signal pll_fbout : std_logic;
    signal pll_fbin : std_logic;

    signal pll_lj92_clk : std_logic;

begin
    pll_inst : PLLE2_BASE
    generic map (
	CLKIN1_PERIOD => 10.000,
	CLKFBOUT_MULT => 16,
	CLKOUT0_DIVIDE => 8, -- 200MHz LJ92 clock
	--
	CLKOUT0_PHASE => 0.0,
	--
	DIVCLK_DIVIDE => 1 )
    port map (
	CLKIN1 => ref_clk_in,
	CLKFBOUT => pll_fbout,
	CLKFBIN => pll_fbin,
	--
	CLKOUT0 => pll_lj92_clk,

	LOCKED => pll_locked,
	PWRDWN => pll_pwrdwn,
	RST => pll_reset );

    pll_fbin <= pll_fbout; -- internal feedback

    BUFG_lj92_inst : BUFG
	port map (
	    I => pll_lj92_clk,
	    O => lj92_clk );

end RTL_200MHZ;


architecture RTL_100MHZ of lj92_pll is

    signal pll_fbout : std_logic;
    signal pll_fbin : std_logic;

    signal pll_lj92_clk : std_logic;

begin
    pll_inst : PLLE2_BASE
    generic map (
	CLKIN1_PERIOD => 10.000,
	CLKFBOUT_MULT => 16,
	CLKOUT0_DIVIDE => 16, -- 100MHz LJ92 clock
	--
	CLKOUT0_PHASE => 0.0,
	--
	DIVCLK_DIVIDE => 1 )
    port map (
	CLKIN1 => ref_clk_in,
	CLKFBOUT => pll_fbout,
	CLKFBIN => pll_fbin,
	--
	CLKOUT0 => pll_lj92_clk,

	LOCKED => pll_locked,
	PWRDWN => pll_pwrdwn,
	RST => pll_reset );

    pll_fbin <= pll_fbout; -- internal feedback

    BUFG_lj92_inst : BUFG
	port map (
	    I => pll_lj92_clk,
	    O => lj92_clk );

end RTL_100MHZ;
