/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(pixel_in, predic_in, \pixel_in$1 , \predic_in$2 , end_in, rst, clk, val_out, \val_out$3 , \val_out$4 , \val_out$5 , valid_out, end_out, valid_in);
  wire [17:0] \$10 ;
  wire [16:0] \$11 ;
  wire [17:0] \$13 ;
  wire [17:0] \$15 ;
  wire [16:0] \$16 ;
  wire [17:0] \$18 ;
  wire [16:0] \$6 ;
  wire [16:0] \$8 ;
  (* src = "./migen_src/difference.py:72" *)
  reg \$next\end_out ;
  (* src = "./migen_src/difference.py:64" *)
  reg [16:0] \$next\val_out ;
  (* src = "./migen_src/difference.py:64" *)
  reg [16:0] \$next\val_out$3 ;
  (* src = "./migen_src/difference.py:61" *)
  reg [16:0] \$next\val_out$4 ;
  (* src = "./migen_src/difference.py:61" *)
  reg [16:0] \$next\val_out$5 ;
  (* src = "./migen_src/difference.py:68" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/difference.py:71" *)
  input end_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/difference.py:72" *)
  output end_out;
  reg end_out = 1'h0;
  (* src = "./migen_src/difference.py:55" *)
  input [15:0] pixel_in;
  (* src = "./migen_src/difference.py:55" *)
  input [15:0] \pixel_in$1 ;
  (* src = "./migen_src/difference.py:58" *)
  input [15:0] predic_in;
  (* src = "./migen_src/difference.py:58" *)
  input [15:0] \predic_in$2 ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:64" *)
  output [16:0] val_out;
  reg [16:0] val_out = 17'h00000;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:64" *)
  output [16:0] \val_out$3 ;
  reg [16:0] \val_out$3  = 17'h00000;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:61" *)
  output [16:0] \val_out$4 ;
  reg [16:0] \val_out$4  = 17'h00000;
  (* init = 17'h00000 *)
  (* src = "./migen_src/difference.py:61" *)
  output [16:0] \val_out$5 ;
  reg [16:0] \val_out$5  = 17'h00000;
  (* src = "./migen_src/difference.py:67" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/difference.py:68" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$11  = pixel_in - (* src = "./migen_src/difference.py:90" *) predic_in;
  assign \$13  = \$11  - (* src = "./migen_src/difference.py:90" *) 1'h1;
  assign \$16  = \pixel_in$1  - (* src = "./migen_src/difference.py:90" *) \predic_in$2 ;
  assign \$18  = \$16  - (* src = "./migen_src/difference.py:90" *) 1'h1;
  assign \$6  = pixel_in - (* src = "./migen_src/difference.py:89" *) predic_in;
  assign \$8  = \pixel_in$1  - (* src = "./migen_src/difference.py:89" *) \predic_in$2 ;
  always @(posedge clk)
      end_out <= \$next\end_out ;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      \val_out$3  <= \$next\val_out$3 ;
  always @(posedge clk)
      val_out <= \$next\val_out ;
  always @(posedge clk)
      \val_out$5  <= \$next\val_out$5 ;
  always @(posedge clk)
      \val_out$4  <= \$next\val_out$4 ;
  always @* begin
    \$next\val_out$4  = \val_out$4 ;
    casez (valid_in)
      1'h1:
          \$next\val_out$4  = \$6 ;
    endcase
    casez (rst)
      1'h1:
          \$next\val_out$4  = 17'h00000;
    endcase
  end
  always @* begin
    \$next\val_out$5  = \val_out$5 ;
    casez (valid_in)
      1'h1:
          \$next\val_out$5  = \$8 ;
    endcase
    casez (rst)
      1'h1:
          \$next\val_out$5  = 17'h00000;
    endcase
  end
  always @* begin
    \$next\val_out  = val_out;
    casez (valid_in)
      1'h1:
          \$next\val_out  = \$10 [16:0];
    endcase
    casez (rst)
      1'h1:
          \$next\val_out  = 17'h00000;
    endcase
  end
  always @* begin
    \$next\val_out$3  = \val_out$3 ;
    casez (valid_in)
      1'h1:
          \$next\val_out$3  = \$15 [16:0];
    endcase
    casez (rst)
      1'h1:
          \$next\val_out$3  = 17'h00000;
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
  always @* begin
    \$next\end_out  = end_out;
    \$next\end_out  = end_in;
    casez (rst)
      1'h1:
          \$next\end_out  = 1'h0;
    endcase
  end
  assign \$10  = \$13 ;
  assign \$15  = \$18 ;
endmodule

