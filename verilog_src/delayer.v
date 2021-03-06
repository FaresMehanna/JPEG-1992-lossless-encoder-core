/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(rst, clk, out_sig, in_sig);
  wire [3:0] \$1 ;
  wire [3:0] \$2 ;
  wire \$4 ;
  wire \$6 ;
  (* src = "delayer.py:11" *)
  reg \$next\out_sig ;
  (* src = "delayer.py:19" *)
  reg \$next\out_val ;
  (* src = "delayer.py:12" *)
  reg [2:0] \$next\timer ;
  (* src = "delayer.py:18" *)
  reg \$next\timer_start ;
  (* src = "nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "delayer.py:10" *)
  input in_sig;
  (* src = "delayer.py:11" *)
  output out_sig;
  (* init = 1'h0 *)
  (* src = "delayer.py:19" *)
  reg out_val = 1'h0;
  (* src = "nmigen/hdl/ir.py:329" *)
  input rst;
  (* init = 3'h6 *)
  (* src = "delayer.py:12" *)
  reg [2:0] timer = 3'h6;
  (* init = 1'h0 *)
  (* src = "delayer.py:18" *)
  reg timer_start = 1'h0;
  assign \$2  = timer - (* src = "delayer.py:27" *) 1'h1;
  assign \$4  = timer == (* src = "delayer.py:29" *) 1'h0;
  assign \$6  = \$4  | (* src = "delayer.py:29" *) out_val;
  always @(posedge clk)
      out_val <= \$next\out_val ;
  always @(posedge clk)
      timer <= \$next\timer ;
  always @(posedge clk)
      timer_start <= \$next\timer_start ;
  always @* begin
    \$next\timer_start  = timer_start;
    casez (in_sig)
      1'h1:
          \$next\timer_start  = 1'h1;
    endcase
    casez (rst)
      1'h1:
          \$next\timer_start  = 1'h0;
    endcase
  end
  always @* begin
    \$next\timer  = timer;
    casez (timer_start)
      1'h1:
          \$next\timer  = \$1 [2:0];
    endcase
    casez (rst)
      1'h1:
          \$next\timer  = 3'h6;
    endcase
  end
  always @* begin
    \$next\out_val  = out_val;
    \$next\out_val  = \$6 ;
    casez (rst)
      1'h1:
          \$next\out_val  = 1'h0;
    endcase
  end
  always @* begin
    \$next\out_sig  = 1'h0;
    \$next\out_sig  = out_val;
  end
  assign \$1  = \$2 ;
  assign out_sig = \$next\out_sig ;
endmodule

