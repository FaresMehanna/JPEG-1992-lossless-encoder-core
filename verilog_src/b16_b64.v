/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(end_in, i_busy, data_in, rst, clk, valid_out, o_busy, data_out, end_out, valid_in);
  wire \$1 ;
  wire \$11 ;
  wire \$13 ;
  wire \$15 ;
  wire \$17 ;
  wire \$19 ;
  wire \$21 ;
  wire [3:0] \$23 ;
  wire [3:0] \$24 ;
  wire \$26 ;
  wire \$28 ;
  wire \$3 ;
  wire \$30 ;
  wire \$32 ;
  wire \$34 ;
  wire \$36 ;
  wire \$38 ;
  wire \$40 ;
  wire \$42 ;
  wire \$44 ;
  wire \$46 ;
  wire \$48 ;
  wire \$5 ;
  wire \$50 ;
  wire \$52 ;
  wire \$54 ;
  wire \$56 ;
  wire \$58 ;
  wire \$60 ;
  wire \$62 ;
  wire \$64 ;
  wire \$66 ;
  wire \$68 ;
  wire \$7 ;
  wire \$70 ;
  wire \$72 ;
  wire \$74 ;
  wire \$76 ;
  wire \$78 ;
  wire \$80 ;
  wire \$82 ;
  wire \$84 ;
  wire \$9 ;
  (* src = "b16_b64.py:67" *)
  reg \$next\buff_chs ;
  (* src = "b16_b64.py:59" *)
  reg [63:0] \$next\buffer1 ;
  (* src = "b16_b64.py:60" *)
  reg \$next\buffer1_valid ;
  (* src = "b16_b64.py:63" *)
  reg [63:0] \$next\buffer2 ;
  (* src = "b16_b64.py:64" *)
  reg \$next\buffer2_valid ;
  (* src = "b16_b64.py:80" *)
  reg [2:0] \$next\counter ;
  (* src = "b16_b64.py:37" *)
  reg [63:0] \$next\data_out ;
  (* src = "b16_b64.py:44" *)
  reg \$next\end_out ;
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg [3:0] \$next\fsm_state ;
  (* src = "b16_b64.py:70" *)
  reg \$next\is_valid ;
  (* src = "b16_b64.py:46" *)
  reg \$next\o_busy ;
  (* src = "b16_b64.py:74" *)
  reg \$next\reg_end ;
  (* src = "b16_b64.py:41" *)
  reg \$next\valid_out ;
  (* init = 1'h0 *)
  (* src = "b16_b64.py:67" *)
  reg buff_chs = 1'h0;
  (* init = 64'h0000000000000000 *)
  (* src = "b16_b64.py:59" *)
  reg [63:0] buffer1 = 64'h0000000000000000;
  (* init = 1'h0 *)
  (* src = "b16_b64.py:60" *)
  reg buffer1_valid = 1'h0;
  (* init = 64'h0000000000000000 *)
  (* src = "b16_b64.py:63" *)
  reg [63:0] buffer2 = 64'h0000000000000000;
  (* init = 1'h0 *)
  (* src = "b16_b64.py:64" *)
  reg buffer2_valid = 1'h0;
  (* src = "nmigen/hdl/ir.py:329" *)
  input clk;
  (* init = 3'h0 *)
  (* src = "b16_b64.py:80" *)
  reg [2:0] counter = 3'h0;
  (* src = "b16_b64.py:34" *)
  input [15:0] data_in;
  (* init = 64'h0000000000000000 *)
  (* src = "b16_b64.py:37" *)
  output [63:0] data_out;
  reg [63:0] data_out = 64'h0000000000000000;
  (* src = "b16_b64.py:43" *)
  input end_in;
  (* init = 1'h0 *)
  (* src = "b16_b64.py:44" *)
  output end_out;
  reg end_out = 1'h0;
  (* init = 4'h0 *)
  (* src = "nmigen/hdl/dsl.py:244" *)
  reg [3:0] fsm_state = 4'h0;
  (* src = "b16_b64.py:47" *)
  input i_busy;
  (* src = "b16_b64.py:70" *)
  wire is_valid;
  (* init = 1'h0 *)
  (* src = "b16_b64.py:46" *)
  output o_busy;
  reg o_busy = 1'h0;
  (* init = 1'h0 *)
  (* src = "b16_b64.py:74" *)
  reg reg_end = 1'h0;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "b16_b64.py:40" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "b16_b64.py:41" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$9  = o_busy == (* src = "b16_b64.py:76" *) 1'h0;
  assign \$11  = \$7  & (* src = "b16_b64.py:76" *) \$9 ;
  assign \$13  = reg_end == (* src = "b16_b64.py:81" *) 1'h1;
  assign \$15  = valid_out == (* src = "b16_b64.py:81" *) 1'h1;
  assign \$17  = \$13  & (* src = "b16_b64.py:81" *) \$15 ;
  assign \$1  = valid_out == (* src = "b16_b64.py:96" *) 1'h1;
  assign \$19  = i_busy == (* src = "b16_b64.py:81" *) 1'h0;
  assign \$21  = \$17  & (* src = "b16_b64.py:81" *) \$19 ;
  assign \$24  = counter + (* src = "b16_b64.py:82" *) 1'h1;
  assign \$26  = reg_end == (* src = "b16_b64.py:83" *) 1'h1;
  assign \$28  = counter == (* src = "b16_b64.py:83" *) 3'h7;
  assign \$30  = \$26  & (* src = "b16_b64.py:83" *) \$28 ;
  assign \$32  = buff_chs == (* src = "b16_b64.py:87" *) 1'h0;
  assign \$34  = buff_chs == (* src = "b16_b64.py:89" *) 1'h1;
  assign \$36  = buffer1_valid == (* src = "b16_b64.py:93" *) 1'h1;
  assign \$38  = buffer2_valid == (* src = "b16_b64.py:93" *) 1'h1;
  assign \$3  = i_busy == (* src = "b16_b64.py:96" *) 1'h0;
  assign \$40  = \$36  | (* src = "b16_b64.py:93" *) \$38 ;
  assign \$42  = is_valid == (* src = "b16_b64.py:93" *) 1'h1;
  assign \$44  = \$40  & (* src = "b16_b64.py:93" *) \$42 ;
  assign \$46  = valid_out == (* src = "b16_b64.py:96" *) 1'h1;
  assign \$48  = i_busy == (* src = "b16_b64.py:96" *) 1'h0;
  assign \$50  = \$46  & (* src = "b16_b64.py:96" *) \$48 ;
  assign \$52  = buff_chs == (* src = "b16_b64.py:98" *) 1'h0;
  assign \$54  = valid_out == (* src = "b16_b64.py:96" *) 1'h1;
  assign \$56  = i_busy == (* src = "b16_b64.py:96" *) 1'h0;
  assign \$58  = \$54  & (* src = "b16_b64.py:96" *) \$56 ;
  assign \$5  = \$1  & (* src = "b16_b64.py:96" *) \$3 ;
  assign \$60  = buff_chs == (* src = "b16_b64.py:99" *) 1'h0;
  assign \$62  = valid_out == (* src = "b16_b64.py:96" *) 1'h1;
  assign \$64  = i_busy == (* src = "b16_b64.py:96" *) 1'h0;
  assign \$66  = \$62  & (* src = "b16_b64.py:96" *) \$64 ;
  assign \$68  = buff_chs == (* src = "b16_b64.py:101" *) 1'h1;
  assign \$70  = buffer1_valid == (* src = "b16_b64.py:110" *) 1'h0;
  assign \$72  = buffer2_valid == (* src = "b16_b64.py:137" *) 1'h0;
  assign \$74  = buffer2_valid == (* src = "b16_b64.py:148" *) 1'h0;
  assign \$76  = buffer1_valid == (* src = "b16_b64.py:175" *) 1'h0;
  assign \$78  = buffer1_valid == (* src = "b16_b64.py:110" *) 1'h0;
  assign \$7  = valid_in == (* src = "b16_b64.py:76" *) 1'h1;
  assign \$80  = buffer2_valid == (* src = "b16_b64.py:137" *) 1'h0;
  assign \$82  = buffer2_valid == (* src = "b16_b64.py:148" *) 1'h0;
  assign \$84  = buffer1_valid == (* src = "b16_b64.py:175" *) 1'h0;
  always @(posedge clk)
      buffer2 <= \$next\buffer2 ;
  always @(posedge clk)
      end_out <= \$next\end_out ;
  always @(posedge clk)
      counter <= \$next\counter ;
  always @(posedge clk)
      reg_end <= \$next\reg_end ;
  always @(posedge clk)
      buffer1 <= \$next\buffer1 ;
  always @(posedge clk)
      fsm_state <= \$next\fsm_state ;
  always @(posedge clk)
      o_busy <= \$next\o_busy ;
  always @(posedge clk)
      buffer2_valid <= \$next\buffer2_valid ;
  always @(posedge clk)
      buffer1_valid <= \$next\buffer1_valid ;
  always @(posedge clk)
      buff_chs <= \$next\buff_chs ;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      data_out <= \$next\data_out ;
  always @* begin
    \$next\is_valid  = 1'h0;
    \$next\is_valid  = 1'h1;
    casez (\$5 )
      1'h1:
          \$next\is_valid  = 1'h0;
    endcase
  end
  always @* begin
    \$next\reg_end  = reg_end;
    casez (\$11 )
      1'h1:
          \$next\reg_end  = end_in;
    endcase
    casez (rst)
      1'h1:
          \$next\reg_end  = 1'h0;
    endcase
  end
  always @* begin
    \$next\fsm_state  = fsm_state;
    casez (fsm_state)
      4'h0:
          casez (\$78 )
            1'h1:
                \$next\fsm_state  = 4'h1;
          endcase
      4'h1:
          casez (valid_in)
            1'h1:
                \$next\fsm_state  = 4'h2;
          endcase
      4'h2:
          casez (valid_in)
            1'h1:
                \$next\fsm_state  = 4'h3;
          endcase
      4'h3:
          casez (valid_in)
            1'h1:
                \$next\fsm_state  = 4'h4;
          endcase
      4'h4:
          casez (valid_in)
            1'h1:
                casez (\$80 )
                  1'h1:
                      \$next\fsm_state  = 4'h5;
                  1'hz:
                      \$next\fsm_state  = 4'h6;
                endcase
          endcase
      4'h6:
          casez (\$82 )
            1'h1:
                \$next\fsm_state  = 4'h5;
          endcase
      4'h5:
          casez (valid_in)
            1'h1:
                \$next\fsm_state  = 4'h7;
          endcase
      4'h7:
          casez (valid_in)
            1'h1:
                \$next\fsm_state  = 4'h8;
          endcase
      4'h8:
          casez (valid_in)
            1'h1:
                \$next\fsm_state  = 4'h9;
          endcase
      4'h9:
          casez (valid_in)
            1'h1:
                casez (\$84 )
                  1'h1:
                      \$next\fsm_state  = 4'h1;
                  1'hz:
                      \$next\fsm_state  = 4'h0;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fsm_state  = 4'h0;
    endcase
  end
  always @* begin
    \$next\buffer1  = buffer1;
    casez (fsm_state)
      4'h1:
          casez (valid_in)
            1'h1:
                \$next\buffer1 [63:48] = data_in;
          endcase
      4'h2:
          casez (valid_in)
            1'h1:
                \$next\buffer1 [47:32] = data_in;
          endcase
      4'h3:
          casez (valid_in)
            1'h1:
                \$next\buffer1 [31:16] = data_in;
          endcase
      4'h4:
          casez (valid_in)
            1'h1:
                \$next\buffer1 [15:0] = data_in;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buffer1  = 64'h0000000000000000;
    endcase
  end
  always @* begin
    \$next\buffer2  = buffer2;
    casez (fsm_state)
      4'h5:
          casez (valid_in)
            1'h1:
                \$next\buffer2 [63:48] = data_in;
          endcase
      4'h7:
          casez (valid_in)
            1'h1:
                \$next\buffer2 [47:32] = data_in;
          endcase
      4'h8:
          casez (valid_in)
            1'h1:
                \$next\buffer2 [31:16] = data_in;
          endcase
      4'h9:
          casez (valid_in)
            1'h1:
                \$next\buffer2 [15:0] = data_in;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buffer2  = 64'h0000000000000000;
    endcase
  end
  always @* begin
    \$next\counter  = counter;
    casez (\$21 )
      1'h1:
          \$next\counter  = \$23 [2:0];
    endcase
    casez (rst)
      1'h1:
          \$next\counter  = 3'h0;
    endcase
  end
  always @* begin
    \$next\end_out  = end_out;
    casez (\$30 )
      1'h1:
          \$next\end_out  = 1'h1;
    endcase
    casez (rst)
      1'h1:
          \$next\end_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\data_out  = data_out;
    casez (\$32 )
      1'h1:
          \$next\data_out  = buffer1;
    endcase
    casez (\$34 )
      1'h1:
          \$next\data_out  = buffer2;
    endcase
    casez (rst)
      1'h1:
          \$next\data_out  = 64'h0000000000000000;
    endcase
  end
  always @* begin
    \$next\valid_out  = valid_out;
    \$next\valid_out  = \$44 ;
    casez (rst)
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\buff_chs  = buff_chs;
    casez (\$50 )
      1'h1:
          \$next\buff_chs  = \$52 ;
    endcase
    casez (rst)
      1'h1:
          \$next\buff_chs  = 1'h0;
    endcase
  end
  always @* begin
    \$next\buffer1_valid  = buffer1_valid;
    casez (\$58 )
      1'h1:
          casez (\$60 )
            1'h1:
                \$next\buffer1_valid  = 1'h0;
          endcase
    endcase
    casez (fsm_state)
      4'h4:
          casez (valid_in)
            1'h1:
                \$next\buffer1_valid  = 1'h1;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buffer1_valid  = 1'h0;
    endcase
  end
  always @* begin
    \$next\buffer2_valid  = buffer2_valid;
    casez (\$66 )
      1'h1:
          casez (\$68 )
            1'h1:
                \$next\buffer2_valid  = 1'h0;
          endcase
    endcase
    casez (fsm_state)
      4'h9:
          casez (valid_in)
            1'h1:
                \$next\buffer2_valid  = 1'h1;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buffer2_valid  = 1'h0;
    endcase
  end
  always @* begin
    \$next\o_busy  = o_busy;
    casez (fsm_state)
      4'h0:
          casez (\$70 )
            1'h1:
                \$next\o_busy  = 1'h0;
          endcase
      4'h4:
          casez (valid_in)
            1'h1:
                casez (\$72 )
                  1'h1:
                      /* empty */;
                  1'hz:
                      \$next\o_busy  = 1'h1;
                endcase
          endcase
      4'h6:
          casez (\$74 )
            1'h1:
                \$next\o_busy  = 1'h0;
          endcase
      4'h9:
          casez (valid_in)
            1'h1:
                casez (\$76 )
                  1'h1:
                      /* empty */;
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
  assign \$23  = \$24 ;
  assign is_valid = \$next\is_valid ;
endmodule

