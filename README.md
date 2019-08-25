# JPEG 1992 lossless encoder core

Under Apertus Association in Google Summer of Code 2019, I worked in implementing lossless JPEG 1992 core and it’s supporting software.

While raw images provide high quality, raw huge size limit FPS and cause difficulties in transition and storing.

My task was to implement lossless JPEG 1992 core to be placed in Axiom Beta and Axiom Micro FPGAs, the core will compress the sensor data (raw stream) with no loss in quality what so  ever. This will enable higher FPS and/or lower bandwidth.

I have completed the main core that will compress the stream of data, I have also wrote software to control the core and the DMA and wrote several tools to manipulate, generate and analyze raw and lossless files. I have also worked in an open source DMA for the core, and tested open source library that can decode resulting files.

## Informations
 Please check [The Report](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/Report.pdf) for furhter information about: 
- Lossless JPEG, LJ92 In Axiom Cameras
- LJ92 Pipeline, LJ92 Beta/Micro Technical Details
- Core Configurations
- Receiver End
- Sender End
- Receiver Recording Options
- LJ92 FPGA Core Software
- LJ92 Tools and Utilities
- Test Cases & Test Cases Analysis
- Best & Worst Size Cases Analysis
- Performance Analysis
- References & Useful Links


## Tests and simulations
- You can run the tests and simulations by running [run_tests.py](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/run_tests.py).
- You can also test the core on FPGA - the steps as well as the software needed is provided in the [software](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/tree/master/software) folder.


## Use the core
- You can use pre-generated files in [verilog_src](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/tree/master/verilog_src) directory for the current beta/micro configuration.
- You can adjust the core to your prefrences and then run [generate_verilog.py](https://github.com/FaresMehanna/JPEG-1992-lossless-encoder-core/blob/master/generate_verilog.py) to generate the verilog files.