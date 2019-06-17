/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top.fifo" *)
(* generator = "nMigen" *)
module fifo(we, re, rst, clk, dout, readable, level, din);
  wire \$1 ;
  wire \$3 ;
  wire \$5 ;
  wire [7:0] \$7 ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:69" *)
  reg [68:0] \$next\dout ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:238" *)
  reg [7:0] \$next\level ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:70" *)
  reg \$next\readable ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:65" *)
  reg [68:0] \$next\unbuffered_din ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:71" *)
  reg \$next\unbuffered_re ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:139" *)
  reg \$next\unbuffered_replace ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:67" *)
  reg \$next\unbuffered_we ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:66" *)
  reg \$next\writable ;
  (* init = 1'h0 *)
  reg \$verilog_initial_trigger  = 1'h0;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:97" *)
  input clk;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:65" *)
  input [68:0] din;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:69" *)
  output [68:0] dout;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:238" *)
  output [7:0] level;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:71" *)
  input re;
  (* init = 1'h0 *)
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:70" *)
  output readable;
  reg readable = 1'h0;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:65" *)
  wire [68:0] unbuffered_din;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:69" *)
  wire [68:0] unbuffered_dout;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:138" *)
  wire [6:0] unbuffered_level;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:71" *)
  wire unbuffered_re;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:70" *)
  wire unbuffered_readable;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:139" *)
  wire unbuffered_replace;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:67" *)
  wire unbuffered_we;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:66" *)
  wire unbuffered_writable;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:67" *)
  input we;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:66" *)
  wire writable;
  assign \$1  = ~ (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:256" *) readable;
  assign \$3  = \$1  | (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:256" *) re;
  assign \$5  = unbuffered_readable & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:256" *) \$3 ;
  assign \$7  = unbuffered_level + (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:263" *) readable;
  always @(posedge clk)
      readable <= \$next\readable ;
  unbuffered unbuffered (
    .clk(clk),
    .din(unbuffered_din),
    .dout(unbuffered_dout),
    .level(unbuffered_level),
    .re(unbuffered_re),
    .readable(unbuffered_readable),
    .replace(unbuffered_replace),
    .rst(rst),
    .we(unbuffered_we),
    .writable(unbuffered_writable)
  );
  always @* begin
    \$next\unbuffered_din  = 69'h000000000000000000;
    \$next\unbuffered_din  = din;
  end
  always @* begin
    \$next\unbuffered_we  = 1'h0;
    \$next\unbuffered_we  = we;
  end
  always @* begin
    \$next\writable  = 1'h0;
    \$next\writable  = unbuffered_writable;
  end
  always @* begin
    \$next\unbuffered_replace  = 1'h0;
    \$next\unbuffered_replace  = 1'h0;
    \$verilog_initial_trigger  = \$verilog_initial_trigger ;
  end
  always @* begin
    \$next\dout  = 69'h000000000000000000;
    \$next\dout  = unbuffered_dout;
  end
  always @* begin
    \$next\unbuffered_re  = 1'h0;
    \$next\unbuffered_re  = \$5 ;
  end
  always @* begin
    \$next\readable  = readable;
    casez ({ re, unbuffered_re })
      2'bz1:
          \$next\readable  = 1'h1;
      2'b1z:
          \$next\readable  = 1'h0;
    endcase
    casez (rst)
      1'h1:
          \$next\readable  = 1'h0;
    endcase
  end
  always @* begin
    \$next\level  = 8'h00;
    \$next\level  = \$7 ;
  end
  assign level = \$next\level ;
  assign unbuffered_re = \$next\unbuffered_re ;
  assign dout = \$next\dout ;
  assign unbuffered_replace = \$next\unbuffered_replace ;
  assign writable = \$next\writable ;
  assign unbuffered_we = \$next\unbuffered_we ;
  assign unbuffered_din = \$next\unbuffered_din ;
endmodule

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(enc_in, enc_in_ctr, in_end, latch_output, rst, clk, enc_out, enc_out_ctr, out_end, valid_out, close_full, valid_in);
  wire \$1 ;
  (* src = "./migen_src/lj92_pipeline_fifo.py:39" *)
  reg \$next\close_full ;
  (* src = "./migen_src/lj92_pipeline_fifo.py:32" *)
  reg [61:0] \$next\enc_out ;
  (* src = "./migen_src/lj92_pipeline_fifo.py:33" *)
  reg [5:0] \$next\enc_out_ctr ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:65" *)
  reg [68:0] \$next\fifo_din ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:71" *)
  reg \$next\fifo_re ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:67" *)
  reg \$next\fifo_we ;
  (* src = "./migen_src/lj92_pipeline_fifo.py:34" *)
  reg \$next\out_end ;
  (* src = "./migen_src/lj92_pipeline_fifo.py:35" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:97" *)
  input clk;
  (* init = 1'h0 *)
  (* src = "./migen_src/lj92_pipeline_fifo.py:39" *)
  output close_full;
  reg close_full = 1'h0;
  (* src = "./migen_src/lj92_pipeline_fifo.py:26" *)
  input [61:0] enc_in;
  (* src = "./migen_src/lj92_pipeline_fifo.py:27" *)
  input [5:0] enc_in_ctr;
  (* src = "./migen_src/lj92_pipeline_fifo.py:32" *)
  output [61:0] enc_out;
  (* src = "./migen_src/lj92_pipeline_fifo.py:33" *)
  output [5:0] enc_out_ctr;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:65" *)
  wire [68:0] fifo_din;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:69" *)
  wire [68:0] fifo_dout;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:238" *)
  wire [7:0] fifo_level;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:71" *)
  wire fifo_re;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:70" *)
  wire fifo_readable;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:67" *)
  wire fifo_we;
  (* src = "./migen_src/lj92_pipeline_fifo.py:28" *)
  input in_end;
  (* src = "./migen_src/lj92_pipeline_fifo.py:31" *)
  input latch_output;
  (* src = "./migen_src/lj92_pipeline_fifo.py:34" *)
  output out_end;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/lj92_pipeline_fifo.py:29" *)
  input valid_in;
  (* src = "./migen_src/lj92_pipeline_fifo.py:35" *)
  output valid_out;
  assign \$1  = fifo_level > (* src = "./migen_src/lj92_pipeline_fifo.py:71" *) 7'h6c;
  always @(posedge clk)
      close_full <= \$next\close_full ;
  fifo fifo (
    .clk(clk),
    .din(fifo_din),
    .dout(fifo_dout),
    .level(fifo_level),
    .re(fifo_re),
    .readable(fifo_readable),
    .rst(rst),
    .we(fifo_we)
  );
  always @* begin
    \$next\fifo_we  = 1'h0;
    \$next\fifo_we  = valid_in;
  end
  always @* begin
    \$next\fifo_din  = 69'h000000000000000000;
    \$next\fifo_din  = { in_end, enc_in_ctr, enc_in };
  end
  always @* begin
    \$next\valid_out  = 1'h0;
    \$next\valid_out  = fifo_readable;
  end
  always @* begin
    \$next\enc_out  = 62'h0000000000000000;
    \$next\enc_out  = fifo_dout[61:0];
  end
  always @* begin
    \$next\enc_out_ctr  = 6'h00;
    \$next\enc_out_ctr  = fifo_dout[67:62];
  end
  always @* begin
    \$next\out_end  = 1'h0;
    \$next\out_end  = fifo_dout[68];
  end
  always @* begin
    \$next\fifo_re  = 1'h0;
    \$next\fifo_re  = latch_output;
  end
  always @* begin
    \$next\close_full  = close_full;
    \$next\close_full  = \$1 ;
    casez (rst)
      1'h1:
          \$next\close_full  = 1'h0;
    endcase
  end
  assign fifo_re = \$next\fifo_re ;
  assign out_end = \$next\out_end ;
  assign enc_out_ctr = \$next\enc_out_ctr ;
  assign enc_out = \$next\enc_out ;
  assign valid_out = \$next\valid_out ;
  assign fifo_din = \$next\fifo_din ;
  assign fifo_we = \$next\fifo_we ;
endmodule

(* \nmigen.hierarchy  = "top.fifo.unbuffered" *)
(* generator = "nMigen" *)
module unbuffered(we, replace, re, rst, clk, writable, readable, dout, level, din);
  wire \$10 ;
  wire \$13 ;
  wire \$15 ;
  wire \$17 ;
  wire \$19 ;
  wire \$2 ;
  wire \$21 ;
  wire [7:0] \$23 ;
  wire [7:0] \$24 ;
  wire [7:0] \$26 ;
  wire \$27 ;
  wire \$30 ;
  wire [7:0] \$32 ;
  wire [7:0] \$33 ;
  wire [7:0] \$35 ;
  wire \$36 ;
  wire \$39 ;
  wire \$4 ;
  wire \$41 ;
  wire \$43 ;
  wire \$45 ;
  wire \$46 ;
  wire \$49 ;
  wire [7:0] \$51 ;
  wire [7:0] \$52 ;
  wire \$54 ;
  wire \$56 ;
  wire \$57 ;
  wire \$59 ;
  wire [7:0] \$6 ;
  wire \$61 ;
  wire \$64 ;
  wire [7:0] \$66 ;
  wire [7:0] \$67 ;
  wire [7:0] \$7 ;
  wire [7:0] \$9 ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:156" *)
  reg [6:0] \$next\consume ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:69" *)
  reg [68:0] \$next\dout ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:138" *)
  reg [6:0] \$next\level ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:155" *)
  reg [6:0] \$next\produce ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:81" *)
  reg [6:0] \$next\rdport_storage_r_addr ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:85" *)
  reg \$next\rdport_storage_r_en ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:70" *)
  reg \$next\readable ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:66" *)
  reg \$next\writable ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:146" *)
  reg [6:0] \$next\wrport_storage_w_addr ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:148" *)
  reg [68:0] \$next\wrport_storage_w_data ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:150" *)
  reg \$next\wrport_storage_w_en ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:97" *)
  input clk;
  (* init = 7'h00 *)
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:156" *)
  reg [6:0] consume = 7'h00;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:65" *)
  input [68:0] din;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:69" *)
  output [68:0] dout;
  (* init = 7'h00 *)
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:138" *)
  output [6:0] level;
  reg [6:0] level = 7'h00;
  (* init = 7'h00 *)
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:155" *)
  reg [6:0] produce = 7'h00;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:81" *)
  wire [6:0] rdport_storage_r_addr;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:83" *)
  wire [68:0] rdport_storage_r_data;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:85" *)
  wire rdport_storage_r_en;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:71" *)
  input re;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:70" *)
  output readable;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:139" *)
  input replace;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:67" *)
  input we;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:66" *)
  output writable;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:146" *)
  wire [6:0] wrport_storage_w_addr;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:148" *)
  wire [68:0] wrport_storage_w_data;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/mem.py:150" *)
  wire wrport_storage_w_en;
  assign \$10  = produce == (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:102" *) 1'h0;
  assign \$9  = \$10  ? (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:164" *) 8'h7e : \$7 ;
  assign \$13  = writable | (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:161" *) replace;
  assign \$15  = we & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:161" *) \$13 ;
  assign \$17  = writable & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) we;
  assign \$19  = ~ (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) replace;
  assign \$21  = \$17  & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) \$19 ;
  assign \$24  = produce + (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:95" *) 1'h1;
  assign \$27  = produce == (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:95" *) 7'h7e;
  assign \$26  = \$27  ? (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:166" *) 8'h00 : \$24 ;
  assign \$2  = level != (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:144" *) 7'h7f;
  assign \$30  = readable & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:148" *) re;
  assign \$33  = consume + (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:95" *) 1'h1;
  assign \$36  = consume == (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:95" *) 7'h7e;
  assign \$35  = \$36  ? (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:175" *) 8'h00 : \$33 ;
  assign \$39  = writable & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) we;
  assign \$41  = ~ (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) replace;
  assign \$43  = \$39  & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) \$41 ;
  assign \$46  = readable & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:148" *) re;
  assign \$45  = ~ (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:177" *) \$46 ;
  assign \$4  = level != (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:145" *) 1'h0;
  assign \$49  = \$43  & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:177" *) \$45 ;
  assign \$52  = level + (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:178" *) 1'h1;
  assign \$54  = readable & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:148" *) re;
  assign \$57  = writable & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) we;
  assign \$59  = ~ (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) replace;
  assign \$61  = \$57  & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:149" *) \$59 ;
  assign \$56  = ~ (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:179" *) \$61 ;
  assign \$64  = \$54  & (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:179" *) \$56 ;
  assign \$67  = level - (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:180" *) 1'h1;
  assign \$7  = produce - (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/lib/fifo.py:102" *) 1'h1;
  always @(posedge clk)
      level <= \$next\level ;
  always @(posedge clk)
      consume <= \$next\consume ;
  always @(posedge clk)
      produce <= \$next\produce ;
  reg [68:0] storage [126:0];
  initial begin
    storage[0] = 69'h000000000000000000;
    storage[1] = 69'h000000000000000000;
    storage[2] = 69'h000000000000000000;
    storage[3] = 69'h000000000000000000;
    storage[4] = 69'h000000000000000000;
    storage[5] = 69'h000000000000000000;
    storage[6] = 69'h000000000000000000;
    storage[7] = 69'h000000000000000000;
    storage[8] = 69'h000000000000000000;
    storage[9] = 69'h000000000000000000;
    storage[10] = 69'h000000000000000000;
    storage[11] = 69'h000000000000000000;
    storage[12] = 69'h000000000000000000;
    storage[13] = 69'h000000000000000000;
    storage[14] = 69'h000000000000000000;
    storage[15] = 69'h000000000000000000;
    storage[16] = 69'h000000000000000000;
    storage[17] = 69'h000000000000000000;
    storage[18] = 69'h000000000000000000;
    storage[19] = 69'h000000000000000000;
    storage[20] = 69'h000000000000000000;
    storage[21] = 69'h000000000000000000;
    storage[22] = 69'h000000000000000000;
    storage[23] = 69'h000000000000000000;
    storage[24] = 69'h000000000000000000;
    storage[25] = 69'h000000000000000000;
    storage[26] = 69'h000000000000000000;
    storage[27] = 69'h000000000000000000;
    storage[28] = 69'h000000000000000000;
    storage[29] = 69'h000000000000000000;
    storage[30] = 69'h000000000000000000;
    storage[31] = 69'h000000000000000000;
    storage[32] = 69'h000000000000000000;
    storage[33] = 69'h000000000000000000;
    storage[34] = 69'h000000000000000000;
    storage[35] = 69'h000000000000000000;
    storage[36] = 69'h000000000000000000;
    storage[37] = 69'h000000000000000000;
    storage[38] = 69'h000000000000000000;
    storage[39] = 69'h000000000000000000;
    storage[40] = 69'h000000000000000000;
    storage[41] = 69'h000000000000000000;
    storage[42] = 69'h000000000000000000;
    storage[43] = 69'h000000000000000000;
    storage[44] = 69'h000000000000000000;
    storage[45] = 69'h000000000000000000;
    storage[46] = 69'h000000000000000000;
    storage[47] = 69'h000000000000000000;
    storage[48] = 69'h000000000000000000;
    storage[49] = 69'h000000000000000000;
    storage[50] = 69'h000000000000000000;
    storage[51] = 69'h000000000000000000;
    storage[52] = 69'h000000000000000000;
    storage[53] = 69'h000000000000000000;
    storage[54] = 69'h000000000000000000;
    storage[55] = 69'h000000000000000000;
    storage[56] = 69'h000000000000000000;
    storage[57] = 69'h000000000000000000;
    storage[58] = 69'h000000000000000000;
    storage[59] = 69'h000000000000000000;
    storage[60] = 69'h000000000000000000;
    storage[61] = 69'h000000000000000000;
    storage[62] = 69'h000000000000000000;
    storage[63] = 69'h000000000000000000;
    storage[64] = 69'h000000000000000000;
    storage[65] = 69'h000000000000000000;
    storage[66] = 69'h000000000000000000;
    storage[67] = 69'h000000000000000000;
    storage[68] = 69'h000000000000000000;
    storage[69] = 69'h000000000000000000;
    storage[70] = 69'h000000000000000000;
    storage[71] = 69'h000000000000000000;
    storage[72] = 69'h000000000000000000;
    storage[73] = 69'h000000000000000000;
    storage[74] = 69'h000000000000000000;
    storage[75] = 69'h000000000000000000;
    storage[76] = 69'h000000000000000000;
    storage[77] = 69'h000000000000000000;
    storage[78] = 69'h000000000000000000;
    storage[79] = 69'h000000000000000000;
    storage[80] = 69'h000000000000000000;
    storage[81] = 69'h000000000000000000;
    storage[82] = 69'h000000000000000000;
    storage[83] = 69'h000000000000000000;
    storage[84] = 69'h000000000000000000;
    storage[85] = 69'h000000000000000000;
    storage[86] = 69'h000000000000000000;
    storage[87] = 69'h000000000000000000;
    storage[88] = 69'h000000000000000000;
    storage[89] = 69'h000000000000000000;
    storage[90] = 69'h000000000000000000;
    storage[91] = 69'h000000000000000000;
    storage[92] = 69'h000000000000000000;
    storage[93] = 69'h000000000000000000;
    storage[94] = 69'h000000000000000000;
    storage[95] = 69'h000000000000000000;
    storage[96] = 69'h000000000000000000;
    storage[97] = 69'h000000000000000000;
    storage[98] = 69'h000000000000000000;
    storage[99] = 69'h000000000000000000;
    storage[100] = 69'h000000000000000000;
    storage[101] = 69'h000000000000000000;
    storage[102] = 69'h000000000000000000;
    storage[103] = 69'h000000000000000000;
    storage[104] = 69'h000000000000000000;
    storage[105] = 69'h000000000000000000;
    storage[106] = 69'h000000000000000000;
    storage[107] = 69'h000000000000000000;
    storage[108] = 69'h000000000000000000;
    storage[109] = 69'h000000000000000000;
    storage[110] = 69'h000000000000000000;
    storage[111] = 69'h000000000000000000;
    storage[112] = 69'h000000000000000000;
    storage[113] = 69'h000000000000000000;
    storage[114] = 69'h000000000000000000;
    storage[115] = 69'h000000000000000000;
    storage[116] = 69'h000000000000000000;
    storage[117] = 69'h000000000000000000;
    storage[118] = 69'h000000000000000000;
    storage[119] = 69'h000000000000000000;
    storage[120] = 69'h000000000000000000;
    storage[121] = 69'h000000000000000000;
    storage[122] = 69'h000000000000000000;
    storage[123] = 69'h000000000000000000;
    storage[124] = 69'h000000000000000000;
    storage[125] = 69'h000000000000000000;
    storage[126] = 69'h000000000000000000;
  end
  reg [68:0] _0_;
  always @(posedge clk) begin
    if (\$next\rdport_storage_r_en ) _0_ <= storage[\$next\rdport_storage_r_addr ];
    if (\$next\wrport_storage_w_en ) storage[\$next\wrport_storage_w_addr ] <= \$next\wrport_storage_w_data ;
  end
  assign rdport_storage_r_data = _0_;
  always @* begin
    \$next\writable  = 1'h0;
    \$next\writable  = \$2 ;
  end
  always @* begin
    \$next\readable  = 1'h0;
    \$next\readable  = \$4 ;
  end
  always @* begin
    \$next\level  = level;
    casez (\$49 )
      1'h1:
          \$next\level  = \$51 [6:0];
    endcase
    casez (\$64 )
      1'h1:
          \$next\level  = \$66 [6:0];
    endcase
    casez (rst)
      1'h1:
          \$next\level  = 7'h00;
    endcase
  end
  always @* begin
    \$next\wrport_storage_w_addr  = 7'h00;
    \$next\wrport_storage_w_addr  = produce;
    casez (replace)
      1'h1:
          \$next\wrport_storage_w_addr  = \$6 [6:0];
    endcase
  end
  always @* begin
    \$next\wrport_storage_w_data  = 69'h000000000000000000;
    \$next\wrport_storage_w_data  = din;
  end
  always @* begin
    \$next\wrport_storage_w_en  = 1'h0;
    \$next\wrport_storage_w_en  = \$15 ;
  end
  always @* begin
    \$next\produce  = produce;
    casez (\$21 )
      1'h1:
          \$next\produce  = \$23 [6:0];
    endcase
    casez (rst)
      1'h1:
          \$next\produce  = 7'h00;
    endcase
  end
  always @* begin
    \$next\rdport_storage_r_addr  = 7'h00;
    \$next\rdport_storage_r_addr  = consume;
  end
  always @* begin
    \$next\dout  = 69'h000000000000000000;
    \$next\dout  = rdport_storage_r_data;
  end
  always @* begin
    \$next\rdport_storage_r_en  = 1'h0;
    \$next\rdport_storage_r_en  = re;
  end
  always @* begin
    \$next\consume  = consume;
    casez (\$30 )
      1'h1:
          \$next\consume  = \$32 [6:0];
    endcase
    casez (rst)
      1'h1:
          \$next\consume  = 7'h00;
    endcase
  end
  assign \$6  = \$9 ;
  assign \$23  = \$26 ;
  assign \$32  = \$35 ;
  assign \$51  = \$52 ;
  assign \$66  = \$67 ;
  assign rdport_storage_r_en = \$next\rdport_storage_r_en ;
  assign dout = \$next\dout ;
  assign rdport_storage_r_addr = \$next\rdport_storage_r_addr ;
  assign wrport_storage_w_en = \$next\wrport_storage_w_en ;
  assign wrport_storage_w_data = \$next\wrport_storage_w_data ;
  assign wrport_storage_w_addr = \$next\wrport_storage_w_addr ;
  assign readable = \$next\readable ;
  assign writable = \$next\writable ;
endmodule

