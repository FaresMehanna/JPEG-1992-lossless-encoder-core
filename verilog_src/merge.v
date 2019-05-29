/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top.merger_lvl1_1" *)
(* generator = "nMigen" *)
module merger_lvl1_1(enc_in_ctr1, enc_in_ctr2, enc_in1, enc_in2, rst, clk, enc_out_ctr, enc_out, valid_out, valid_in);
  wire [5:0] \$1 ;
  wire [61:0] \$3 ;
  wire [61:0] \$5 ;
  (* src = "./migen_src/merge.py:17" *)
  reg [61:0] \$next\enc_out ;
  (* src = "./migen_src/merge.py:18" *)
  reg [5:0] \$next\enc_out_ctr ;
  (* src = "./migen_src/merge.py:21" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/merge.py:11" *)
  input [30:0] enc_in1;
  (* src = "./migen_src/merge.py:14" *)
  input [30:0] enc_in2;
  (* src = "./migen_src/merge.py:12" *)
  input [4:0] enc_in_ctr1;
  (* src = "./migen_src/merge.py:15" *)
  input [4:0] enc_in_ctr2;
  (* init = 62'h0000000000000000 *)
  (* src = "./migen_src/merge.py:17" *)
  output [61:0] enc_out;
  reg [61:0] enc_out = 62'h0000000000000000;
  (* init = 6'h00 *)
  (* src = "./migen_src/merge.py:18" *)
  output [5:0] enc_out_ctr;
  reg [5:0] enc_out_ctr = 6'h00;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/merge.py:20" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/merge.py:21" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$1  = enc_in_ctr1 + (* src = "./migen_src/merge.py:35" *) enc_in_ctr2;
  assign \$3  = enc_in1 <<< (* src = "./migen_src/merge.py:36" *) enc_in_ctr2;
  assign \$5  = \$3  | (* src = "./migen_src/merge.py:36" *) enc_in2;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      enc_out <= \$next\enc_out ;
  always @(posedge clk)
      enc_out_ctr <= \$next\enc_out_ctr ;
  always @* begin
    \$next\enc_out_ctr  = enc_out_ctr;
    casez (valid_in)
      1'h1:
          \$next\enc_out_ctr  = \$1 ;
    endcase
    casez (rst)
      1'h1:
          \$next\enc_out_ctr  = 6'h00;
    endcase
  end
  always @* begin
    \$next\enc_out  = enc_out;
    casez (valid_in)
      1'h1:
          \$next\enc_out  = \$5 ;
    endcase
    casez (rst)
      1'h1:
          \$next\enc_out  = 62'h0000000000000000;
    endcase
  end
  always @* begin
    \$next\valid_out  = valid_out;
    \$next\valid_out  = valid_in;
    casez (rst)
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
  end
endmodule

(* \nmigen.hierarchy  = "top.merger_lvl1_2" *)
(* generator = "nMigen" *)
module merger_lvl1_2(enc_in_ctr1, enc_in_ctr2, enc_in1, enc_in2, rst, clk, enc_out_ctr, enc_out, valid_in);
  wire [5:0] \$1 ;
  wire [61:0] \$3 ;
  wire [61:0] \$5 ;
  (* src = "./migen_src/merge.py:17" *)
  reg [61:0] \$next\enc_out ;
  (* src = "./migen_src/merge.py:18" *)
  reg [5:0] \$next\enc_out_ctr ;
  (* src = "./migen_src/merge.py:21" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/merge.py:11" *)
  input [30:0] enc_in1;
  (* src = "./migen_src/merge.py:14" *)
  input [30:0] enc_in2;
  (* src = "./migen_src/merge.py:12" *)
  input [4:0] enc_in_ctr1;
  (* src = "./migen_src/merge.py:15" *)
  input [4:0] enc_in_ctr2;
  (* init = 62'h0000000000000000 *)
  (* src = "./migen_src/merge.py:17" *)
  output [61:0] enc_out;
  reg [61:0] enc_out = 62'h0000000000000000;
  (* init = 6'h00 *)
  (* src = "./migen_src/merge.py:18" *)
  output [5:0] enc_out_ctr;
  reg [5:0] enc_out_ctr = 6'h00;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/merge.py:20" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/merge.py:21" *)
  reg valid_out = 1'h0;
  assign \$1  = enc_in_ctr1 + (* src = "./migen_src/merge.py:35" *) enc_in_ctr2;
  assign \$3  = enc_in1 <<< (* src = "./migen_src/merge.py:36" *) enc_in_ctr2;
  assign \$5  = \$3  | (* src = "./migen_src/merge.py:36" *) enc_in2;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      enc_out <= \$next\enc_out ;
  always @(posedge clk)
      enc_out_ctr <= \$next\enc_out_ctr ;
  always @* begin
    \$next\enc_out_ctr  = enc_out_ctr;
    casez (valid_in)
      1'h1:
          \$next\enc_out_ctr  = \$1 ;
    endcase
    casez (rst)
      1'h1:
          \$next\enc_out_ctr  = 6'h00;
    endcase
  end
  always @* begin
    \$next\enc_out  = enc_out;
    casez (valid_in)
      1'h1:
          \$next\enc_out  = \$5 ;
    endcase
    casez (rst)
      1'h1:
          \$next\enc_out  = 62'h0000000000000000;
    endcase
  end
  always @* begin
    \$next\valid_out  = valid_out;
    \$next\valid_out  = valid_in;
    casez (rst)
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
  end
endmodule

(* \nmigen.hierarchy  = "top.merger_lvl2" *)
(* generator = "nMigen" *)
module merger_lvl2(enc_in_ctr1, enc_in_ctr2, enc_in1, enc_in2, rst, clk, enc_out_ctr, enc_out, valid_out, valid_in);
  wire [6:0] \$1 ;
  wire [124:0] \$3 ;
  wire [124:0] \$4 ;
  wire [124:0] \$6 ;
  (* src = "./migen_src/merge.py:17" *)
  reg [123:0] \$next\enc_out ;
  (* src = "./migen_src/merge.py:18" *)
  reg [6:0] \$next\enc_out_ctr ;
  (* src = "./migen_src/merge.py:21" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/merge.py:11" *)
  input [61:0] enc_in1;
  (* src = "./migen_src/merge.py:14" *)
  input [61:0] enc_in2;
  (* src = "./migen_src/merge.py:12" *)
  input [5:0] enc_in_ctr1;
  (* src = "./migen_src/merge.py:15" *)
  input [5:0] enc_in_ctr2;
  (* init = 124'h0000000000000000000000000000000 *)
  (* src = "./migen_src/merge.py:17" *)
  output [123:0] enc_out;
  reg [123:0] enc_out = 124'h0000000000000000000000000000000;
  (* init = 7'h00 *)
  (* src = "./migen_src/merge.py:18" *)
  output [6:0] enc_out_ctr;
  reg [6:0] enc_out_ctr = 7'h00;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/merge.py:20" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/merge.py:21" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$1  = enc_in_ctr1 + (* src = "./migen_src/merge.py:35" *) enc_in_ctr2;
  assign \$4  = enc_in1 <<< (* src = "./migen_src/merge.py:36" *) enc_in_ctr2;
  assign \$6  = \$4  | (* src = "./migen_src/merge.py:36" *) enc_in2;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      enc_out <= \$next\enc_out ;
  always @(posedge clk)
      enc_out_ctr <= \$next\enc_out_ctr ;
  always @* begin
    \$next\enc_out_ctr  = enc_out_ctr;
    casez (valid_in)
      1'h1:
          \$next\enc_out_ctr  = \$1 ;
    endcase
    casez (rst)
      1'h1:
          \$next\enc_out_ctr  = 7'h00;
    endcase
  end
  always @* begin
    \$next\enc_out  = enc_out;
    casez (valid_in)
      1'h1:
          \$next\enc_out  = \$3 [123:0];
    endcase
    casez (rst)
      1'h1:
          \$next\enc_out  = 124'h0000000000000000000000000000000;
    endcase
  end
  always @* begin
    \$next\valid_out  = valid_out;
    \$next\valid_out  = valid_in;
    casez (rst)
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
  end
  assign \$3  = \$6 ;
endmodule

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(enc_in_ctr1, enc_in2, enc_in_ctr2, valid_in, enc_in3, enc_in_ctr3, enc_in4, enc_in_ctr4, rst, clk, enc_out, enc_out_ctr, valid_out, enc_in1);
  (* src = "./migen_src/merge.py:57" *)
  reg [123:0] \$next\enc_out ;
  (* src = "./migen_src/merge.py:58" *)
  reg [6:0] \$next\enc_out_ctr ;
  (* src = "./migen_src/merge.py:11" *)
  reg [30:0] \$next\merger_lvl1_1_enc_in1 ;
  (* src = "./migen_src/merge.py:14" *)
  reg [30:0] \$next\merger_lvl1_1_enc_in2 ;
  (* src = "./migen_src/merge.py:12" *)
  reg [4:0] \$next\merger_lvl1_1_enc_in_ctr1 ;
  (* src = "./migen_src/merge.py:15" *)
  reg [4:0] \$next\merger_lvl1_1_enc_in_ctr2 ;
  (* src = "./migen_src/merge.py:20" *)
  reg \$next\merger_lvl1_1_valid_in ;
  (* src = "./migen_src/merge.py:11" *)
  reg [30:0] \$next\merger_lvl1_2_enc_in1 ;
  (* src = "./migen_src/merge.py:14" *)
  reg [30:0] \$next\merger_lvl1_2_enc_in2 ;
  (* src = "./migen_src/merge.py:12" *)
  reg [4:0] \$next\merger_lvl1_2_enc_in_ctr1 ;
  (* src = "./migen_src/merge.py:15" *)
  reg [4:0] \$next\merger_lvl1_2_enc_in_ctr2 ;
  (* src = "./migen_src/merge.py:20" *)
  reg \$next\merger_lvl1_2_valid_in ;
  (* src = "./migen_src/merge.py:11" *)
  reg [61:0] \$next\merger_lvl2_enc_in1 ;
  (* src = "./migen_src/merge.py:14" *)
  reg [61:0] \$next\merger_lvl2_enc_in2 ;
  (* src = "./migen_src/merge.py:12" *)
  reg [5:0] \$next\merger_lvl2_enc_in_ctr1 ;
  (* src = "./migen_src/merge.py:15" *)
  reg [5:0] \$next\merger_lvl2_enc_in_ctr2 ;
  (* src = "./migen_src/merge.py:20" *)
  reg \$next\merger_lvl2_valid_in ;
  (* src = "./migen_src/merge.py:61" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/merge.py:48" *)
  input [30:0] enc_in1;
  (* src = "./migen_src/merge.py:50" *)
  input [30:0] enc_in2;
  (* src = "./migen_src/merge.py:52" *)
  input [30:0] enc_in3;
  (* src = "./migen_src/merge.py:54" *)
  input [30:0] enc_in4;
  (* src = "./migen_src/merge.py:49" *)
  input [4:0] enc_in_ctr1;
  (* src = "./migen_src/merge.py:51" *)
  input [4:0] enc_in_ctr2;
  (* src = "./migen_src/merge.py:53" *)
  input [4:0] enc_in_ctr3;
  (* src = "./migen_src/merge.py:55" *)
  input [4:0] enc_in_ctr4;
  (* src = "./migen_src/merge.py:57" *)
  output [123:0] enc_out;
  (* src = "./migen_src/merge.py:58" *)
  output [6:0] enc_out_ctr;
  (* src = "./migen_src/merge.py:11" *)
  wire [30:0] merger_lvl1_1_enc_in1;
  (* src = "./migen_src/merge.py:14" *)
  wire [30:0] merger_lvl1_1_enc_in2;
  (* src = "./migen_src/merge.py:12" *)
  wire [4:0] merger_lvl1_1_enc_in_ctr1;
  (* src = "./migen_src/merge.py:15" *)
  wire [4:0] merger_lvl1_1_enc_in_ctr2;
  (* src = "./migen_src/merge.py:17" *)
  wire [61:0] merger_lvl1_1_enc_out;
  (* src = "./migen_src/merge.py:18" *)
  wire [5:0] merger_lvl1_1_enc_out_ctr;
  (* src = "./migen_src/merge.py:20" *)
  wire merger_lvl1_1_valid_in;
  (* src = "./migen_src/merge.py:21" *)
  wire merger_lvl1_1_valid_out;
  (* src = "./migen_src/merge.py:11" *)
  wire [30:0] merger_lvl1_2_enc_in1;
  (* src = "./migen_src/merge.py:14" *)
  wire [30:0] merger_lvl1_2_enc_in2;
  (* src = "./migen_src/merge.py:12" *)
  wire [4:0] merger_lvl1_2_enc_in_ctr1;
  (* src = "./migen_src/merge.py:15" *)
  wire [4:0] merger_lvl1_2_enc_in_ctr2;
  (* src = "./migen_src/merge.py:17" *)
  wire [61:0] merger_lvl1_2_enc_out;
  (* src = "./migen_src/merge.py:18" *)
  wire [5:0] merger_lvl1_2_enc_out_ctr;
  (* src = "./migen_src/merge.py:20" *)
  wire merger_lvl1_2_valid_in;
  (* src = "./migen_src/merge.py:11" *)
  wire [61:0] merger_lvl2_enc_in1;
  (* src = "./migen_src/merge.py:14" *)
  wire [61:0] merger_lvl2_enc_in2;
  (* src = "./migen_src/merge.py:12" *)
  wire [5:0] merger_lvl2_enc_in_ctr1;
  (* src = "./migen_src/merge.py:15" *)
  wire [5:0] merger_lvl2_enc_in_ctr2;
  (* src = "./migen_src/merge.py:17" *)
  wire [123:0] merger_lvl2_enc_out;
  (* src = "./migen_src/merge.py:18" *)
  wire [6:0] merger_lvl2_enc_out_ctr;
  (* src = "./migen_src/merge.py:20" *)
  wire merger_lvl2_valid_in;
  (* src = "./migen_src/merge.py:21" *)
  wire merger_lvl2_valid_out;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/merge.py:60" *)
  input valid_in;
  (* src = "./migen_src/merge.py:61" *)
  output valid_out;
  merger_lvl1_1 merger_lvl1_1 (
    .clk(clk),
    .enc_in1(merger_lvl1_1_enc_in1),
    .enc_in2(merger_lvl1_1_enc_in2),
    .enc_in_ctr1(merger_lvl1_1_enc_in_ctr1),
    .enc_in_ctr2(merger_lvl1_1_enc_in_ctr2),
    .enc_out(merger_lvl1_1_enc_out),
    .enc_out_ctr(merger_lvl1_1_enc_out_ctr),
    .rst(rst),
    .valid_in(merger_lvl1_1_valid_in),
    .valid_out(merger_lvl1_1_valid_out)
  );
  merger_lvl1_2 merger_lvl1_2 (
    .clk(clk),
    .enc_in1(merger_lvl1_2_enc_in1),
    .enc_in2(merger_lvl1_2_enc_in2),
    .enc_in_ctr1(merger_lvl1_2_enc_in_ctr1),
    .enc_in_ctr2(merger_lvl1_2_enc_in_ctr2),
    .enc_out(merger_lvl1_2_enc_out),
    .enc_out_ctr(merger_lvl1_2_enc_out_ctr),
    .rst(rst),
    .valid_in(merger_lvl1_2_valid_in)
  );
  merger_lvl2 merger_lvl2 (
    .clk(clk),
    .enc_in1(merger_lvl2_enc_in1),
    .enc_in2(merger_lvl2_enc_in2),
    .enc_in_ctr1(merger_lvl2_enc_in_ctr1),
    .enc_in_ctr2(merger_lvl2_enc_in_ctr2),
    .enc_out(merger_lvl2_enc_out),
    .enc_out_ctr(merger_lvl2_enc_out_ctr),
    .rst(rst),
    .valid_in(merger_lvl2_valid_in),
    .valid_out(merger_lvl2_valid_out)
  );
  always @* begin
    \$next\merger_lvl1_1_enc_in1  = 31'h00000000;
    \$next\merger_lvl1_1_enc_in1  = enc_in1;
  end
  always @* begin
    \$next\merger_lvl1_1_enc_in_ctr1  = 5'h00;
    \$next\merger_lvl1_1_enc_in_ctr1  = enc_in_ctr1;
  end
  always @* begin
    \$next\merger_lvl2_enc_in1  = 62'h0000000000000000;
    \$next\merger_lvl2_enc_in1  = merger_lvl1_1_enc_out;
  end
  always @* begin
    \$next\merger_lvl2_enc_in_ctr1  = 6'h00;
    \$next\merger_lvl2_enc_in_ctr1  = merger_lvl1_1_enc_out_ctr;
  end
  always @* begin
    \$next\merger_lvl2_enc_in2  = 62'h0000000000000000;
    \$next\merger_lvl2_enc_in2  = merger_lvl1_2_enc_out;
  end
  always @* begin
    \$next\merger_lvl2_enc_in_ctr2  = 6'h00;
    \$next\merger_lvl2_enc_in_ctr2  = merger_lvl1_2_enc_out_ctr;
  end
  always @* begin
    \$next\merger_lvl2_valid_in  = 1'h0;
    \$next\merger_lvl2_valid_in  = merger_lvl1_1_valid_out;
  end
  always @* begin
    \$next\enc_out  = 124'h0000000000000000000000000000000;
    \$next\enc_out  = merger_lvl2_enc_out;
  end
  always @* begin
    \$next\enc_out_ctr  = 7'h00;
    \$next\enc_out_ctr  = merger_lvl2_enc_out_ctr;
  end
  always @* begin
    \$next\valid_out  = 1'h0;
    \$next\valid_out  = merger_lvl2_valid_out;
  end
  always @* begin
    \$next\merger_lvl1_1_enc_in2  = 31'h00000000;
    \$next\merger_lvl1_1_enc_in2  = enc_in2;
  end
  always @* begin
    \$next\merger_lvl1_1_enc_in_ctr2  = 5'h00;
    \$next\merger_lvl1_1_enc_in_ctr2  = enc_in_ctr2;
  end
  always @* begin
    \$next\merger_lvl1_1_valid_in  = 1'h0;
    \$next\merger_lvl1_1_valid_in  = valid_in;
  end
  always @* begin
    \$next\merger_lvl1_2_enc_in1  = 31'h00000000;
    \$next\merger_lvl1_2_enc_in1  = enc_in3;
  end
  always @* begin
    \$next\merger_lvl1_2_enc_in_ctr1  = 5'h00;
    \$next\merger_lvl1_2_enc_in_ctr1  = enc_in_ctr3;
  end
  always @* begin
    \$next\merger_lvl1_2_enc_in2  = 31'h00000000;
    \$next\merger_lvl1_2_enc_in2  = enc_in4;
  end
  always @* begin
    \$next\merger_lvl1_2_enc_in_ctr2  = 5'h00;
    \$next\merger_lvl1_2_enc_in_ctr2  = enc_in_ctr4;
  end
  always @* begin
    \$next\merger_lvl1_2_valid_in  = 1'h0;
    \$next\merger_lvl1_2_valid_in  = valid_in;
  end
  assign valid_out = \$next\valid_out ;
  assign enc_out_ctr = \$next\enc_out_ctr ;
  assign enc_out = \$next\enc_out ;
  assign merger_lvl2_valid_in = \$next\merger_lvl2_valid_in ;
  assign merger_lvl2_enc_in_ctr2 = \$next\merger_lvl2_enc_in_ctr2 ;
  assign merger_lvl2_enc_in2 = \$next\merger_lvl2_enc_in2 ;
  assign merger_lvl2_enc_in_ctr1 = \$next\merger_lvl2_enc_in_ctr1 ;
  assign merger_lvl2_enc_in1 = \$next\merger_lvl2_enc_in1 ;
  assign merger_lvl1_2_valid_in = \$next\merger_lvl1_2_valid_in ;
  assign merger_lvl1_2_enc_in_ctr2 = \$next\merger_lvl1_2_enc_in_ctr2 ;
  assign merger_lvl1_2_enc_in2 = \$next\merger_lvl1_2_enc_in2 ;
  assign merger_lvl1_2_enc_in_ctr1 = \$next\merger_lvl1_2_enc_in_ctr1 ;
  assign merger_lvl1_2_enc_in1 = \$next\merger_lvl1_2_enc_in1 ;
  assign merger_lvl1_1_valid_in = \$next\merger_lvl1_1_valid_in ;
  assign merger_lvl1_1_enc_in_ctr2 = \$next\merger_lvl1_1_enc_in_ctr2 ;
  assign merger_lvl1_1_enc_in2 = \$next\merger_lvl1_1_enc_in2 ;
  assign merger_lvl1_1_enc_in_ctr1 = \$next\merger_lvl1_1_enc_in_ctr1 ;
  assign merger_lvl1_1_enc_in1 = \$next\merger_lvl1_1_enc_in1 ;
endmodule

