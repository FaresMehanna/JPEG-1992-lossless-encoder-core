/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(s_axi_wi___awvalid, s_axi_ri___araddr, in1, in2, in3, in4, in5, in6, in7, in8, in9, s_axi_ri___rready, s_axi_wi___awaddr, s_axi_wi___wvalid, s_axi_wi___wdata, s_axi_wi___wstrb, s_axi_wi___bready, rst, clk, read_addr, write_addr, start, s_axi_ro___arready, s_axi_ro___rdata, s_axi_ro___rresp, s_axi_ro___rvalid, s_axi_wo___awready, s_axi_wo___wready, s_axi_wo___bresp, s_axi_wo___bvalid, s_axi_ri___arvalid);
  wire [31:0] \$1 ;
  wire [31:0] \$3 ;
  (* src = "dma_axi_lite.py:110" *)
  reg [31:0] \$next\addr_v ;
  (* src = "dma_axi_lite.py:112" *)
  reg \$next\arready_v ;
  (* src = "dma_axi_lite.py:115" *)
  reg \$next\awready_v ;
  (* src = "dma_axi_lite.py:134" *)
  reg \$next\basic_enable ;
  (* src = "dma_axi_lite.py:135" *)
  reg [3:0] \$next\basic_index ;
  (* src = "dma_axi_lite.py:122" *)
  reg [1:0] \$next\bresp_v ;
  (* src = "dma_axi_lite.py:117" *)
  reg \$next\bvalid_v ;
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg [2:0] \$next\fsm_state ;
  (* src = "dma_axi_lite.py:119" *)
  reg [31:0] \$next\rdata_v ;
  (* src = "dma_axi_lite.py:59" *)
  reg [31:0] \$next\read_addr ;
  (* src = "dma_axi_lite.py:120" *)
  reg [1:0] \$next\rresp_v ;
  (* src = "dma_axi_lite.py:113" *)
  reg \$next\rvalid_v ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg \$next\s_axi_ro___arready ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg [31:0] \$next\s_axi_ro___rdata ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg [1:0] \$next\s_axi_ro___rresp ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg \$next\s_axi_ro___rvalid ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg \$next\s_axi_wo___awready ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg [1:0] \$next\s_axi_wo___bresp ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg \$next\s_axi_wo___bvalid ;
  (* src = "nmigen/hdl/rec.py:84" *)
  reg \$next\s_axi_wo___wready ;
  (* src = "dma_axi_lite.py:63" *)
  reg [31:0] \$next\start ;
  (* src = "dma_axi_lite.py:125" *)
  reg [31:0] \$next\wdata_v ;
  (* src = "dma_axi_lite.py:116" *)
  reg \$next\wready_v ;
  (* src = "dma_axi_lite.py:60" *)
  reg [31:0] \$next\write_addr ;
  (* src = "dma_axi_lite.py:126" *)
  reg [3:0] \$next\wstrb_v ;
  (* init = 32'd0 *)
  (* src = "dma_axi_lite.py:110" *)
  reg [31:0] addr_v = 32'd0;
  (* init = 1'h0 *)
  (* src = "dma_axi_lite.py:112" *)
  reg arready_v = 1'h0;
  (* init = 1'h0 *)
  (* src = "dma_axi_lite.py:115" *)
  reg awready_v = 1'h0;
  (* src = "dma_axi_lite.py:134" *)
  wire basic_enable;
  (* src = "dma_axi_lite.py:135" *)
  wire [3:0] basic_index;
  (* init = 2'h0 *)
  (* src = "dma_axi_lite.py:122" *)
  reg [1:0] bresp_v = 2'h0;
  (* init = 1'h0 *)
  (* src = "dma_axi_lite.py:117" *)
  reg bvalid_v = 1'h0;
  (* src = "nmigen/hdl/ir.py:329" *)
  input clk;
  (* init = 3'h0 *)
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg [2:0] fsm_state = 3'h0;
  (* src = "dma_axi_lite.py:66" *)
  input [31:0] in1;
  (* src = "dma_axi_lite.py:67" *)
  input [31:0] in2;
  (* src = "dma_axi_lite.py:68" *)
  input [31:0] in3;
  (* src = "dma_axi_lite.py:69" *)
  input [31:0] in4;
  (* src = "dma_axi_lite.py:70" *)
  input [31:0] in5;
  (* src = "dma_axi_lite.py:71" *)
  input [31:0] in6;
  (* src = "dma_axi_lite.py:72" *)
  input [31:0] in7;
  (* src = "dma_axi_lite.py:73" *)
  input [31:0] in8;
  (* src = "dma_axi_lite.py:74" *)
  input [31:0] in9;
  (* init = 32'd0 *)
  (* src = "dma_axi_lite.py:119" *)
  reg [31:0] rdata_v = 32'd0;
  (* init = 32'd0 *)
  (* src = "dma_axi_lite.py:59" *)
  output [31:0] read_addr;
  reg [31:0] read_addr = 32'd0;
  (* init = 2'h0 *)
  (* src = "dma_axi_lite.py:120" *)
  reg [1:0] rresp_v = 2'h0;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* init = 1'h0 *)
  (* src = "dma_axi_lite.py:113" *)
  reg rvalid_v = 1'h0;
  (* src = "nmigen/hdl/rec.py:84" *)
  input [31:0] s_axi_ri___araddr;
  (* src = "nmigen/hdl/rec.py:84" *)
  input s_axi_ri___arvalid;
  (* src = "nmigen/hdl/rec.py:84" *)
  input s_axi_ri___rready;
  (* src = "nmigen/hdl/rec.py:84" *)
  output s_axi_ro___arready;
  (* src = "nmigen/hdl/rec.py:84" *)
  output [31:0] s_axi_ro___rdata;
  (* src = "nmigen/hdl/rec.py:84" *)
  output [1:0] s_axi_ro___rresp;
  (* src = "nmigen/hdl/rec.py:84" *)
  output s_axi_ro___rvalid;
  (* src = "nmigen/hdl/rec.py:84" *)
  input [31:0] s_axi_wi___awaddr;
  (* src = "nmigen/hdl/rec.py:84" *)
  input s_axi_wi___awvalid;
  (* src = "nmigen/hdl/rec.py:84" *)
  input s_axi_wi___bready;
  (* src = "nmigen/hdl/rec.py:84" *)
  input [31:0] s_axi_wi___wdata;
  (* src = "nmigen/hdl/rec.py:84" *)
  input [3:0] s_axi_wi___wstrb;
  (* src = "nmigen/hdl/rec.py:84" *)
  input s_axi_wi___wvalid;
  (* src = "nmigen/hdl/rec.py:84" *)
  output s_axi_wo___awready;
  (* src = "nmigen/hdl/rec.py:84" *)
  output [1:0] s_axi_wo___bresp;
  (* src = "nmigen/hdl/rec.py:84" *)
  output s_axi_wo___bvalid;
  (* src = "nmigen/hdl/rec.py:84" *)
  output s_axi_wo___wready;
  (* init = 32'd0 *)
  (* src = "dma_axi_lite.py:63" *)
  output [31:0] start;
  reg [31:0] start = 32'd0;
  (* src = "dma_axi_lite.py:125" *)
  wire [31:0] wdata_v;
  (* init = 1'h0 *)
  (* src = "dma_axi_lite.py:116" *)
  reg wready_v = 1'h0;
  (* init = 32'd0 *)
  (* src = "dma_axi_lite.py:60" *)
  output [31:0] write_addr;
  reg [31:0] write_addr = 32'd0;
  (* src = "dma_axi_lite.py:126" *)
  wire [3:0] wstrb_v;
  assign \$1  = s_axi_ri___araddr >>> (* src = "dma_axi_lite.py:225" *) 2'h2;
  assign \$3  = s_axi_wi___awaddr >>> (* src = "dma_axi_lite.py:248" *) 2'h2;
  always @(posedge clk)
      start <= \$next\start ;
  always @(posedge clk)
      addr_v <= \$next\addr_v ;
  always @(posedge clk)
      fsm_state <= \$next\fsm_state ;
  always @(posedge clk)
      bvalid_v <= \$next\bvalid_v ;
  always @(posedge clk)
      rvalid_v <= \$next\rvalid_v ;
  always @(posedge clk)
      write_addr <= \$next\write_addr ;
  always @(posedge clk)
      read_addr <= \$next\read_addr ;
  always @(posedge clk)
      bresp_v <= \$next\bresp_v ;
  always @(posedge clk)
      wready_v <= \$next\wready_v ;
  always @(posedge clk)
      awready_v <= \$next\awready_v ;
  always @(posedge clk)
      rresp_v <= \$next\rresp_v ;
  always @(posedge clk)
      rdata_v <= \$next\rdata_v ;
  always @(posedge clk)
      arready_v <= \$next\arready_v ;
  always @* begin
    \$next\wdata_v  = 32'd0;
    \$next\wdata_v  = 32'd0;
    casez (fsm_state)
      3'h4:
          casez (s_axi_wi___wvalid)
            1'h1:
                \$next\wdata_v  = s_axi_wi___wdata;
          endcase
    endcase
  end
  always @* begin
    \$next\wstrb_v  = 4'h0;
    \$next\wstrb_v  = 4'h0;
    casez (fsm_state)
      3'h4:
          casez (s_axi_wi___wvalid)
            1'h1:
                \$next\wstrb_v  = s_axi_wi___wstrb;
          endcase
    endcase
  end
  always @* begin
    \$next\rresp_v  = rresp_v;
    casez (fsm_state)
      3'h3:
          casez (basic_enable)
            1'h1:
                \$next\rresp_v  = 2'h0;
            1'hz:
                \$next\rresp_v  = 2'h3;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\rresp_v  = 2'h0;
    endcase
  end
  always @* begin
    \$next\awready_v  = awready_v;
    casez (fsm_state)
      3'h2:
          \$next\awready_v  = 1'h1;
      3'h4:
          \$next\awready_v  = 1'h0;
    endcase
    casez (rst)
      1'h1:
          \$next\awready_v  = 1'h0;
    endcase
  end
  always @* begin
    \$next\wready_v  = wready_v;
    casez (fsm_state)
      3'h4:
          \$next\wready_v  = 1'h1;
      3'h5:
          \$next\wready_v  = 1'h0;
    endcase
    casez (rst)
      1'h1:
          \$next\wready_v  = 1'h0;
    endcase
  end
  always @* begin
    \$next\bresp_v  = bresp_v;
    casez (fsm_state)
      3'h4:
          casez (s_axi_wi___wvalid)
            1'h1:
                casez (basic_enable)
                  1'h1:
                    begin
                      \$next\bresp_v  = 2'h0;
                      casez (wstrb_v[0])
                        1'h1:
                            casez (basic_index)
                              4'h3:
                                  \$next\bresp_v  = 2'h2;
                              4'h4:
                                  \$next\bresp_v  = 2'h2;
                              4'h5:
                                  \$next\bresp_v  = 2'h2;
                              4'h6:
                                  \$next\bresp_v  = 2'h2;
                              4'h7:
                                  \$next\bresp_v  = 2'h2;
                              4'h8:
                                  \$next\bresp_v  = 2'h2;
                              4'h9:
                                  \$next\bresp_v  = 2'h2;
                              4'ha:
                                  \$next\bresp_v  = 2'h2;
                              4'hb:
                                  \$next\bresp_v  = 2'h2;
                            endcase
                      endcase
                      casez (wstrb_v[1])
                        1'h1:
                            casez (basic_index)
                              4'h3:
                                  \$next\bresp_v  = 2'h2;
                              4'h4:
                                  \$next\bresp_v  = 2'h2;
                              4'h5:
                                  \$next\bresp_v  = 2'h2;
                              4'h6:
                                  \$next\bresp_v  = 2'h2;
                              4'h7:
                                  \$next\bresp_v  = 2'h2;
                              4'h8:
                                  \$next\bresp_v  = 2'h2;
                              4'h9:
                                  \$next\bresp_v  = 2'h2;
                              4'ha:
                                  \$next\bresp_v  = 2'h2;
                              4'hb:
                                  \$next\bresp_v  = 2'h2;
                            endcase
                      endcase
                      casez (wstrb_v[2])
                        1'h1:
                            casez (basic_index)
                              4'h3:
                                  \$next\bresp_v  = 2'h2;
                              4'h4:
                                  \$next\bresp_v  = 2'h2;
                              4'h5:
                                  \$next\bresp_v  = 2'h2;
                              4'h6:
                                  \$next\bresp_v  = 2'h2;
                              4'h7:
                                  \$next\bresp_v  = 2'h2;
                              4'h8:
                                  \$next\bresp_v  = 2'h2;
                              4'h9:
                                  \$next\bresp_v  = 2'h2;
                              4'ha:
                                  \$next\bresp_v  = 2'h2;
                              4'hb:
                                  \$next\bresp_v  = 2'h2;
                            endcase
                      endcase
                      casez (wstrb_v[3])
                        1'h1:
                            casez (basic_index)
                              4'h3:
                                  \$next\bresp_v  = 2'h2;
                              4'h4:
                                  \$next\bresp_v  = 2'h2;
                              4'h5:
                                  \$next\bresp_v  = 2'h2;
                              4'h6:
                                  \$next\bresp_v  = 2'h2;
                              4'h7:
                                  \$next\bresp_v  = 2'h2;
                              4'h8:
                                  \$next\bresp_v  = 2'h2;
                              4'h9:
                                  \$next\bresp_v  = 2'h2;
                              4'ha:
                                  \$next\bresp_v  = 2'h2;
                              4'hb:
                                  \$next\bresp_v  = 2'h2;
                            endcase
                      endcase
                    end
                  1'hz:
                      \$next\bresp_v  = 2'h3;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\bresp_v  = 2'h0;
    endcase
  end
  always @* begin
    \$next\read_addr  = read_addr;
    casez (fsm_state)
      3'h4:
          casez (s_axi_wi___wvalid)
            1'h1:
                casez (basic_enable)
                  1'h1:
                    begin
                      casez (wstrb_v[0])
                        1'h1:
                            casez (basic_index)
                              4'h0:
                                  \$next\read_addr [7:0] = wdata_v[7:0];
                            endcase
                      endcase
                      casez (wstrb_v[1])
                        1'h1:
                            casez (basic_index)
                              4'h0:
                                  \$next\read_addr [15:8] = wdata_v[15:8];
                            endcase
                      endcase
                      casez (wstrb_v[2])
                        1'h1:
                            casez (basic_index)
                              4'h0:
                                  \$next\read_addr [23:16] = wdata_v[23:16];
                            endcase
                      endcase
                      casez (wstrb_v[3])
                        1'h1:
                            casez (basic_index)
                              4'h0:
                                  \$next\read_addr [31:24] = wdata_v[31:24];
                            endcase
                      endcase
                    end
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\read_addr  = 32'd0;
    endcase
  end
  always @* begin
    \$next\write_addr  = write_addr;
    casez (fsm_state)
      3'h4:
          casez (s_axi_wi___wvalid)
            1'h1:
                casez (basic_enable)
                  1'h1:
                    begin
                      casez (wstrb_v[0])
                        1'h1:
                            casez (basic_index)
                              4'h1:
                                  \$next\write_addr [7:0] = wdata_v[7:0];
                            endcase
                      endcase
                      casez (wstrb_v[1])
                        1'h1:
                            casez (basic_index)
                              4'h1:
                                  \$next\write_addr [15:8] = wdata_v[15:8];
                            endcase
                      endcase
                      casez (wstrb_v[2])
                        1'h1:
                            casez (basic_index)
                              4'h1:
                                  \$next\write_addr [23:16] = wdata_v[23:16];
                            endcase
                      endcase
                      casez (wstrb_v[3])
                        1'h1:
                            casez (basic_index)
                              4'h1:
                                  \$next\write_addr [31:24] = wdata_v[31:24];
                            endcase
                      endcase
                    end
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\write_addr  = 32'd0;
    endcase
  end
  always @* begin
    \$next\start  = start;
    casez (fsm_state)
      3'h4:
          casez (s_axi_wi___wvalid)
            1'h1:
                casez (basic_enable)
                  1'h1:
                    begin
                      casez (wstrb_v[0])
                        1'h1:
                            casez (basic_index)
                              4'h2:
                                  \$next\start [7:0] = wdata_v[7:0];
                            endcase
                      endcase
                      casez (wstrb_v[1])
                        1'h1:
                            casez (basic_index)
                              4'h2:
                                  \$next\start [15:8] = wdata_v[15:8];
                            endcase
                      endcase
                      casez (wstrb_v[2])
                        1'h1:
                            casez (basic_index)
                              4'h2:
                                  \$next\start [23:16] = wdata_v[23:16];
                            endcase
                      endcase
                      casez (wstrb_v[3])
                        1'h1:
                            casez (basic_index)
                              4'h2:
                                  \$next\start [31:24] = wdata_v[31:24];
                            endcase
                      endcase
                    end
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\start  = 32'd0;
    endcase
  end
  always @* begin
    \$next\s_axi_ro___arready  = 1'h0;
    \$next\s_axi_ro___arready  = arready_v;
  end
  always @* begin
    \$next\s_axi_ro___rvalid  = 1'h0;
    \$next\s_axi_ro___rvalid  = rvalid_v;
  end
  always @* begin
    \$next\s_axi_wo___awready  = 1'h0;
    \$next\s_axi_wo___awready  = awready_v;
  end
  always @* begin
    \$next\basic_enable  = 1'h0;
    \$next\basic_enable  = addr_v[10];
  end
  always @* begin
    \$next\s_axi_wo___wready  = 1'h0;
    \$next\s_axi_wo___wready  = wready_v;
  end
  always @* begin
    \$next\s_axi_wo___bvalid  = 1'h0;
    \$next\s_axi_wo___bvalid  = bvalid_v;
  end
  always @* begin
    \$next\s_axi_ro___rdata  = 32'd0;
    \$next\s_axi_ro___rdata  = rdata_v;
  end
  always @* begin
    \$next\s_axi_ro___rresp  = 2'h0;
    \$next\s_axi_ro___rresp  = rresp_v;
  end
  always @* begin
    \$next\s_axi_wo___bresp  = 2'h0;
    \$next\s_axi_wo___bresp  = bresp_v;
  end
  always @* begin
    \$next\basic_index  = 4'h0;
    \$next\basic_index  = addr_v[3:0];
  end
  always @* begin
    \$next\rvalid_v  = rvalid_v;
    casez (fsm_state)
      3'h0:
          \$next\rvalid_v  = 1'h0;
      3'h3:
          casez (s_axi_ri___rready)
            1'h1:
                \$next\rvalid_v  = 1'h1;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\rvalid_v  = 1'h0;
    endcase
  end
  always @* begin
    \$next\bvalid_v  = bvalid_v;
    casez (fsm_state)
      3'h0:
          \$next\bvalid_v  = 1'h0;
      3'h5:
          casez (s_axi_wi___bready)
            1'h1:
                \$next\bvalid_v  = 1'h1;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\bvalid_v  = 1'h0;
    endcase
  end
  always @* begin
    \$next\fsm_state  = fsm_state;
    casez (fsm_state)
      3'h0:
          casez ({ s_axi_wi___awvalid, s_axi_ri___arvalid })
            2'bz1:
                \$next\fsm_state  = 3'h1;
            2'b1z:
                \$next\fsm_state  = 3'h2;
          endcase
      3'h1:
          \$next\fsm_state  = 3'h3;
      3'h3:
          casez (s_axi_ri___rready)
            1'h1:
                \$next\fsm_state  = 3'h0;
          endcase
      3'h2:
          \$next\fsm_state  = 3'h4;
      3'h4:
          casez (s_axi_wi___wvalid)
            1'h1:
                \$next\fsm_state  = 3'h5;
          endcase
      3'h5:
          casez (s_axi_wi___bready)
            1'h1:
                \$next\fsm_state  = 3'h0;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fsm_state  = 3'h0;
    endcase
  end
  always @* begin
    \$next\addr_v  = addr_v;
    casez (fsm_state)
      3'h1:
          \$next\addr_v  = \$1 ;
      3'h2:
          \$next\addr_v  = \$3 ;
    endcase
    casez (rst)
      1'h1:
          \$next\addr_v  = 32'd0;
    endcase
  end
  always @* begin
    \$next\arready_v  = arready_v;
    casez (fsm_state)
      3'h1:
          \$next\arready_v  = 1'h1;
      3'h3:
          \$next\arready_v  = 1'h0;
    endcase
    casez (rst)
      1'h1:
          \$next\arready_v  = 1'h0;
    endcase
  end
  always @* begin
    \$next\rdata_v  = rdata_v;
    casez (fsm_state)
      3'h3:
          casez (basic_enable)
            1'h1:
                casez (basic_index)
                  4'h0:
                      \$next\rdata_v  = read_addr;
                  4'h1:
                      \$next\rdata_v  = write_addr;
                  4'h2:
                      \$next\rdata_v  = start;
                  4'h3:
                      \$next\rdata_v  = in1;
                  4'h4:
                      \$next\rdata_v  = in2;
                  4'h5:
                      \$next\rdata_v  = in3;
                  4'h6:
                      \$next\rdata_v  = in4;
                  4'h7:
                      \$next\rdata_v  = in5;
                  4'h8:
                      \$next\rdata_v  = in6;
                  4'h9:
                      \$next\rdata_v  = in7;
                  4'ha:
                      \$next\rdata_v  = in8;
                  4'hb:
                      \$next\rdata_v  = in9;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\rdata_v  = 32'd0;
    endcase
  end
  assign s_axi_wo___bresp = \$next\s_axi_wo___bresp ;
  assign s_axi_ro___rresp = \$next\s_axi_ro___rresp ;
  assign s_axi_ro___rdata = \$next\s_axi_ro___rdata ;
  assign s_axi_wo___bvalid = \$next\s_axi_wo___bvalid ;
  assign s_axi_wo___wready = \$next\s_axi_wo___wready ;
  assign s_axi_wo___awready = \$next\s_axi_wo___awready ;
  assign s_axi_ro___rvalid = \$next\s_axi_ro___rvalid ;
  assign s_axi_ro___arready = \$next\s_axi_ro___arready ;
  assign basic_index = \$next\basic_index ;
  assign basic_enable = \$next\basic_enable ;
  assign wstrb_v = \$next\wstrb_v ;
  assign wdata_v = \$next\wdata_v ;
endmodule

