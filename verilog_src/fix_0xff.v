/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(valid_in, end_in, data_in, rst, clk, valid_out, o_busy, data_out, data_out_ctr, end_out, i_busy);
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
  wire [31:0] \$125 ;
  wire [31:0] \$127 ;
  wire [31:0] \$129 ;
  wire \$13 ;
  wire \$131 ;
  wire \$133 ;
  wire \$135 ;
  wire \$137 ;
  wire \$139 ;
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
  wire [31:0] \$43 ;
  wire [31:0] \$45 ;
  wire [31:0] \$47 ;
  wire \$49 ;
  wire \$5 ;
  wire \$51 ;
  wire \$53 ;
  wire [31:0] \$55 ;
  wire [31:0] \$57 ;
  wire [31:0] \$59 ;
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
  (* src = "fix_0xff.py:72" *)
  reg [31:0] \$next\data_out ;
  (* src = "fix_0xff.py:73" *)
  reg [2:0] \$next\data_out_ctr ;
  (* src = "fix_0xff.py:99" *)
  reg [2:0] \$next\data_out_ctr_reg ;
  (* src = "fix_0xff.py:97" *)
  reg [31:0] \$next\data_out_reg ;
  (* src = "fix_0xff.py:100" *)
  reg \$next\data_out_valid ;
  (* src = "fix_0xff.py:82" *)
  reg \$next\end_out ;
  (* src = "fix_0xff.py:98" *)
  reg \$next\end_out_reg ;
  (* src = "fix_0xff.py:78" *)
  reg \$next\o_busy ;
  (* src = "fix_0xff.py:93" *)
  reg [7:0] \$next\ones ;
  (* src = "fix_0xff.py:77" *)
  reg \$next\valid_out ;
  (* src = "fix_0xff.py:92" *)
  reg [7:0] \$next\zeros ;
  (* src = "nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "fix_0xff.py:69" *)
  input [15:0] data_in;
  (* init = 32'd0 *)
  (* src = "fix_0xff.py:72" *)
  output [31:0] data_out;
  reg [31:0] data_out = 32'd0;
  (* init = 3'h0 *)
  (* src = "fix_0xff.py:73" *)
  output [2:0] data_out_ctr;
  reg [2:0] data_out_ctr = 3'h0;
  (* init = 3'h0 *)
  (* src = "fix_0xff.py:99" *)
  reg [2:0] data_out_ctr_reg = 3'h0;
  (* init = 32'd0 *)
  (* src = "fix_0xff.py:97" *)
  reg [31:0] data_out_reg = 32'd0;
  (* init = 1'h0 *)
  (* src = "fix_0xff.py:100" *)
  reg data_out_valid = 1'h0;
  (* src = "fix_0xff.py:81" *)
  input end_in;
  (* init = 1'h0 *)
  (* src = "fix_0xff.py:82" *)
  output end_out;
  reg end_out = 1'h0;
  (* init = 1'h0 *)
  (* src = "fix_0xff.py:98" *)
  reg end_out_reg = 1'h0;
  (* src = "fix_0xff.py:79" *)
  input i_busy;
  (* init = 1'h0 *)
  (* src = "fix_0xff.py:78" *)
  output o_busy;
  reg o_busy = 1'h0;
  (* init = 8'hff *)
  (* src = "fix_0xff.py:93" *)
  reg [7:0] ones = 8'hff;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "fix_0xff.py:76" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "fix_0xff.py:77" *)
  output valid_out;
  reg valid_out = 1'h0;
  (* init = 8'h00 *)
  (* src = "fix_0xff.py:92" *)
  reg [7:0] zeros = 8'h00;
  assign \$9  = \$5  & (* src = "fix_0xff.py:135" *) \$7 ;
  assign \$99  = \$95  & (* src = "fix_0xff.py:138" *) \$97 ;
  assign \$101  = i_busy == (* src = "fix_0xff.py:106" *) 1'h0;
  assign \$103  = valid_out == (* src = "fix_0xff.py:125" *) 1'h0;
  assign \$105  = valid_in == (* src = "fix_0xff.py:135" *) 1'h1;
  assign \$107  = o_busy == (* src = "fix_0xff.py:135" *) 1'h0;
  assign \$109  = \$105  & (* src = "fix_0xff.py:135" *) \$107 ;
  assign \$111  = valid_in == (* src = "fix_0xff.py:137" *) 1'h1;
  assign \$113  = valid_out == (* src = "fix_0xff.py:137" *) 1'h1;
  assign \$115  = \$111  & (* src = "fix_0xff.py:137" *) \$113 ;
  assign \$117  = o_busy == (* src = "fix_0xff.py:141" *) 1'h0;
  assign \$11  = data_out_valid == (* src = "fix_0xff.py:107" *) 1'h0;
  assign \$119  = data_in == (* src = "fix_0xff.py:41" *) 16'hffff;
  assign \$121  = data_in[7:0] == (* src = "fix_0xff.py:47" *) 8'hff;
  assign \$123  = data_in[15:8] == (* src = "fix_0xff.py:53" *) 8'hff;
  assign \$125  = + (* src = "fix_0xff.py:49" *) { data_in[15:8], ones, zeros };
  assign \$127  = + (* src = "fix_0xff.py:55" *) { ones, zeros, data_in[7:0] };
  assign \$129  = + (* src = "fix_0xff.py:69" *) data_in;
  assign \$131  = o_busy == (* src = "fix_0xff.py:141" *) 1'h0;
  assign \$133  = data_in == (* src = "fix_0xff.py:41" *) 16'hffff;
  assign \$135  = data_in[7:0] == (* src = "fix_0xff.py:47" *) 8'hff;
  assign \$137  = data_in[15:8] == (* src = "fix_0xff.py:53" *) 8'hff;
  assign \$13  = i_busy == (* src = "fix_0xff.py:106" *) 1'h0;
  assign \$139  = o_busy == (* src = "fix_0xff.py:141" *) 1'h0;
  assign \$15  = valid_out == (* src = "fix_0xff.py:125" *) 1'h0;
  assign \$17  = valid_in == (* src = "fix_0xff.py:135" *) 1'h1;
  assign \$1  = i_busy == (* src = "fix_0xff.py:106" *) 1'h0;
  assign \$19  = o_busy == (* src = "fix_0xff.py:135" *) 1'h0;
  assign \$21  = \$17  & (* src = "fix_0xff.py:135" *) \$19 ;
  assign \$23  = data_out_valid == (* src = "fix_0xff.py:107" *) 1'h0;
  assign \$25  = i_busy == (* src = "fix_0xff.py:106" *) 1'h0;
  assign \$27  = valid_out == (* src = "fix_0xff.py:125" *) 1'h0;
  assign \$29  = valid_in == (* src = "fix_0xff.py:135" *) 1'h1;
  assign \$31  = o_busy == (* src = "fix_0xff.py:135" *) 1'h0;
  assign \$33  = \$29  & (* src = "fix_0xff.py:135" *) \$31 ;
  assign \$35  = data_out_valid == (* src = "fix_0xff.py:107" *) 1'h0;
  assign \$37  = data_in == (* src = "fix_0xff.py:41" *) 16'hffff;
  assign \$3  = valid_out == (* src = "fix_0xff.py:125" *) 1'h0;
  assign \$39  = data_in[7:0] == (* src = "fix_0xff.py:47" *) 8'hff;
  assign \$41  = data_in[15:8] == (* src = "fix_0xff.py:53" *) 8'hff;
  assign \$43  = + (* src = "fix_0xff.py:49" *) { data_in[15:8], ones, zeros };
  assign \$45  = + (* src = "fix_0xff.py:55" *) { ones, zeros, data_in[7:0] };
  assign \$47  = + (* src = "fix_0xff.py:69" *) data_in;
  assign \$49  = data_in == (* src = "fix_0xff.py:41" *) 16'hffff;
  assign \$51  = data_in[7:0] == (* src = "fix_0xff.py:47" *) 8'hff;
  assign \$53  = data_in[15:8] == (* src = "fix_0xff.py:53" *) 8'hff;
  assign \$55  = + (* src = "fix_0xff.py:49" *) { data_in[15:8], ones, zeros };
  assign \$57  = + (* src = "fix_0xff.py:55" *) { ones, zeros, data_in[7:0] };
  assign \$5  = valid_in == (* src = "fix_0xff.py:135" *) 1'h1;
  assign \$59  = + (* src = "fix_0xff.py:69" *) data_in;
  assign \$61  = i_busy == (* src = "fix_0xff.py:106" *) 1'h0;
  assign \$63  = valid_out == (* src = "fix_0xff.py:125" *) 1'h0;
  assign \$65  = valid_in == (* src = "fix_0xff.py:135" *) 1'h1;
  assign \$67  = o_busy == (* src = "fix_0xff.py:135" *) 1'h0;
  assign \$69  = \$65  & (* src = "fix_0xff.py:135" *) \$67 ;
  assign \$71  = data_out_valid == (* src = "fix_0xff.py:107" *) 1'h0;
  assign \$73  = data_in == (* src = "fix_0xff.py:41" *) 16'hffff;
  assign \$75  = data_in[7:0] == (* src = "fix_0xff.py:47" *) 8'hff;
  assign \$77  = data_in[15:8] == (* src = "fix_0xff.py:53" *) 8'hff;
  assign \$7  = o_busy == (* src = "fix_0xff.py:135" *) 1'h0;
  assign \$79  = data_in == (* src = "fix_0xff.py:41" *) 16'hffff;
  assign \$81  = data_in[7:0] == (* src = "fix_0xff.py:47" *) 8'hff;
  assign \$83  = data_in[15:8] == (* src = "fix_0xff.py:53" *) 8'hff;
  assign \$85  = i_busy == (* src = "fix_0xff.py:106" *) 1'h0;
  assign \$87  = valid_out == (* src = "fix_0xff.py:125" *) 1'h0;
  assign \$89  = valid_in == (* src = "fix_0xff.py:135" *) 1'h1;
  assign \$91  = o_busy == (* src = "fix_0xff.py:135" *) 1'h0;
  assign \$93  = \$89  & (* src = "fix_0xff.py:135" *) \$91 ;
  assign \$95  = valid_in == (* src = "fix_0xff.py:138" *) 1'h1;
  assign \$97  = valid_out == (* src = "fix_0xff.py:138" *) 1'h1;
  always @(posedge clk)
      end_out_reg <= \$next\end_out_reg ;
  always @(posedge clk)
      zeros <= \$next\zeros ;
  always @(posedge clk)
      ones <= \$next\ones ;
  always @(posedge clk)
      data_out_ctr_reg <= \$next\data_out_ctr_reg ;
  always @(posedge clk)
      data_out_reg <= \$next\data_out_reg ;
  always @(posedge clk)
      data_out_valid <= \$next\data_out_valid ;
  always @(posedge clk)
      o_busy <= \$next\o_busy ;
  always @(posedge clk)
      data_out_ctr <= \$next\data_out_ctr ;
  always @(posedge clk)
      data_out <= \$next\data_out ;
  always @(posedge clk)
      end_out <= \$next\end_out ;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @* begin
    \$next\ones  = ones;
    \$next\ones  = 8'hff;
    casez (rst)
      1'h1:
          \$next\ones  = 8'hff;
    endcase
  end
  always @* begin
    \$next\zeros  = zeros;
    \$next\zeros  = 8'h00;
    casez (rst)
      1'h1:
          \$next\zeros  = 8'h00;
    endcase
  end
  always @* begin
    \$next\end_out_reg  = end_out_reg;
    casez (\$139 )
      1'h1:
          \$next\end_out_reg  = end_in;
    endcase
    casez (rst)
      1'h1:
          \$next\end_out_reg  = 1'h0;
    endcase
  end
  always @* begin
    \$next\valid_out  = valid_out;
    casez ({ \$9 , \$3 , \$1  })
      3'bzz1:
          casez (\$11 )
            1'h1:
                \$next\valid_out  = valid_in;
            1'hz:
                \$next\valid_out  = 1'h1;
          endcase
      3'bz1z:
          \$next\valid_out  = valid_in;
    endcase
    casez (rst)
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\end_out  = end_out;
    casez ({ \$21 , \$15 , \$13  })
      3'bzz1:
          casez (\$23 )
            1'h1:
                \$next\end_out  = end_in;
            1'hz:
                \$next\end_out  = end_out_reg;
          endcase
      3'bz1z:
          \$next\end_out  = end_in;
    endcase
    casez (rst)
      1'h1:
          \$next\end_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\data_out  = data_out;
    casez ({ \$33 , \$27 , \$25  })
      3'bzz1:
          casez (\$35 )
            1'h1:
                casez ({ \$41 , \$39 , \$37  })
                  3'bzz1:
                      \$next\data_out  = { ones, zeros, ones, zeros };
                  3'bz1z:
                      \$next\data_out  = \$43 ;
                  3'b1zz:
                      \$next\data_out  = \$45 ;
                  3'hz:
                      \$next\data_out  = \$47 ;
                endcase
            1'hz:
                \$next\data_out  = data_out_reg;
          endcase
      3'bz1z:
          casez ({ \$53 , \$51 , \$49  })
            3'bzz1:
                \$next\data_out  = { ones, zeros, ones, zeros };
            3'bz1z:
                \$next\data_out  = \$55 ;
            3'b1zz:
                \$next\data_out  = \$57 ;
            3'hz:
                \$next\data_out  = \$59 ;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\data_out  = 32'd0;
    endcase
  end
  always @* begin
    \$next\data_out_ctr  = data_out_ctr;
    casez ({ \$69 , \$63 , \$61  })
      3'bzz1:
          casez (\$71 )
            1'h1:
                casez ({ \$77 , \$75 , \$73  })
                  3'bzz1:
                      \$next\data_out_ctr  = 3'h4;
                  3'bz1z:
                      \$next\data_out_ctr  = 3'h3;
                  3'b1zz:
                      \$next\data_out_ctr  = 3'h3;
                  3'hz:
                      \$next\data_out_ctr  = 3'h2;
                endcase
            1'hz:
                \$next\data_out_ctr  = data_out_ctr_reg;
          endcase
      3'bz1z:
          casez ({ \$83 , \$81 , \$79  })
            3'bzz1:
                \$next\data_out_ctr  = 3'h4;
            3'bz1z:
                \$next\data_out_ctr  = 3'h3;
            3'b1zz:
                \$next\data_out_ctr  = 3'h3;
            3'hz:
                \$next\data_out_ctr  = 3'h2;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\data_out_ctr  = 3'h0;
    endcase
  end
  always @* begin
    \$next\o_busy  = o_busy;
    casez ({ \$93 , \$87 , \$85  })
      3'bzz1:
          \$next\o_busy  = 1'h0;
      3'bz1z:
          \$next\o_busy  = 1'h0;
      3'b1zz:
          \$next\o_busy  = \$99 ;
    endcase
    casez (rst)
      1'h1:
          \$next\o_busy  = 1'h0;
    endcase
  end
  always @* begin
    \$next\data_out_valid  = data_out_valid;
    casez ({ \$109 , \$103 , \$101  })
      3'bzz1:
          \$next\data_out_valid  = 1'h0;
      3'bz1z:
          \$next\data_out_valid  = 1'h0;
      3'b1zz:
          \$next\data_out_valid  = \$115 ;
    endcase
    casez (rst)
      1'h1:
          \$next\data_out_valid  = 1'h0;
    endcase
  end
  always @* begin
    \$next\data_out_reg  = data_out_reg;
    casez (\$117 )
      1'h1:
          casez ({ \$123 , \$121 , \$119  })
            3'bzz1:
                \$next\data_out_reg  = { ones, zeros, ones, zeros };
            3'bz1z:
                \$next\data_out_reg  = \$125 ;
            3'b1zz:
                \$next\data_out_reg  = \$127 ;
            3'hz:
                \$next\data_out_reg  = \$129 ;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\data_out_reg  = 32'd0;
    endcase
  end
  always @* begin
    \$next\data_out_ctr_reg  = data_out_ctr_reg;
    casez (\$131 )
      1'h1:
          casez ({ \$137 , \$135 , \$133  })
            3'bzz1:
                \$next\data_out_ctr_reg  = 3'h4;
            3'bz1z:
                \$next\data_out_ctr_reg  = 3'h3;
            3'b1zz:
                \$next\data_out_ctr_reg  = 3'h3;
            3'hz:
                \$next\data_out_ctr_reg  = 3'h2;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\data_out_ctr_reg  = 3'h0;
    endcase
  end
endmodule

