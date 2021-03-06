/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(regs_en, full_rst, \$signal , \$signal$1 , \$signal$2 , \$signal$3 , \$signal$4 , \$signal$5 , \$signal$6 , \$signal$7 , full_clk);
  wire [32:0] \$11 ;
  wire [32:0] \$12 ;
  wire [32:0] \$14 ;
  wire [32:0] \$15 ;
  wire [32:0] \$17 ;
  wire [32:0] \$18 ;
  wire [32:0] \$20 ;
  wire [32:0] \$21 ;
  wire [32:0] \$23 ;
  wire [32:0] \$24 ;
  wire [32:0] \$26 ;
  wire [32:0] \$27 ;
  wire [32:0] \$29 ;
  wire [32:0] \$30 ;
  wire [32:0] \$8 ;
  wire [32:0] \$9 ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal$1 ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal$2 ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal$3 ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal$4 ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal$5 ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal$6 ;
  (* src = "debug_module.py:36" *)
  reg [31:0] \$next$signal$7 ;
  (* src = "clk_domains.py:5" *)
  reg \$next\clk ;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal ;
  reg [31:0] \$signal  = 32'd0;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal$1 ;
  reg [31:0] \$signal$1  = 32'd0;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal$2 ;
  reg [31:0] \$signal$2  = 32'd0;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal$3 ;
  reg [31:0] \$signal$3  = 32'd0;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal$4 ;
  reg [31:0] \$signal$4  = 32'd0;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal$5 ;
  reg [31:0] \$signal$5  = 32'd0;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal$6 ;
  reg [31:0] \$signal$6  = 32'd0;
  (* init = 32'd0 *)
  (* src = "debug_module.py:36" *)
  output [31:0] \$signal$7 ;
  reg [31:0] \$signal$7  = 32'd0;
  (* src = "clk_domains.py:5" *)
  wire clk;
  (* src = "clk_domains.py:4" *)
  input full_clk;
  (* src = "clk_domains.py:4" *)
  input full_rst;
  (* src = "debug_module.py:37" *)
  input [7:0] regs_en;
  assign \$9  = \$signal  + (* src = "debug_module.py:52" *) 1'h1;
  assign \$12  = \$signal$1  + (* src = "debug_module.py:52" *) 1'h1;
  assign \$15  = \$signal$2  + (* src = "debug_module.py:52" *) 1'h1;
  assign \$18  = \$signal$3  + (* src = "debug_module.py:52" *) 1'h1;
  assign \$21  = \$signal$4  + (* src = "debug_module.py:52" *) 1'h1;
  assign \$24  = \$signal$5  + (* src = "debug_module.py:52" *) 1'h1;
  assign \$27  = \$signal$6  + (* src = "debug_module.py:52" *) 1'h1;
  assign \$30  = \$signal$7  + (* src = "debug_module.py:52" *) 1'h1;
  always @(posedge full_clk)
      \$signal$7  <= \$next$signal$7 ;
  always @(posedge full_clk)
      \$signal$6  <= \$next$signal$6 ;
  always @(posedge full_clk)
      \$signal$5  <= \$next$signal$5 ;
  always @(posedge full_clk)
      \$signal$4  <= \$next$signal$4 ;
  always @(posedge full_clk)
      \$signal$3  <= \$next$signal$3 ;
  always @(posedge full_clk)
      \$signal$2  <= \$next$signal$2 ;
  always @(posedge full_clk)
      \$signal$1  <= \$next$signal$1 ;
  always @(posedge full_clk)
      \$signal  <= \$next$signal ;
  always @* begin
    \$next\clk  = 1'h0;
    \$next\clk  = full_clk;
  end
  always @* begin
    \$next$signal  = \$signal ;
    casez (regs_en[0])
      1'h1:
          \$next$signal  = \$8 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal  = 32'd0;
    endcase
  end
  always @* begin
    \$next$signal$1  = \$signal$1 ;
    casez (regs_en[1])
      1'h1:
          \$next$signal$1  = \$11 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal$1  = 32'd0;
    endcase
  end
  always @* begin
    \$next$signal$2  = \$signal$2 ;
    casez (regs_en[2])
      1'h1:
          \$next$signal$2  = \$14 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal$2  = 32'd0;
    endcase
  end
  always @* begin
    \$next$signal$3  = \$signal$3 ;
    casez (regs_en[3])
      1'h1:
          \$next$signal$3  = \$17 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal$3  = 32'd0;
    endcase
  end
  always @* begin
    \$next$signal$4  = \$signal$4 ;
    casez (regs_en[4])
      1'h1:
          \$next$signal$4  = \$20 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal$4  = 32'd0;
    endcase
  end
  always @* begin
    \$next$signal$5  = \$signal$5 ;
    casez (regs_en[5])
      1'h1:
          \$next$signal$5  = \$23 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal$5  = 32'd0;
    endcase
  end
  always @* begin
    \$next$signal$6  = \$signal$6 ;
    casez (regs_en[6])
      1'h1:
          \$next$signal$6  = \$26 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal$6  = 32'd0;
    endcase
  end
  always @* begin
    \$next$signal$7  = \$signal$7 ;
    casez (regs_en[7])
      1'h1:
          \$next$signal$7  = \$29 [31:0];
    endcase
    casez (full_rst)
      1'h1:
          \$next$signal$7  = 32'd0;
    endcase
  end
  assign \$8  = \$9 ;
  assign \$11  = \$12 ;
  assign \$14  = \$15 ;
  assign \$17  = \$18 ;
  assign \$20  = \$21 ;
  assign \$23  = \$24 ;
  assign \$26  = \$27 ;
  assign \$29  = \$30 ;
  assign clk = \$next\clk ;
endmodule

