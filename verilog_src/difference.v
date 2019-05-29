/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(pixel_in1, predic_in1, pixel_in2, predic_in2, pixel_in3, predic_in3, pixel_in4, predic_in4, rst, clk, val_out1, val_out2, val_out3, val_out4, valid_out, valid_in);
  wire [16:0] \$1 ;
  wire [16:0] \$3 ;
  wire [16:0] \$5 ;
  wire [16:0] \$7 ;
  (* src = "./migen_src/difference.py:22" *)
  reg [16:0] \$next\val_out1 ;
  (* src = "./migen_src/difference.py:23" *)
  reg [16:0] \$next\val_out2 ;
  (* src = "./migen_src/difference.py:24" *)
  reg [16:0] \$next\val_out3 ;
  (* src = "./migen_src/difference.py:25" *)
  reg [16:0] \$next\val_out4 ;
  (* src = "./migen_src/difference.py:28" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/difference.py:12" *)
  input [15:0] pixel_in1;
  (* src = "./migen_src/difference.py:13" *)
  input [15:0] pixel_in2;
  (* src = "./migen_src/difference.py:14" *)
  input [15:0] pixel_in3;
  (* src = "./migen_src/difference.py:15" *)
  input [15:0] pixel_in4;
  (* src = "./migen_src/difference.py:17" *)
  input [15:0] predic_in1;
  (* src = "./migen_src/difference.py:18" *)
  input [15:0] predic_in2;
  (* src = "./migen_src/difference.py:19" *)
  input [15:0] predic_in3;
  (* src = "./migen_src/difference.py:20" *)
  input [15:0] predic_in4;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:22" *)
  output [16:0] val_out1;
  reg [16:0] val_out1 = 17'h00000;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:23" *)
  output [16:0] val_out2;
  reg [16:0] val_out2 = 17'h00000;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:24" *)
  output [16:0] val_out3;
  reg [16:0] val_out3 = 17'h00000;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:25" *)
  output [16:0] val_out4;
  reg [16:0] val_out4 = 17'h00000;
  (* src = "./migen_src/difference.py:27" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/difference.py:28" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$1  = pixel_in1 - (* src = "./migen_src/difference.py:44" *) predic_in1;
  assign \$3  = pixel_in2 - (* src = "./migen_src/difference.py:45" *) predic_in2;
  assign \$5  = pixel_in3 - (* src = "./migen_src/difference.py:46" *) predic_in3;
  assign \$7  = pixel_in4 - (* src = "./migen_src/difference.py:47" *) predic_in4;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      val_out4 <= \$next\val_out4 ;
  always @(posedge clk)
      val_out3 <= \$next\val_out3 ;
  always @(posedge clk)
      val_out2 <= \$next\val_out2 ;
  always @(posedge clk)
      val_out1 <= \$next\val_out1 ;
  always @* begin
    \$next\val_out1  = val_out1;
    casez (valid_in)
      1'h1:
          \$next\val_out1  = \$1 ;
    endcase
    casez (rst)
      1'h1:
          \$next\val_out1  = 17'h00000;
    endcase
  end
  always @* begin
    \$next\val_out2  = val_out2;
    casez (valid_in)
      1'h1:
          \$next\val_out2  = \$3 ;
    endcase
    casez (rst)
      1'h1:
          \$next\val_out2  = 17'h00000;
    endcase
  end
  always @* begin
    \$next\val_out3  = val_out3;
    casez (valid_in)
      1'h1:
          \$next\val_out3  = \$5 ;
    endcase
    casez (rst)
      1'h1:
          \$next\val_out3  = 17'h00000;
    endcase
  end
  always @* begin
    \$next\val_out4  = val_out4;
    casez (valid_in)
      1'h1:
          \$next\val_out4  = \$7 ;
    endcase
    casez (rst)
      1'h1:
          \$next\val_out4  = 17'h00000;
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

