/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top.fifo32" *)
(* generator = "nMigen" *)
module fifo32(we, replace, re, rst, clk, writable, readable, dout, din);
  wire \$11 ;
  wire \$13 ;
  wire \$15 ;
  wire \$17 ;
  wire [2:0] \$19 ;
  wire \$2 ;
  wire [2:0] \$20 ;
  wire \$22 ;
  wire [2:0] \$24 ;
  wire [2:0] \$25 ;
  wire \$27 ;
  wire \$29 ;
  wire \$31 ;
  wire \$33 ;
  wire \$34 ;
  wire \$37 ;
  wire [3:0] \$39 ;
  wire \$4 ;
  wire [3:0] \$40 ;
  wire \$42 ;
  wire \$44 ;
  wire \$45 ;
  wire \$47 ;
  wire \$49 ;
  wire \$52 ;
  wire [3:0] \$54 ;
  wire [3:0] \$55 ;
  wire [2:0] \$6 ;
  wire [2:0] \$7 ;
  wire \$9 ;
  (* src = "nmigen/lib/fifo.py:156" *)
  reg [1:0] \$next\consume ;
  (* src = "nmigen/lib/fifo.py:69" *)
  reg [31:0] \$next\dout ;
  (* src = "nmigen/lib/fifo.py:138" *)
  reg [2:0] \$next\level ;
  (* src = "nmigen/lib/fifo.py:155" *)
  reg [1:0] \$next\produce ;
  (* src = "nmigen/hdl/mem.py:81" *)
  reg [1:0] \$next\rdport_storage_r_addr ;
  (* src = "nmigen/lib/fifo.py:70" *)
  reg \$next\readable ;
  (* src = "nmigen/lib/fifo.py:66" *)
  reg \$next\writable ;
  (* src = "nmigen/hdl/mem.py:146" *)
  reg [1:0] \$next\wrport_storage_w_addr ;
  (* src = "nmigen/hdl/mem.py:148" *)
  reg [31:0] \$next\wrport_storage_w_data ;
  (* src = "nmigen/hdl/mem.py:150" *)
  reg \$next\wrport_storage_w_en ;
  (* src = "nmigen/hdl/mem.py:160" *)
  input clk;
  (* init = 2'h0 *)
  (* src = "nmigen/lib/fifo.py:156" *)
  reg [1:0] consume = 2'h0;
  (* src = "nmigen/lib/fifo.py:65" *)
  input [31:0] din;
  (* src = "nmigen/lib/fifo.py:69" *)
  output [31:0] dout;
  (* init = 3'h0 *)
  (* src = "nmigen/lib/fifo.py:138" *)
  reg [2:0] level = 3'h0;
  (* init = 2'h0 *)
  (* src = "nmigen/lib/fifo.py:155" *)
  reg [1:0] produce = 2'h0;
  (* src = "nmigen/hdl/mem.py:81" *)
  wire [1:0] rdport_storage_r_addr;
  (* src = "nmigen/hdl/mem.py:83" *)
  wire [31:0] rdport_storage_r_data;
  (* src = "nmigen/lib/fifo.py:71" *)
  input re;
  (* src = "nmigen/lib/fifo.py:70" *)
  output readable;
  (* src = "nmigen/lib/fifo.py:139" *)
  input replace;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "nmigen/lib/fifo.py:67" *)
  input we;
  (* src = "nmigen/lib/fifo.py:66" *)
  output writable;
  (* src = "nmigen/hdl/mem.py:146" *)
  wire [1:0] wrport_storage_w_addr;
  (* src = "nmigen/hdl/mem.py:148" *)
  wire [31:0] wrport_storage_w_data;
  (* src = "nmigen/hdl/mem.py:150" *)
  wire wrport_storage_w_en;
  assign \$9  = writable | (* src = "nmigen/lib/fifo.py:161" *) replace;
  assign \$11  = we & (* src = "nmigen/lib/fifo.py:161" *) \$9 ;
  assign \$13  = writable & (* src = "nmigen/lib/fifo.py:149" *) we;
  assign \$15  = ~ (* src = "nmigen/lib/fifo.py:149" *) replace;
  assign \$17  = \$13  & (* src = "nmigen/lib/fifo.py:149" *) \$15 ;
  assign \$20  = produce + (* src = "nmigen/lib/fifo.py:93" *) 1'h1;
  assign \$22  = readable & (* src = "nmigen/lib/fifo.py:148" *) re;
  assign \$25  = consume + (* src = "nmigen/lib/fifo.py:93" *) 1'h1;
  assign \$27  = writable & (* src = "nmigen/lib/fifo.py:149" *) we;
  assign \$2  = level != (* src = "nmigen/lib/fifo.py:144" *) 3'h4;
  assign \$29  = ~ (* src = "nmigen/lib/fifo.py:149" *) replace;
  assign \$31  = \$27  & (* src = "nmigen/lib/fifo.py:149" *) \$29 ;
  assign \$34  = readable & (* src = "nmigen/lib/fifo.py:148" *) re;
  assign \$33  = ~ (* src = "nmigen/lib/fifo.py:177" *) \$34 ;
  assign \$37  = \$31  & (* src = "nmigen/lib/fifo.py:177" *) \$33 ;
  assign \$40  = level + (* src = "nmigen/lib/fifo.py:178" *) 1'h1;
  assign \$42  = readable & (* src = "nmigen/lib/fifo.py:148" *) re;
  assign \$45  = writable & (* src = "nmigen/lib/fifo.py:149" *) we;
  assign \$47  = ~ (* src = "nmigen/lib/fifo.py:149" *) replace;
  assign \$4  = level != (* src = "nmigen/lib/fifo.py:145" *) 1'h0;
  assign \$49  = \$45  & (* src = "nmigen/lib/fifo.py:149" *) \$47 ;
  assign \$44  = ~ (* src = "nmigen/lib/fifo.py:179" *) \$49 ;
  assign \$52  = \$42  & (* src = "nmigen/lib/fifo.py:179" *) \$44 ;
  assign \$55  = level - (* src = "nmigen/lib/fifo.py:180" *) 1'h1;
  assign \$7  = produce - (* src = "nmigen/lib/fifo.py:100" *) 1'h1;
  always @(posedge clk)
      level <= \$next\level ;
  always @(posedge clk)
      consume <= \$next\consume ;
  always @(posedge clk)
      produce <= \$next\produce ;
  reg [31:0] storage [3:0];
  initial begin
    storage[0] = 32'd0;
    storage[1] = 32'd0;
    storage[2] = 32'd0;
    storage[3] = 32'd0;
  end
  always @(posedge clk) begin
    if (\$next\wrport_storage_w_en ) storage[\$next\wrport_storage_w_addr ] <= \$next\wrport_storage_w_data ;
  end
  assign rdport_storage_r_data = storage[\$next\rdport_storage_r_addr ];
  always @* begin
    \$next\writable  = 1'h0;
    \$next\writable  = \$2 ;
  end
  always @* begin
    \$next\readable  = 1'h0;
    \$next\readable  = \$4 ;
  end
  always @* begin
    \$next\wrport_storage_w_addr  = 2'h0;
    \$next\wrport_storage_w_addr  = produce;
    casez (replace)
      1'h1:
          \$next\wrport_storage_w_addr  = \$6 [1:0];
    endcase
  end
  always @* begin
    \$next\wrport_storage_w_data  = 32'd0;
    \$next\wrport_storage_w_data  = din;
  end
  always @* begin
    \$next\wrport_storage_w_en  = 1'h0;
    \$next\wrport_storage_w_en  = \$11 ;
  end
  always @* begin
    \$next\produce  = produce;
    casez (\$17 )
      1'h1:
          \$next\produce  = \$19 [1:0];
    endcase
    casez (rst)
      1'h1:
          \$next\produce  = 2'h0;
    endcase
  end
  always @* begin
    \$next\rdport_storage_r_addr  = 2'h0;
    \$next\rdport_storage_r_addr  = consume;
  end
  always @* begin
    \$next\dout  = 32'd0;
    \$next\dout  = rdport_storage_r_data;
  end
  always @* begin
    \$next\consume  = consume;
    casez (\$22 )
      1'h1:
          \$next\consume  = \$24 [1:0];
    endcase
    casez (rst)
      1'h1:
          \$next\consume  = 2'h0;
    endcase
  end
  always @* begin
    \$next\level  = level;
    casez (\$37 )
      1'h1:
          \$next\level  = \$39 [2:0];
    endcase
    casez (\$52 )
      1'h1:
          \$next\level  = \$54 [2:0];
    endcase
    casez (rst)
      1'h1:
          \$next\level  = 3'h0;
    endcase
  end
  assign \$6  = \$7 ;
  assign \$19  = \$20 ;
  assign \$24  = \$25 ;
  assign \$39  = \$40 ;
  assign \$54  = \$55 ;
  assign dout = \$next\dout ;
  assign rdport_storage_r_addr = \$next\rdport_storage_r_addr ;
  assign wrport_storage_w_en = \$next\wrport_storage_w_en ;
  assign wrport_storage_w_data = \$next\wrport_storage_w_data ;
  assign wrport_storage_w_addr = \$next\wrport_storage_w_addr ;
  assign readable = \$next\readable ;
  assign writable = \$next\writable ;
endmodule

(* \nmigen.hierarchy  = "top.fifo64" *)
(* generator = "nMigen" *)
module fifo64(we, replace, re, rst, clk, writable, readable, dout, din);
  wire \$11 ;
  wire \$13 ;
  wire \$15 ;
  wire \$17 ;
  wire [1:0] \$19 ;
  wire \$2 ;
  wire [1:0] \$20 ;
  wire \$22 ;
  wire [1:0] \$24 ;
  wire [1:0] \$25 ;
  wire \$27 ;
  wire \$29 ;
  wire \$31 ;
  wire \$33 ;
  wire \$34 ;
  wire \$37 ;
  wire [2:0] \$39 ;
  wire \$4 ;
  wire [2:0] \$40 ;
  wire \$42 ;
  wire \$44 ;
  wire \$45 ;
  wire \$47 ;
  wire \$49 ;
  wire \$52 ;
  wire [2:0] \$54 ;
  wire [2:0] \$55 ;
  wire [1:0] \$6 ;
  wire [1:0] \$7 ;
  wire \$9 ;
  (* src = "nmigen/lib/fifo.py:156" *)
  reg \$next\consume ;
  (* src = "nmigen/lib/fifo.py:69" *)
  reg [63:0] \$next\dout ;
  (* src = "nmigen/lib/fifo.py:138" *)
  reg [1:0] \$next\level ;
  (* src = "nmigen/lib/fifo.py:155" *)
  reg \$next\produce ;
  (* src = "nmigen/hdl/mem.py:81" *)
  reg \$next\rdport_storage_r_addr ;
  (* src = "nmigen/lib/fifo.py:70" *)
  reg \$next\readable ;
  (* src = "nmigen/lib/fifo.py:66" *)
  reg \$next\writable ;
  (* src = "nmigen/hdl/mem.py:146" *)
  reg \$next\wrport_storage_w_addr ;
  (* src = "nmigen/hdl/mem.py:148" *)
  reg [63:0] \$next\wrport_storage_w_data ;
  (* src = "nmigen/hdl/mem.py:150" *)
  reg \$next\wrport_storage_w_en ;
  (* src = "nmigen/hdl/mem.py:160" *)
  input clk;
  (* init = 1'h0 *)
  (* src = "nmigen/lib/fifo.py:156" *)
  reg consume = 1'h0;
  (* src = "nmigen/lib/fifo.py:65" *)
  input [63:0] din;
  (* src = "nmigen/lib/fifo.py:69" *)
  output [63:0] dout;
  (* init = 2'h0 *)
  (* src = "nmigen/lib/fifo.py:138" *)
  reg [1:0] level = 2'h0;
  (* init = 1'h0 *)
  (* src = "nmigen/lib/fifo.py:155" *)
  reg produce = 1'h0;
  (* src = "nmigen/hdl/mem.py:81" *)
  wire rdport_storage_r_addr;
  (* src = "nmigen/hdl/mem.py:83" *)
  wire [63:0] rdport_storage_r_data;
  (* src = "nmigen/lib/fifo.py:71" *)
  input re;
  (* src = "nmigen/lib/fifo.py:70" *)
  output readable;
  (* src = "nmigen/lib/fifo.py:139" *)
  input replace;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "nmigen/lib/fifo.py:67" *)
  input we;
  (* src = "nmigen/lib/fifo.py:66" *)
  output writable;
  (* src = "nmigen/hdl/mem.py:146" *)
  wire wrport_storage_w_addr;
  (* src = "nmigen/hdl/mem.py:148" *)
  wire [63:0] wrport_storage_w_data;
  (* src = "nmigen/hdl/mem.py:150" *)
  wire wrport_storage_w_en;
  assign \$9  = writable | (* src = "nmigen/lib/fifo.py:161" *) replace;
  assign \$11  = we & (* src = "nmigen/lib/fifo.py:161" *) \$9 ;
  assign \$13  = writable & (* src = "nmigen/lib/fifo.py:149" *) we;
  assign \$15  = ~ (* src = "nmigen/lib/fifo.py:149" *) replace;
  assign \$17  = \$13  & (* src = "nmigen/lib/fifo.py:149" *) \$15 ;
  assign \$20  = produce + (* src = "nmigen/lib/fifo.py:93" *) 1'h1;
  assign \$22  = readable & (* src = "nmigen/lib/fifo.py:148" *) re;
  assign \$25  = consume + (* src = "nmigen/lib/fifo.py:93" *) 1'h1;
  assign \$27  = writable & (* src = "nmigen/lib/fifo.py:149" *) we;
  assign \$2  = level != (* src = "nmigen/lib/fifo.py:144" *) 2'h2;
  assign \$29  = ~ (* src = "nmigen/lib/fifo.py:149" *) replace;
  assign \$31  = \$27  & (* src = "nmigen/lib/fifo.py:149" *) \$29 ;
  assign \$34  = readable & (* src = "nmigen/lib/fifo.py:148" *) re;
  assign \$33  = ~ (* src = "nmigen/lib/fifo.py:177" *) \$34 ;
  assign \$37  = \$31  & (* src = "nmigen/lib/fifo.py:177" *) \$33 ;
  assign \$40  = level + (* src = "nmigen/lib/fifo.py:178" *) 1'h1;
  assign \$42  = readable & (* src = "nmigen/lib/fifo.py:148" *) re;
  assign \$45  = writable & (* src = "nmigen/lib/fifo.py:149" *) we;
  assign \$47  = ~ (* src = "nmigen/lib/fifo.py:149" *) replace;
  assign \$4  = level != (* src = "nmigen/lib/fifo.py:145" *) 1'h0;
  assign \$49  = \$45  & (* src = "nmigen/lib/fifo.py:149" *) \$47 ;
  assign \$44  = ~ (* src = "nmigen/lib/fifo.py:179" *) \$49 ;
  assign \$52  = \$42  & (* src = "nmigen/lib/fifo.py:179" *) \$44 ;
  assign \$55  = level - (* src = "nmigen/lib/fifo.py:180" *) 1'h1;
  assign \$7  = produce - (* src = "nmigen/lib/fifo.py:100" *) 1'h1;
  always @(posedge clk)
      level <= \$next\level ;
  always @(posedge clk)
      consume <= \$next\consume ;
  always @(posedge clk)
      produce <= \$next\produce ;
  reg [63:0] storage [1:0];
  initial begin
    storage[0] = 64'h0000000000000000;
    storage[1] = 64'h0000000000000000;
  end
  always @(posedge clk) begin
    if (\$next\wrport_storage_w_en ) storage[\$next\wrport_storage_w_addr ] <= \$next\wrport_storage_w_data ;
  end
  assign rdport_storage_r_data = storage[\$next\rdport_storage_r_addr ];
  always @* begin
    \$next\writable  = 1'h0;
    \$next\writable  = \$2 ;
  end
  always @* begin
    \$next\readable  = 1'h0;
    \$next\readable  = \$4 ;
  end
  always @* begin
    \$next\wrport_storage_w_addr  = 1'h0;
    \$next\wrport_storage_w_addr  = produce;
    casez (replace)
      1'h1:
          \$next\wrport_storage_w_addr  = \$6 [0];
    endcase
  end
  always @* begin
    \$next\wrport_storage_w_data  = 64'h0000000000000000;
    \$next\wrport_storage_w_data  = din;
  end
  always @* begin
    \$next\wrport_storage_w_en  = 1'h0;
    \$next\wrport_storage_w_en  = \$11 ;
  end
  always @* begin
    \$next\produce  = produce;
    casez (\$17 )
      1'h1:
          \$next\produce  = \$19 [0];
    endcase
    casez (rst)
      1'h1:
          \$next\produce  = 1'h0;
    endcase
  end
  always @* begin
    \$next\rdport_storage_r_addr  = 1'h0;
    \$next\rdport_storage_r_addr  = consume;
  end
  always @* begin
    \$next\dout  = 64'h0000000000000000;
    \$next\dout  = rdport_storage_r_data;
  end
  always @* begin
    \$next\consume  = consume;
    casez (\$22 )
      1'h1:
          \$next\consume  = \$24 [0];
    endcase
    casez (rst)
      1'h1:
          \$next\consume  = 1'h0;
    endcase
  end
  always @* begin
    \$next\level  = level;
    casez (\$37 )
      1'h1:
          \$next\level  = \$39 [1:0];
    endcase
    casez (\$52 )
      1'h1:
          \$next\level  = \$54 [1:0];
    endcase
    casez (rst)
      1'h1:
          \$next\level  = 2'h0;
    endcase
  end
  assign \$6  = \$7 ;
  assign \$19  = \$20 ;
  assign \$24  = \$25 ;
  assign \$39  = \$40 ;
  assign \$54  = \$55 ;
  assign dout = \$next\dout ;
  assign rdport_storage_r_addr = \$next\rdport_storage_r_addr ;
  assign wrport_storage_w_en = \$next\wrport_storage_w_en ;
  assign wrport_storage_w_data = \$next\wrport_storage_w_data ;
  assign wrport_storage_w_addr = \$next\wrport_storage_w_addr ;
  assign readable = \$next\readable ;
  assign writable = \$next\writable ;
endmodule

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(data_in, i_busy, rst, clk, valid_out, o_busy, data_out, valid_in);
  wire \$10 ;
  wire \$12 ;
  wire \$14 ;
  wire \$16 ;
  wire \$18 ;
  wire \$2 ;
  wire \$20 ;
  wire \$22 ;
  wire \$24 ;
  wire \$26 ;
  wire \$28 ;
  wire \$30 ;
  wire \$32 ;
  wire \$4 ;
  wire \$6 ;
  wire \$8 ;
  (* src = "b64_b32.py:105" *)
  reg [31:0] \$next\buff ;
  (* src = "b64_b32.py:38" *)
  reg [31:0] \$next\data_out ;
  (* src = "nmigen/lib/fifo.py:65" *)
  reg [31:0] \$next\fifo32_din ;
  (* src = "nmigen/lib/fifo.py:71" *)
  reg \$next\fifo32_re ;
  (* src = "nmigen/lib/fifo.py:139" *)
  reg \$next\fifo32_replace ;
  (* src = "nmigen/lib/fifo.py:67" *)
  reg \$next\fifo32_we ;
  (* src = "nmigen/lib/fifo.py:65" *)
  reg [63:0] \$next\fifo64_din ;
  (* src = "nmigen/lib/fifo.py:71" *)
  reg \$next\fifo64_re ;
  (* src = "nmigen/lib/fifo.py:139" *)
  reg \$next\fifo64_replace ;
  (* src = "nmigen/lib/fifo.py:67" *)
  reg \$next\fifo64_we ;
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg [1:0] \$next\fsm_state ;
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg \$next\fsm_state$1 ;
  (* src = "b64_b32.py:44" *)
  reg \$next\o_busy ;
  (* src = "b64_b32.py:68" *)
  reg [63:0] \$next\reg ;
  (* src = "b64_b32.py:42" *)
  reg \$next\valid_out ;
  (* init = 32'd0 *)
  (* src = "b64_b32.py:105" *)
  reg [31:0] buff = 32'd0;
  (* src = "nmigen/hdl/mem.py:160" *)
  input clk;
  (* src = "b64_b32.py:35" *)
  input [63:0] data_in;
  (* src = "b64_b32.py:38" *)
  output [31:0] data_out;
  (* init = 32'd0 *)
  (* src = "nmigen/lib/fifo.py:65" *)
  reg [31:0] fifo32_din = 32'd0;
  (* src = "nmigen/lib/fifo.py:69" *)
  wire [31:0] fifo32_dout;
  (* src = "nmigen/lib/fifo.py:71" *)
  wire fifo32_re;
  (* src = "nmigen/lib/fifo.py:70" *)
  wire fifo32_readable;
  (* init = 1'h0 *)
  (* src = "nmigen/lib/fifo.py:139" *)
  reg fifo32_replace = 1'h0;
  (* init = 1'h0 *)
  (* src = "nmigen/lib/fifo.py:67" *)
  reg fifo32_we = 1'h0;
  (* src = "nmigen/lib/fifo.py:66" *)
  wire fifo32_writable;
  (* init = 64'h0000000000000000 *)
  (* src = "nmigen/lib/fifo.py:65" *)
  reg [63:0] fifo64_din = 64'h0000000000000000;
  (* src = "nmigen/lib/fifo.py:69" *)
  wire [63:0] fifo64_dout;
  (* init = 1'h0 *)
  (* src = "nmigen/lib/fifo.py:71" *)
  reg fifo64_re = 1'h0;
  (* src = "nmigen/lib/fifo.py:70" *)
  wire fifo64_readable;
  (* init = 1'h0 *)
  (* src = "nmigen/lib/fifo.py:139" *)
  reg fifo64_replace = 1'h0;
  (* init = 1'h0 *)
  (* src = "nmigen/lib/fifo.py:67" *)
  reg fifo64_we = 1'h0;
  (* src = "nmigen/lib/fifo.py:66" *)
  wire fifo64_writable;
  (* init = 2'h0 *)
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg [1:0] fsm_state = 2'h0;
  (* init = 1'h0 *)
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg \fsm_state$1  = 1'h0;
  (* src = "b64_b32.py:45" *)
  input i_busy;
  (* init = 1'h0 *)
  (* src = "b64_b32.py:44" *)
  output o_busy;
  reg o_busy = 1'h0;
  (* init = 64'h0000000000000000 *)
  (* src = "b64_b32.py:68" *)
  reg [63:0] \reg  = 64'h0000000000000000;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "b64_b32.py:41" *)
  input valid_in;
  (* src = "b64_b32.py:42" *)
  output valid_out;
  assign \$10  = fifo64_readable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$12  = \$8  & (* src = "b64_b32.py:111" *) \$10 ;
  assign \$14  = fifo32_writable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$16  = fifo64_readable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$18  = \$14  & (* src = "b64_b32.py:111" *) \$16 ;
  assign \$20  = fifo32_writable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$22  = fifo64_readable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$24  = \$20  & (* src = "b64_b32.py:111" *) \$22 ;
  assign \$26  = fifo32_writable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$28  = fifo64_readable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$2  = fifo32_writable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$30  = \$26  & (* src = "b64_b32.py:111" *) \$28 ;
  assign \$32  = i_busy == (* src = "b64_b32.py:131" *) 1'h0;
  assign \$4  = fifo64_readable == (* src = "b64_b32.py:111" *) 1'h1;
  assign \$6  = \$2  & (* src = "b64_b32.py:111" *) \$4 ;
  assign \$8  = fifo32_writable == (* src = "b64_b32.py:111" *) 1'h1;
  always @(posedge clk)
      \fsm_state$1  <= \$next\fsm_state$1 ;
  always @(posedge clk)
      fifo64_we <= \$next\fifo64_we ;
  always @(posedge clk)
      fifo64_replace <= \$next\fifo64_replace ;
  always @(posedge clk)
      fifo32_replace <= \$next\fifo32_replace ;
  always @(posedge clk)
      fifo64_re <= \$next\fifo64_re ;
  always @(posedge clk)
      fifo32_we <= \$next\fifo32_we ;
  always @(posedge clk)
      buff <= \$next\buff ;
  always @(posedge clk)
      fifo32_din <= \$next\fifo32_din ;
  always @(posedge clk)
      \reg  <= \$next\reg ;
  always @(posedge clk)
      fifo64_din <= \$next\fifo64_din ;
  always @(posedge clk)
      fsm_state <= \$next\fsm_state ;
  always @(posedge clk)
      o_busy <= \$next\o_busy ;
  fifo32 fifo32 (
    .clk(clk),
    .din(fifo32_din),
    .dout(fifo32_dout),
    .re(fifo32_re),
    .readable(fifo32_readable),
    .replace(fifo32_replace),
    .rst(rst),
    .we(fifo32_we),
    .writable(fifo32_writable)
  );
  fifo64 fifo64 (
    .clk(clk),
    .din(fifo64_din),
    .dout(fifo64_dout),
    .re(fifo64_re),
    .readable(fifo64_readable),
    .replace(fifo64_replace),
    .rst(rst),
    .we(fifo64_we),
    .writable(fifo64_writable)
  );
  always @* begin
    \$next\fifo32_replace  = fifo32_replace;
    \$next\fifo32_replace  = 1'h0;
    casez (rst)
      1'h1:
          \$next\fifo32_replace  = 1'h0;
    endcase
  end
  always @* begin
    \$next\fifo64_replace  = fifo64_replace;
    \$next\fifo64_replace  = 1'h0;
    casez (rst)
      1'h1:
          \$next\fifo64_replace  = 1'h0;
    endcase
  end
  always @* begin
    \$next\fifo64_re  = fifo64_re;
    casez (\fsm_state$1 )
      1'h0:
          casez ({ fifo32_writable, \$24  })
            2'bz1:
                \$next\fifo64_re  = 1'h1;
          endcase
      1'h1:
          \$next\fifo64_re  = 1'h0;
    endcase
    casez (rst)
      1'h1:
          \$next\fifo64_re  = 1'h0;
    endcase
  end
  always @* begin
    \$next\fsm_state$1  = \fsm_state$1 ;
    casez (\fsm_state$1 )
      1'h0:
          casez ({ fifo32_writable, \$30  })
            2'bz1:
                \$next\fsm_state$1  = 1'h1;
          endcase
      1'h1:
          casez (fifo32_writable)
            1'h1:
                \$next\fsm_state$1  = 1'h0;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fsm_state$1  = 1'h0;
    endcase
  end
  always @* begin
    \$next\valid_out  = 1'h0;
    \$next\valid_out  = fifo32_readable;
  end
  always @* begin
    \$next\data_out  = 32'd0;
    \$next\data_out  = fifo32_dout;
  end
  always @* begin
    \$next\fifo32_re  = 1'h0;
    \$next\fifo32_re  = \$32 ;
  end
  always @* begin
    \$next\fifo64_we  = fifo64_we;
    casez (fsm_state)
      2'h0:
          \$next\fifo64_we  = 1'h0;
      2'h1:
          casez (valid_in)
            1'h1:
                casez (fifo64_writable)
                  1'h1:
                      \$next\fifo64_we  = 1'h1;
                endcase
          endcase
      2'h2:
          casez (fifo64_writable)
            1'h1:
                \$next\fifo64_we  = 1'h1;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fifo64_we  = 1'h0;
    endcase
  end
  always @* begin
    \$next\o_busy  = o_busy;
    casez (fsm_state)
      2'h0:
          \$next\o_busy  = 1'h0;
      2'h1:
          casez (valid_in)
            1'h1:
                casez (fifo64_writable)
                  1'h1:
                      \$next\o_busy  = 1'h1;
                  1'hz:
                      \$next\o_busy  = 1'h1;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\o_busy  = 1'h0;
    endcase
  end
  always @* begin
    \$next\fsm_state  = fsm_state;
    casez (fsm_state)
      2'h0:
          \$next\fsm_state  = 2'h1;
      2'h1:
          casez (valid_in)
            1'h1:
                casez (fifo64_writable)
                  1'h1:
                      \$next\fsm_state  = 2'h0;
                  1'hz:
                      \$next\fsm_state  = 2'h2;
                endcase
          endcase
      2'h2:
          casez (fifo64_writable)
            1'h1:
                \$next\fsm_state  = 2'h0;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fsm_state  = 2'h0;
    endcase
  end
  always @* begin
    \$next\fifo64_din  = fifo64_din;
    casez (fsm_state)
      2'h1:
          casez (valid_in)
            1'h1:
                casez (fifo64_writable)
                  1'h1:
                      \$next\fifo64_din  = data_in;
                endcase
          endcase
      2'h2:
          casez (fifo64_writable)
            1'h1:
                \$next\fifo64_din  = \reg ;
          endcase
    endcase
  end
  always @* begin
    \$next\reg  = \reg ;
    casez (fsm_state)
      2'h1:
          casez (valid_in)
            1'h1:
                casez (fifo64_writable)
                  1'h1:
                      /* empty */;
                  1'hz:
                      \$next\reg  = data_in;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\reg  = 64'h0000000000000000;
    endcase
  end
  always @* begin
    \$next\fifo32_din  = fifo32_din;
    casez (\fsm_state$1 )
      1'h0:
          casez ({ fifo32_writable, \$6  })
            2'bz1:
                \$next\fifo32_din  = fifo64_dout[63:32];
          endcase
      1'h1:
          casez (fifo32_writable)
            1'h1:
                \$next\fifo32_din  = buff;
          endcase
    endcase
  end
  always @* begin
    \$next\buff  = buff;
    casez (\fsm_state$1 )
      1'h0:
          casez ({ fifo32_writable, \$12  })
            2'bz1:
                \$next\buff  = fifo64_dout[31:0];
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff  = 32'd0;
    endcase
  end
  always @* begin
    \$next\fifo32_we  = fifo32_we;
    casez (\fsm_state$1 )
      1'h0:
          casez ({ fifo32_writable, \$18  })
            2'bz1:
                \$next\fifo32_we  = 1'h1;
            2'b1z:
                \$next\fifo32_we  = 1'h0;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fifo32_we  = 1'h0;
    endcase
  end
  assign fifo32_re = \$next\fifo32_re ;
  assign data_out = \$next\data_out ;
  assign valid_out = \$next\valid_out ;
endmodule

