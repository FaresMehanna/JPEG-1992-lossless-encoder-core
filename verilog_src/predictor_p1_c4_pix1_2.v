/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(new_row, pixel_in, \pixel_in$1 , end_in, rst, clk, pixel_out, \pixel_out$2 , predic_out, \predic_out$3 , valid_out, end_out, debug_counter, valid_in);
  wire \$10 ;
  wire \$12 ;
  wire \$14 ;
  wire \$16 ;
  wire [32:0] \$18 ;
  wire [32:0] \$19 ;
  wire [1:0] \$21 ;
  wire [1:0] \$22 ;
  wire [1:0] \$27 ;
  wire [1:0] \$28 ;
  wire \$4 ;
  wire \$6 ;
  wire \$8 ;
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] \$next\buff ;
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] \$next\buff$24 ;
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] \$next\buff$25 ;
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] \$next\buff$26 ;
  (* src = "predictor_p1_c4_pix1_2.py:108" *)
  reg \$next\buff_ctr ;
  (* src = "predictor_p1_c4_pix1_2.py:84" *)
  reg [31:0] \$next\debug_counter ;
  (* src = "predictor_p1_c4_pix1_2.py:81" *)
  reg \$next\end_out ;
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] \$next\lbuff ;
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] \$next\lbuff$30 ;
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] \$next\lbuff$31 ;
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] \$next\lbuff$32 ;
  (* src = "predictor_p1_c4_pix1_2.py:109" *)
  reg \$next\lbuff_ctr ;
  (* src = "predictor_p1_c4_pix1_2.py:112" *)
  reg \$next\new_row_latch ;
  (* src = "predictor_p1_c4_pix1_2.py:111" *)
  reg \$next\new_row_reg ;
  (* src = "predictor_p1_c4_pix1_2.py:67" *)
  reg [15:0] \$next\pixel_out ;
  (* src = "predictor_p1_c4_pix1_2.py:67" *)
  reg [15:0] \$next\pixel_out$2 ;
  (* src = "predictor_p1_c4_pix1_2.py:70" *)
  reg [15:0] \$next\predic_out ;
  (* src = "predictor_p1_c4_pix1_2.py:70" *)
  reg [15:0] \$next\predic_out$3 ;
  (* src = "predictor_p1_c4_pix1_2.py:77" *)
  reg \$next\valid_out ;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] buff = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] \buff$24  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] \buff$25  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:100" *)
  reg [15:0] \buff$26  = 16'h8000;
  (* init = 1'h0 *)
  (* src = "predictor_p1_c4_pix1_2.py:108" *)
  reg buff_ctr = 1'h0;
  (* src = "nmigen/hdl/ir.py:329" *)
  input clk;
  (* init = 32'd0 *)
  (* src = "predictor_p1_c4_pix1_2.py:84" *)
  output [31:0] debug_counter;
  reg [31:0] debug_counter = 32'd0;
  (* src = "predictor_p1_c4_pix1_2.py:80" *)
  input end_in;
  (* init = 1'h0 *)
  (* src = "predictor_p1_c4_pix1_2.py:81" *)
  output end_out;
  reg end_out = 1'h0;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] lbuff = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] \lbuff$30  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] \lbuff$31  = 16'h8000;
  (* init = 16'h8000 *)
  (* src = "predictor_p1_c4_pix1_2.py:106" *)
  reg [15:0] \lbuff$32  = 16'h8000;
  (* init = 1'h0 *)
  (* src = "predictor_p1_c4_pix1_2.py:109" *)
  reg lbuff_ctr = 1'h0;
  (* src = "predictor_p1_c4_pix1_2.py:73" *)
  input new_row;
  (* src = "predictor_p1_c4_pix1_2.py:112" *)
  wire new_row_latch;
  (* init = 1'h0 *)
  (* src = "predictor_p1_c4_pix1_2.py:111" *)
  reg new_row_reg = 1'h0;
  (* src = "predictor_p1_c4_pix1_2.py:64" *)
  input [15:0] pixel_in;
  (* src = "predictor_p1_c4_pix1_2.py:64" *)
  input [15:0] \pixel_in$1 ;
  (* init = 16'h0000 *)
  (* src = "predictor_p1_c4_pix1_2.py:67" *)
  output [15:0] pixel_out;
  reg [15:0] pixel_out = 16'h0000;
  (* init = 16'h0000 *)
  (* src = "predictor_p1_c4_pix1_2.py:67" *)
  output [15:0] \pixel_out$2 ;
  reg [15:0] \pixel_out$2  = 16'h0000;
  (* init = 16'h0000 *)
  (* src = "predictor_p1_c4_pix1_2.py:70" *)
  output [15:0] predic_out;
  reg [15:0] predic_out = 16'h0000;
  (* init = 16'h0000 *)
  (* src = "predictor_p1_c4_pix1_2.py:70" *)
  output [15:0] \predic_out$3 ;
  reg [15:0] \predic_out$3  = 16'h0000;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "predictor_p1_c4_pix1_2.py:76" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "predictor_p1_c4_pix1_2.py:77" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$10  = valid_in == (* src = "predictor_p1_c4_pix1_2.py:117" *) 1'h1;
  assign \$12  = lbuff_ctr == (* src = "predictor_p1_c4_pix1_2.py:117" *) 1'h1;
  assign \$14  = \$10  & (* src = "predictor_p1_c4_pix1_2.py:117" *) \$12 ;
  assign \$16  = new_row | (* src = "predictor_p1_c4_pix1_2.py:119" *) new_row_reg;
  assign \$19  = debug_counter + (* src = "predictor_p1_c4_pix1_2.py:124" *) 1'h1;
  assign \$22  = buff_ctr + (* src = "predictor_p1_c4_pix1_2.py:130" *) 1'h1;
  assign \$28  = lbuff_ctr + (* src = "predictor_p1_c4_pix1_2.py:138" *) 1'h1;
  assign \$4  = valid_in == (* src = "predictor_p1_c4_pix1_2.py:115" *) 1'h1;
  assign \$6  = new_row == (* src = "predictor_p1_c4_pix1_2.py:115" *) 1'h1;
  assign \$8  = \$4  & (* src = "predictor_p1_c4_pix1_2.py:115" *) \$6 ;
  always @(posedge clk)
      end_out <= \$next\end_out ;
  always @(posedge clk)
      \buff$26  <= \$next\buff$26 ;
  always @(posedge clk)
      \buff$25  <= \$next\buff$25 ;
  always @(posedge clk)
      \buff$24  <= \$next\buff$24 ;
  always @(posedge clk)
      buff <= \$next\buff ;
  always @(posedge clk)
      buff_ctr <= \$next\buff_ctr ;
  always @(posedge clk)
      \pixel_out$2  <= \$next\pixel_out$2 ;
  always @(posedge clk)
      pixel_out <= \$next\pixel_out ;
  always @(posedge clk)
      debug_counter <= \$next\debug_counter ;
  always @(posedge clk)
      new_row_reg <= \$next\new_row_reg ;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      \predic_out$3  <= \$next\predic_out$3 ;
  always @(posedge clk)
      predic_out <= \$next\predic_out ;
  always @(posedge clk)
      \lbuff$32  <= \$next\lbuff$32 ;
  always @(posedge clk)
      \lbuff$31  <= \$next\lbuff$31 ;
  always @(posedge clk)
      \lbuff$30  <= \$next\lbuff$30 ;
  always @(posedge clk)
      lbuff <= \$next\lbuff ;
  always @(posedge clk)
      lbuff_ctr <= \$next\lbuff_ctr ;
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
    \$next\lbuff_ctr  = lbuff_ctr;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                \$next\lbuff_ctr  = \$27 [0];
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff_ctr  = 1'h0;
    endcase
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
    \$next\lbuff$30  = \lbuff$30 ;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h0:
                      \$next\lbuff$30  = \pixel_in$1 ;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff$30  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\lbuff$31  = \lbuff$31 ;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h1:
                      \$next\lbuff$31  = pixel_in;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff$31  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\lbuff$32  = \lbuff$32 ;
    casez (valid_in)
      1'h1:
          casez (new_row_latch)
            1'h1:
                casez (lbuff_ctr)
                  1'h1:
                      \$next\lbuff$32  = \pixel_in$1 ;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\lbuff$32  = 16'h8000;
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
                      \$next\predic_out  = \lbuff$31 ;
                endcase
            1'hz:
                casez (buff_ctr)
                  1'h0:
                      \$next\predic_out  = buff;
                  1'h1:
                      \$next\predic_out  = \buff$25 ;
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
                      \$next\predic_out$3  = \lbuff$30 ;
                  1'h1:
                      \$next\predic_out$3  = \lbuff$32 ;
                endcase
            1'hz:
                casez (buff_ctr)
                  1'h0:
                      \$next\predic_out$3  = \buff$24 ;
                  1'h1:
                      \$next\predic_out$3  = \buff$26 ;
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
    \$next\end_out  = end_out;
    \$next\end_out  = end_in;
    casez (rst)
      1'h1:
          \$next\end_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\debug_counter  = debug_counter;
    casez (valid_in)
      1'h1:
          \$next\debug_counter  = \$18 [31:0];
    endcase
    casez (rst)
      1'h1:
          \$next\debug_counter  = 32'd0;
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
          \$next\buff_ctr  = \$21 [0];
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
    \$next\buff$24  = \buff$24 ;
    casez (valid_in)
      1'h1:
          casez (buff_ctr)
            1'h0:
                \$next\buff$24  = \pixel_in$1 ;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff$24  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\buff$25  = \buff$25 ;
    casez (valid_in)
      1'h1:
          casez (buff_ctr)
            1'h1:
                \$next\buff$25  = pixel_in;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff$25  = 16'h8000;
    endcase
  end
  always @* begin
    \$next\buff$26  = \buff$26 ;
    casez (valid_in)
      1'h1:
          casez (buff_ctr)
            1'h1:
                \$next\buff$26  = \pixel_in$1 ;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buff$26  = 16'h8000;
    endcase
  end
  assign \$18  = \$19 ;
  assign \$21  = \$22 ;
  assign \$27  = \$28 ;
  assign new_row_latch = \$next\new_row_latch ;
endmodule

