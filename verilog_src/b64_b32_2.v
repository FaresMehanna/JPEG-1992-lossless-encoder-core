/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(data_in, i_busy, rst, clk, valid_out, o_busy, data_out, valid_in);
  wire \$1 ;
  wire \$101 ;
  wire \$103 ;
  wire \$105 ;
  wire \$107 ;
  wire \$109 ;
  wire \$11 ;
  wire \$111 ;
  wire \$113 ;
  wire \$115 ;
  wire \$117 ;
  wire \$119 ;
  wire \$121 ;
  wire \$123 ;
  wire \$125 ;
  wire \$127 ;
  wire \$129 ;
  wire \$13 ;
  wire \$131 ;
  wire \$15 ;
  wire \$17 ;
  wire \$19 ;
  wire \$21 ;
  wire \$23 ;
  wire \$25 ;
  wire \$27 ;
  wire \$29 ;
  wire \$3 ;
  wire \$31 ;
  wire \$33 ;
  wire \$35 ;
  wire \$37 ;
  wire \$39 ;
  wire \$41 ;
  wire \$43 ;
  wire \$45 ;
  wire \$47 ;
  wire \$49 ;
  wire \$5 ;
  wire \$51 ;
  wire \$53 ;
  wire \$55 ;
  wire \$57 ;
  wire \$59 ;
  wire \$61 ;
  wire \$63 ;
  wire \$65 ;
  wire \$67 ;
  wire \$69 ;
  wire \$7 ;
  wire \$71 ;
  wire \$73 ;
  wire \$75 ;
  wire \$77 ;
  wire \$79 ;
  wire \$81 ;
  wire \$83 ;
  wire \$85 ;
  wire \$87 ;
  wire \$89 ;
  wire \$9 ;
  wire \$91 ;
  wire \$93 ;
  wire \$95 ;
  wire \$97 ;
  wire \$99 ;
  (* src = "./migen_src/b64_b32_2.py:41" *)
  reg [23:0] \$next\data_out ;
  (* src = "./migen_src/b64_b32_2.py:62" *)
  reg \$next\half_latched ;
  (* src = "./migen_src/b64_b32_2.py:47" *)
  reg \$next\o_busy ;
  (* src = "./migen_src/b64_b32_2.py:59" *)
  reg [63:0] \$next\reg ;
  (* src = "./migen_src/b64_b32_2.py:61" *)
  reg \$next\reg_tobe_invalid ;
  (* src = "./migen_src/b64_b32_2.py:60" *)
  reg \$next\reg_valid ;
  (* src = "./migen_src/b64_b32_2.py:45" *)
  reg \$next\valid_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/b64_b32_2.py:38" *)
  input [63:0] data_in;
  (* init = 24'h000000 *)
  (* src = "./migen_src/b64_b32_2.py:41" *)
  output [23:0] data_out;
  reg [23:0] data_out = 24'h000000;
  (* init = 1'h0 *)
  (* src = "./migen_src/b64_b32_2.py:62" *)
  reg half_latched = 1'h0;
  (* src = "./migen_src/b64_b32_2.py:48" *)
  input i_busy;
  (* src = "./migen_src/b64_b32_2.py:47" *)
  output o_busy;
  (* init = 64'h0000000000000000 *)
  (* src = "./migen_src/b64_b32_2.py:59" *)
  reg [63:0] \reg  = 64'h0000000000000000;
  (* src = "./migen_src/b64_b32_2.py:61" *)
  wire reg_tobe_invalid;
  (* init = 1'h0 *)
  (* src = "./migen_src/b64_b32_2.py:60" *)
  reg reg_valid = 1'h0;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/b64_b32_2.py:44" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/b64_b32_2.py:45" *)
  output valid_out;
  reg valid_out = 1'h0;
  assign \$9  = \$5  & (* src = "./migen_src/b64_b32_2.py:93" *) \$7 ;
  assign \$99  = half_latched == (* src = "./migen_src/b64_b32_2.py:94" *) 1'h1;
  assign \$101  = reg_valid == (* src = "./migen_src/b64_b32_2.py:118" *) 1'h0;
  assign \$103  = i_busy == (* src = "./migen_src/b64_b32_2.py:118" *) 1'h0;
  assign \$105  = \$101  & (* src = "./migen_src/b64_b32_2.py:118" *) \$103 ;
  assign \$107  = valid_out == (* src = "./migen_src/b64_b32_2.py:118" *) 1'h1;
  assign \$109  = \$105  & (* src = "./migen_src/b64_b32_2.py:118" *) \$107 ;
  assign \$111  = reg_valid == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h1;
  assign \$113  = valid_out == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h0;
  assign \$115  = \$111  & (* src = "./migen_src/b64_b32_2.py:84" *) \$113 ;
  assign \$117  = half_latched == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h0;
  assign \$11  = half_latched == (* src = "./migen_src/b64_b32_2.py:94" *) 1'h1;
  assign \$119  = \$115  & (* src = "./migen_src/b64_b32_2.py:84" *) \$117 ;
  assign \$121  = reg_valid == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$123  = i_busy == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h0;
  assign \$125  = \$121  & (* src = "./migen_src/b64_b32_2.py:93" *) \$123 ;
  assign \$127  = valid_out == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$129  = \$125  & (* src = "./migen_src/b64_b32_2.py:93" *) \$127 ;
  assign \$131  = half_latched == (* src = "./migen_src/b64_b32_2.py:94" *) 1'h1;
  assign \$13  = valid_in == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h1;
  assign \$15  = reg_valid == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h0;
  assign \$17  = reg_tobe_invalid == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h1;
  assign \$1  = reg_valid == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$19  = \$15  | (* src = "./migen_src/b64_b32_2.py:73" *) \$17 ;
  assign \$21  = \$13  & (* src = "./migen_src/b64_b32_2.py:73" *) \$19 ;
  assign \$23  = valid_in == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h1;
  assign \$25  = reg_valid == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h0;
  assign \$27  = reg_tobe_invalid == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h1;
  assign \$29  = \$25  | (* src = "./migen_src/b64_b32_2.py:73" *) \$27 ;
  assign \$31  = \$23  & (* src = "./migen_src/b64_b32_2.py:73" *) \$29 ;
  assign \$33  = valid_in == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h1;
  assign \$35  = reg_valid == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h0;
  assign \$37  = reg_tobe_invalid == (* src = "./migen_src/b64_b32_2.py:73" *) 1'h1;
  assign \$3  = i_busy == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h0;
  assign \$39  = \$35  | (* src = "./migen_src/b64_b32_2.py:73" *) \$37 ;
  assign \$41  = \$33  & (* src = "./migen_src/b64_b32_2.py:73" *) \$39 ;
  assign \$43  = reg_valid == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$45  = i_busy == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h0;
  assign \$47  = \$43  & (* src = "./migen_src/b64_b32_2.py:93" *) \$45 ;
  assign \$49  = valid_out == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$51  = \$47  & (* src = "./migen_src/b64_b32_2.py:93" *) \$49 ;
  assign \$53  = half_latched == (* src = "./migen_src/b64_b32_2.py:94" *) 1'h1;
  assign \$55  = valid_in == (* src = "./migen_src/b64_b32_2.py:105" *) 1'h0;
  assign \$57  = reg_valid == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h1;
  assign \$5  = \$1  & (* src = "./migen_src/b64_b32_2.py:93" *) \$3 ;
  assign \$59  = valid_out == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h0;
  assign \$61  = \$57  & (* src = "./migen_src/b64_b32_2.py:84" *) \$59 ;
  assign \$63  = half_latched == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h0;
  assign \$65  = \$61  & (* src = "./migen_src/b64_b32_2.py:84" *) \$63 ;
  assign \$67  = reg_valid == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$69  = i_busy == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h0;
  assign \$71  = \$67  & (* src = "./migen_src/b64_b32_2.py:93" *) \$69 ;
  assign \$73  = valid_out == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$75  = \$71  & (* src = "./migen_src/b64_b32_2.py:93" *) \$73 ;
  assign \$77  = half_latched == (* src = "./migen_src/b64_b32_2.py:94" *) 1'h1;
  assign \$7  = valid_out == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$79  = reg_valid == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h1;
  assign \$81  = valid_out == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h0;
  assign \$83  = \$79  & (* src = "./migen_src/b64_b32_2.py:84" *) \$81 ;
  assign \$85  = half_latched == (* src = "./migen_src/b64_b32_2.py:84" *) 1'h0;
  assign \$87  = \$83  & (* src = "./migen_src/b64_b32_2.py:84" *) \$85 ;
  assign \$89  = reg_valid == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$91  = i_busy == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h0;
  assign \$93  = \$89  & (* src = "./migen_src/b64_b32_2.py:93" *) \$91 ;
  assign \$95  = valid_out == (* src = "./migen_src/b64_b32_2.py:93" *) 1'h1;
  assign \$97  = \$93  & (* src = "./migen_src/b64_b32_2.py:93" *) \$95 ;
  always @(posedge clk)
      half_latched <= \$next\half_latched ;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      data_out <= \$next\data_out ;
  always @(posedge clk)
      reg_valid <= \$next\reg_valid ;
  always @(posedge clk)
      \reg  <= \$next\reg ;
  always @* begin
    \$next\reg_tobe_invalid  = 1'h0;
    \$next\reg_tobe_invalid  = 1'h0;
    casez (\$9 )
      1'h1:
          casez (\$11 )
            1'h1:
                \$next\reg_tobe_invalid  = 1'h1;
          endcase
    endcase
  end
  always @* begin
    \$next\o_busy  = 1'h1;
    \$next\o_busy  = 1'h1;
    casez (\$21 )
      1'h1:
          \$next\o_busy  = 1'h0;
    endcase
  end
  always @* begin
    \$next\reg  = \reg ;
    casez (\$31 )
      1'h1:
          \$next\reg  = data_in;
    endcase
    casez (rst)
      1'h1:
          \$next\reg  = 64'h0000000000000000;
    endcase
  end
  always @* begin
    \$next\reg_valid  = reg_valid;
    casez (\$41 )
      1'h1:
          \$next\reg_valid  = 1'h1;
    endcase
    casez (\$51 )
      1'h1:
          casez (\$53 )
            1'h1:
                casez (\$55 )
                  1'h1:
                      \$next\reg_valid  = 1'h0;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\reg_valid  = 1'h0;
    endcase
  end
  always @* begin
    \$next\data_out  = data_out;
    casez (\$65 )
      1'h1:
          \$next\data_out  = \reg [63:40];
    endcase
    casez (\$75 )
      1'h1:
          casez (\$77 )
            1'h1:
                \$next\data_out  = \reg [39:16];
            1'hz:
                \$next\data_out  = \reg [63:40];
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\data_out  = 24'h000000;
    endcase
  end
  always @* begin
    \$next\valid_out  = valid_out;
    casez (\$87 )
      1'h1:
          \$next\valid_out  = 1'h1;
    endcase
    casez (\$97 )
      1'h1:
          casez (\$99 )
            1'h1:
                \$next\valid_out  = 1'h1;
            1'hz:
                \$next\valid_out  = 1'h1;
          endcase
    endcase
    casez (\$109 )
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
    casez (rst)
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\half_latched  = half_latched;
    casez (\$119 )
      1'h1:
          \$next\half_latched  = 1'h1;
    endcase
    casez (\$129 )
      1'h1:
          casez (\$131 )
            1'h1:
                \$next\half_latched  = 1'h0;
            1'hz:
                \$next\half_latched  = 1'h1;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\half_latched  = 1'h0;
    endcase
  end
  assign o_busy = \$next\o_busy ;
  assign reg_tobe_invalid = \$next\reg_tobe_invalid ;
endmodule
