# Tools and steps to run the LJ92 core in ZYNQ 7000

## Generate Verilog files

- You can use the generated Verilog file [beta_integration_axistream.v](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/verilog_src/beta_integration_axistream.v)
- Or you can download yosys and nmigen, then run [generate_verilog.py](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/generate_verilog.py).
- This file will run successfully and will overwrite [beta_integration_axistream.v](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/verilog_src/beta_integration_axistream.v).


## Create vivado project

### LJ92 with Xilinx DMA

- Create a project and and initiate ZYNQ PS.
- Connect DMA with the ZYNQ and with the core interface.
- Connect LJ92 AXI Lite to the ZYNQ.
- Make sure DMA configuration allow for a big transfers using the maximum register size.
- Make sure LJ92 reset [rst] signal is connected to active high reset signal.
- Use [xilinx_dma_vivado_1](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/xilinx_dma_sw/xilinx_dma_vivado_1.png) and [xilinx_dma_vivado_2](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/xilinx_dma_sw/xilinx_dma_vivado_2.png) as a reference.
- Synthesize and implement the design, apply the generated ".BIT" file to your ZYNQ.

### LJ92 with custom, open source DMA

- TODO.


## Generate test files

- In order to test the core you will need RAW12 images and their LJ92 counterpart with configuration that matches the encoder configuration.
- To generate LJ92 files, please refer to [RAW-Image-Tools](https://github.com/FaresMehanna/RAW-Image-Tools).
- Clone and build the code with cmake.
- Run /src/build/bin/lj92_eval with single parameter, the RAW12 image, this will export several LJ92 files, currently the core will match the file that end with "_headerless_fix.lj92" - which mean it is header-less file with 0xFF fix applied.


## Test the core

### LJ92 with Xilinx DMA

- Set DMA_BASE, AXI_LITE_BASE - these info from Vivado address tab - and other info if needed in [config.h](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/xilinx_dma_sw/src/config.h) file.
- Compile the code in [src/](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/xilinx_dma_sw/src/) directory.
- Run "xilinx_test" bin file with two parameters, the RAW12 image and LJ92 file in order.

### LJ92 with custom, open source DMA

- TODO.