/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(new_row, pixel_in, \pixel_in$1 , rst, clk, pixel_out, \pixel_out$2 , predic_out, \predic_out$3 , valid_out, valid_in);
  wire \$10 ;
  wire \$12 ;
  wire \$14 ;
  wire \$16 ;
  wire [1:0] \$18 ;
  wire [1:0] \$19 ;
  wire [1:0] \$24 ;
  wire [1:0] \$25 ;
  wire \$4 ;
  wire \$6 ;
  wire \$8 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] \$next\buff ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] \$next\buff$21 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] \$next\buff$22 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] \$next\buff$23 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:62" *)
  reg \$next\buff_ctr ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] \$next\lbuff ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] \$next\lbuff$27 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] \$next\lbuff$28 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] \$next\lbuff$29 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:63" *)
  reg \$next\lbuff_ctr ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:66" *)
  reg \$next\new_row_latch ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:65" *)
  reg \$next\new_row_reg ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:34" *)
  reg [15:0] \$next\pixel_out ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:34" *)
  reg [15:0] \$next\pixel_out$2 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:37" *)
  reg [15:0] \$next\predic_out ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:37" *)
  reg [15:0] \$next\predic_out$3 ;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:44" *)
  reg \$next\valid_out ;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] buff = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] \buff$21  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] \buff$22  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:57" *)
  reg [15:0] \buff$23  = 16'h8000;
  (* init = 1'h0 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:62" *)
  reg buff_ctr = 1'h0;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] lbuff = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] \lbuff$27  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] \lbuff$28  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:60" *)
  reg [15:0] \lbuff$29  = 16'h8000;
  (* init = 1'h0 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:63" *)
  reg lbuff_ctr = 1'h0;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:40" *)
  input new_row;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:66" *)
  wire new_row_latch;
  (* init = 1'h0 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:65" *)
  reg new_row_reg = 1'h0;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:31" *)
  input [15:0] pixel_in;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:31" *)
  input [15:0] \pixel_in$1 ;
  (* init = 16'h0000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:34" *)
  output [15:0] pixel_out;
  reg [15:0] pixel_out = 16'h0000;
  (* init = 16'h0000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:34" *)
  output [15:0] \pixel_out$2 ;
  reg [15:0] \pixel_out$2  = 16'h0000;
  (* init = 16'h0000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:37" *)
  output [15:0] predic_out;
  reg [15:0] predic_out = 16'h0000;
  (* init = 16'h0000 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:37" *)
  output [15:0] \predic_out$3 ;
  reg [15:0] \predic_out$3  = 16'h0000;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:43" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/predictor_p1_c4_pix1_2.py:44" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$10  = valid_in == (* src = "./migen_src/predictor_p1_c4_pix1_2.py:71" *) 1'h1;
  assign \$12  = lbuff_ctr == (* src = "./migen_src/predictor_p1_c4_pix1_2.py:71" *) 1'h1;
  assign \$14  = \$10  & (* src = "./migen_src/predictor_p1_c4_pix1_2.py:71" *) \$12 ;
  assign \$16  = new_row | (* src = "./migen_src/predictor_p1_c4_pix1_2.py:73" *) new_row_reg;
  assign \$19  = buff_ctr + (* src = "./migen_src/predictor_p1_c4_pix1_2.py:82" *) 1'h1;
  assign \$25  = lbuff_ctr + (* src = "./migen_src/predictor_p1_c4_pix1_2.py:91" *) 1'h1;
  assign \$4  = valid_in == (* src = "./migen_src/predictor_p1_c4_pix1_2.py:69" *) 1'h1;
  assign \$6  = new_row == (* src = "./migen_src/predictor_p1_c4_pix1_2.py:69" *) 1'h1;
  assign \$8  = \$4  & (* src = "./migen_src/predictor_p1_c4_pix1_2.py:69" *) \$6 ;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      \buff$22  <= \$next\buff$22 ;
  always @(posedge clk)
      \buff$21  <= \$next\buff$21 ;
  always @(posedge clk)
      buff <= \$next\buff ;
  always @(posedge clk)
      buff_ctr <= \$next\buff_ctr ;
  always @(posedge clk)
      \pixel_out$2  <= \$next\pixel_out$2 ;
  always @(posedge clk)
      pixel_out <= \$next\pixel_out ;
  always @(posedge clk)
      new_row_reg <= \$next\new_row_reg ;
  always @(posedge clk)
      \predic_out$3  <= \$next\predic_out$3 ;
  always @(posedge clk)
      predic_out <= \$next\predic_out ;
  always @(posedge clk)
      \lbuff$29  <= \$next\lbuff$29 ;
  always @(posedge clk)
      \lbuff$28  <= \$next\lbuff$28 ;
  always @(posedge clk)
      \lbuff$27  <= \$next\lbuff$27 ;
  always @(posedge clk)
      lbuff <= \$next\lbuff ;
  always @(posedge clk)
      lbuff_ctr <= \$next\lbuff_ctr ;
  always @(posedge clk)
      \buff$23  <= \$next\buff$23 ;
  always @* begin
    \$next\new_row_reg  = new_row_reg;
    casez ({ \$14 , \$8  })
      2'bz1:
          \$next\new_row_reg  = 1'h1;
      2'b1z:
          \$next\new_row_reg  = 1'h0;
    endcase
    casez (rst)
      1'h1:
          \$next\new_row_reg  = 1'h0;
    endcase
  end
  always @* begin
    \$next\new_row_latch  = 1'h0;
    \$next\new_row_latch  = \$16 ;
  end
  always @* begin
    \$next\lbuff  = lbuff;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h0:
                      \$next\lbuff  = pixel_in;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\lbuff$27  = \lbuff$27 ;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h0:
                      \$next\lbuff$27  = \pixel_in$1 ;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff$27  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\lbuff$28  = \lbuff$28 ;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h1:
                      \$next\lbuff$28  = pixel_in;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff$28  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\lbuff$29  = \lbuff$29 ;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h1:
                      \$next\lbuff$29  = \pixel_in$1 ;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff$29  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\predic_out  = predic_out;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h0:
                      \$next\predic_out  = lbuff;
                  1'h1:
                      \$next\predic_out  = \lbuff$28 ;
                endcase
            1'hz:
                casez (buff_ctr)
                  1'h0:
                      \$next\predic_out  = buff;
                  1'h1:
                      \$next\predic_out  = \buff$22 ;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\predic_out  = 16'h0000;
    endcase
  end
  always @* begin
    \$next\predic_out$3  = \predic_out$3 ;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h0:
                      \$next\predic_out$3  = \lbuff$27 ;
                  1'h1:
                      \$next\predic_out$3  = \lbuff$29 ;
                endcase
            1'hz:
                casez (buff_ctr)
                  1'h0:
                      \$next\predic_out$3  = \buff$21 ;
                  1'h1:
                      \$next\predic_out$3  = \buff$23 ;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\predic_out$3  = 16'h0000;
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
    \$next\pixel_out  = pixel_out;
    casez (valid_in)
      1'h1:
          \$next\pixel_out  = pixel_in;
    endcase
    casez (rst)
      1'h1:
          \$next\pixel_out  = 16'h0000;
    endcase
  end
  always @* begin
    \$next\pixel_out$2  = \pixel_out$2 ;
    casez (valid_in)
      1'h1:
          \$next\pixel_out$2  = \pixel_in$1 ;
    endcase
    casez (rst)
      1'h1:
          \$next\pixel_out$2  = 16'h0000;
    endcase
  end
  always @* begin
    \$next\buff_ctr  = buff_ctr;
    casez (valid_in)
      1'h1:
          \$next\buff_ctr  = \$18 [0];
    endcase
    casez (rst)
      1'h1:
          \$next\buff_ctr  = 1'h0;
    endcase
  end
  always @* begin
    \$next\buff  = buff;
    casez (valid_in)
      1'h1:
          casez (buff_ctr)
            1'h0:
                \$next\buff  = pixel_in;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\buff$21  = \buff$21 ;
    casez (valid_in)
      1'h1:
          casez (buff_ctr)
            1'h0:
                \$next\buff$21  = \pixel_in$1 ;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff$21  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\buff$22  = \buff$22 ;
    casez (valid_in)
      1'h1:
          casez (buff_ctr)
            1'h1:
                \$next\buff$22  = pixel_in;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff$22  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\buff$23  = \buff$23 ;
    casez (valid_in)
      1'h1:
          casez (buff_ctr)
            1'h1:
                \$next\buff$23  = \pixel_in$1 ;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff$23  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\lbuff_ctr  = lbuff_ctr;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                \$next\lbuff_ctr  = \$24 [0];
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff_ctr  = 1'h0;
    endcase
  end
  assign \$18  = \$19 ;
  assign \$24  = \$25 ;
  assign new_row_latch = \$next\new_row_latch ;
endmodule

