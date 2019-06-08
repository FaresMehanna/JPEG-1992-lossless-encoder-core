/* Generated by Yosys 0.8+     369 (git sha1 ea0e0722, clang 10.0.1 -fPIC -Os) */

(* \nmigen.hierarchy  = "top.buff_pick" *)
(* generator = "nMigen" *)
module buff_pick(zeros, in_signal, out_signal, buff_consum);
  (* src = "./migen_src/vbits_to_cbits.py:16" *)
  reg [31:0] \$next\out_signal ;
  (* src = "./migen_src/vbits_to_cbits.py:17" *)
  input [7:0] buff_consum;
  (* src = "./migen_src/vbits_to_cbits.py:15" *)
  input [143:0] in_signal;
  (* src = "./migen_src/vbits_to_cbits.py:16" *)
  output [31:0] out_signal;
  (* src = "./migen_src/vbits_to_cbits.py:24" *)
  input [31:0] zeros;
  always @* begin
    \$next\out_signal  = 32'd0;
    casez (buff_consum)
      8'h01:
          \$next\out_signal  = { in_signal[0], zeros[30:0] };
      8'h02:
          \$next\out_signal  = { in_signal[1:0], zeros[29:0] };
      8'h03:
          \$next\out_signal  = { in_signal[2:0], zeros[28:0] };
      8'h04:
          \$next\out_signal  = { in_signal[3:0], zeros[27:0] };
      8'h05:
          \$next\out_signal  = { in_signal[4:0], zeros[26:0] };
      8'h06:
          \$next\out_signal  = { in_signal[5:0], zeros[25:0] };
      8'h07:
          \$next\out_signal  = { in_signal[6:0], zeros[24:0] };
      8'h08:
          \$next\out_signal  = { in_signal[7:0], zeros[23:0] };
      8'h09:
          \$next\out_signal  = { in_signal[8:0], zeros[22:0] };
      8'h0a:
          \$next\out_signal  = { in_signal[9:0], zeros[21:0] };
      8'h0b:
          \$next\out_signal  = { in_signal[10:0], zeros[20:0] };
      8'h0c:
          \$next\out_signal  = { in_signal[11:0], zeros[19:0] };
      8'h0d:
          \$next\out_signal  = { in_signal[12:0], zeros[18:0] };
      8'h0e:
          \$next\out_signal  = { in_signal[13:0], zeros[17:0] };
      8'h0f:
          \$next\out_signal  = { in_signal[14:0], zeros[16:0] };
      8'h10:
          \$next\out_signal  = { in_signal[15:0], zeros[15:0] };
      8'h11:
          \$next\out_signal  = { in_signal[16:0], zeros[14:0] };
      8'h12:
          \$next\out_signal  = { in_signal[17:0], zeros[13:0] };
      8'h13:
          \$next\out_signal  = { in_signal[18:0], zeros[12:0] };
      8'h14:
          \$next\out_signal  = { in_signal[19:0], zeros[11:0] };
      8'h15:
          \$next\out_signal  = { in_signal[20:0], zeros[10:0] };
      8'h16:
          \$next\out_signal  = { in_signal[21:0], zeros[9:0] };
      8'h17:
          \$next\out_signal  = { in_signal[22:0], zeros[8:0] };
      8'h18:
          \$next\out_signal  = { in_signal[23:0], zeros[7:0] };
      8'h19:
          \$next\out_signal  = { in_signal[24:0], zeros[6:0] };
      8'h1a:
          \$next\out_signal  = { in_signal[25:0], zeros[5:0] };
      8'h1b:
          \$next\out_signal  = { in_signal[26:0], zeros[4:0] };
      8'h1c:
          \$next\out_signal  = { in_signal[27:0], zeros[3:0] };
      8'h1d:
          \$next\out_signal  = { in_signal[28:0], zeros[2:0] };
      8'h1e:
          \$next\out_signal  = { in_signal[29:0], zeros[1:0] };
      8'h1f:
          \$next\out_signal  = { in_signal[30:0], zeros[0] };
      8'h20:
          \$next\out_signal  = in_signal[31:0];
      8'h21:
          \$next\out_signal  = in_signal[32:1];
      8'h22:
          \$next\out_signal  = in_signal[33:2];
      8'h23:
          \$next\out_signal  = in_signal[34:3];
      8'h24:
          \$next\out_signal  = in_signal[35:4];
      8'h25:
          \$next\out_signal  = in_signal[36:5];
      8'h26:
          \$next\out_signal  = in_signal[37:6];
      8'h27:
          \$next\out_signal  = in_signal[38:7];
      8'h28:
          \$next\out_signal  = in_signal[39:8];
      8'h29:
          \$next\out_signal  = in_signal[40:9];
      8'h2a:
          \$next\out_signal  = in_signal[41:10];
      8'h2b:
          \$next\out_signal  = in_signal[42:11];
      8'h2c:
          \$next\out_signal  = in_signal[43:12];
      8'h2d:
          \$next\out_signal  = in_signal[44:13];
      8'h2e:
          \$next\out_signal  = in_signal[45:14];
      8'h2f:
          \$next\out_signal  = in_signal[46:15];
      8'h30:
          \$next\out_signal  = in_signal[47:16];
      8'h31:
          \$next\out_signal  = in_signal[48:17];
      8'h32:
          \$next\out_signal  = in_signal[49:18];
      8'h33:
          \$next\out_signal  = in_signal[50:19];
      8'h34:
          \$next\out_signal  = in_signal[51:20];
      8'h35:
          \$next\out_signal  = in_signal[52:21];
      8'h36:
          \$next\out_signal  = in_signal[53:22];
      8'h37:
          \$next\out_signal  = in_signal[54:23];
      8'h38:
          \$next\out_signal  = in_signal[55:24];
      8'h39:
          \$next\out_signal  = in_signal[56:25];
      8'h3a:
          \$next\out_signal  = in_signal[57:26];
      8'h3b:
          \$next\out_signal  = in_signal[58:27];
      8'h3c:
          \$next\out_signal  = in_signal[59:28];
      8'h3d:
          \$next\out_signal  = in_signal[60:29];
      8'h3e:
          \$next\out_signal  = in_signal[61:30];
      8'h3f:
          \$next\out_signal  = in_signal[62:31];
      8'h40:
          \$next\out_signal  = in_signal[63:32];
      8'h41:
          \$next\out_signal  = in_signal[64:33];
      8'h42:
          \$next\out_signal  = in_signal[65:34];
      8'h43:
          \$next\out_signal  = in_signal[66:35];
      8'h44:
          \$next\out_signal  = in_signal[67:36];
      8'h45:
          \$next\out_signal  = in_signal[68:37];
      8'h46:
          \$next\out_signal  = in_signal[69:38];
      8'h47:
          \$next\out_signal  = in_signal[70:39];
      8'h48:
          \$next\out_signal  = in_signal[71:40];
      8'h49:
          \$next\out_signal  = in_signal[72:41];
      8'h4a:
          \$next\out_signal  = in_signal[73:42];
      8'h4b:
          \$next\out_signal  = in_signal[74:43];
      8'h4c:
          \$next\out_signal  = in_signal[75:44];
      8'h4d:
          \$next\out_signal  = in_signal[76:45];
      8'h4e:
          \$next\out_signal  = in_signal[77:46];
      8'h4f:
          \$next\out_signal  = in_signal[78:47];
      8'h50:
          \$next\out_signal  = in_signal[79:48];
      8'h51:
          \$next\out_signal  = in_signal[80:49];
      8'h52:
          \$next\out_signal  = in_signal[81:50];
      8'h53:
          \$next\out_signal  = in_signal[82:51];
      8'h54:
          \$next\out_signal  = in_signal[83:52];
      8'h55:
          \$next\out_signal  = in_signal[84:53];
      8'h56:
          \$next\out_signal  = in_signal[85:54];
      8'h57:
          \$next\out_signal  = in_signal[86:55];
      8'h58:
          \$next\out_signal  = in_signal[87:56];
      8'h59:
          \$next\out_signal  = in_signal[88:57];
      8'h5a:
          \$next\out_signal  = in_signal[89:58];
      8'h5b:
          \$next\out_signal  = in_signal[90:59];
      8'h5c:
          \$next\out_signal  = in_signal[91:60];
      8'h5d:
          \$next\out_signal  = in_signal[92:61];
      8'h5e:
          \$next\out_signal  = in_signal[93:62];
      8'h5f:
          \$next\out_signal  = in_signal[94:63];
      8'h60:
          \$next\out_signal  = in_signal[95:64];
      8'h61:
          \$next\out_signal  = in_signal[96:65];
      8'h62:
          \$next\out_signal  = in_signal[97:66];
      8'h63:
          \$next\out_signal  = in_signal[98:67];
      8'h64:
          \$next\out_signal  = in_signal[99:68];
      8'h65:
          \$next\out_signal  = in_signal[100:69];
      8'h66:
          \$next\out_signal  = in_signal[101:70];
      8'h67:
          \$next\out_signal  = in_signal[102:71];
      8'h68:
          \$next\out_signal  = in_signal[103:72];
      8'h69:
          \$next\out_signal  = in_signal[104:73];
      8'h6a:
          \$next\out_signal  = in_signal[105:74];
      8'h6b:
          \$next\out_signal  = in_signal[106:75];
      8'h6c:
          \$next\out_signal  = in_signal[107:76];
      8'h6d:
          \$next\out_signal  = in_signal[108:77];
      8'h6e:
          \$next\out_signal  = in_signal[109:78];
      8'h6f:
          \$next\out_signal  = in_signal[110:79];
      8'h70:
          \$next\out_signal  = in_signal[111:80];
      8'h71:
          \$next\out_signal  = in_signal[112:81];
      8'h72:
          \$next\out_signal  = in_signal[113:82];
      8'h73:
          \$next\out_signal  = in_signal[114:83];
      8'h74:
          \$next\out_signal  = in_signal[115:84];
      8'h75:
          \$next\out_signal  = in_signal[116:85];
      8'h76:
          \$next\out_signal  = in_signal[117:86];
      8'h77:
          \$next\out_signal  = in_signal[118:87];
      8'h78:
          \$next\out_signal  = in_signal[119:88];
      8'h79:
          \$next\out_signal  = in_signal[120:89];
      8'h7a:
          \$next\out_signal  = in_signal[121:90];
      8'h7b:
          \$next\out_signal  = in_signal[122:91];
      8'h7c:
          \$next\out_signal  = in_signal[123:92];
      8'h7d:
          \$next\out_signal  = in_signal[124:93];
      8'h7e:
          \$next\out_signal  = in_signal[125:94];
      8'h7f:
          \$next\out_signal  = in_signal[126:95];
      8'h80:
          \$next\out_signal  = in_signal[127:96];
      8'h81:
          \$next\out_signal  = in_signal[128:97];
      8'h82:
          \$next\out_signal  = in_signal[129:98];
      8'h83:
          \$next\out_signal  = in_signal[130:99];
      8'h84:
          \$next\out_signal  = in_signal[131:100];
      8'h85:
          \$next\out_signal  = in_signal[132:101];
      8'h86:
          \$next\out_signal  = in_signal[133:102];
      8'h87:
          \$next\out_signal  = in_signal[134:103];
      8'h88:
          \$next\out_signal  = in_signal[135:104];
      8'h89:
          \$next\out_signal  = in_signal[136:105];
      8'h8a:
          \$next\out_signal  = in_signal[137:106];
      8'h8b:
          \$next\out_signal  = in_signal[138:107];
      8'h8c:
          \$next\out_signal  = in_signal[139:108];
      8'h8d:
          \$next\out_signal  = in_signal[140:109];
      8'h8e:
          \$next\out_signal  = in_signal[141:110];
      8'h8f:
          \$next\out_signal  = in_signal[142:111];
      8'h90:
          \$next\out_signal  = in_signal[143:112];
    endcase
  end
  assign out_signal = \$next\out_signal ;
endmodule

(* \nmigen.hierarchy  = "top.buff_set" *)
(* generator = "nMigen" *)
module buff_set(enc_in_ctr, enc_in, rst, clk, buff, latch);
  wire [206:0] \$1 ;
  wire [206:0] \$2 ;
  wire [206:0] \$4 ;
  (* src = "./migen_src/vbits_to_cbits.py:49" *)
  reg [143:0] \$next\buff ;
  (* init = 144'h000000000000000000000000000000000000 *)
  (* src = "./migen_src/vbits_to_cbits.py:49" *)
  output [143:0] buff;
  reg [143:0] buff = 144'h000000000000000000000000000000000000;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* src = "./migen_src/vbits_to_cbits.py:47" *)
  input [47:0] enc_in;
  (* src = "./migen_src/vbits_to_cbits.py:48" *)
  input [5:0] enc_in_ctr;
  (* src = "./migen_src/vbits_to_cbits.py:50" *)
  input latch;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  assign \$2  = buff <<< (* src = "./migen_src/vbits_to_cbits.py:61" *) enc_in_ctr;
  assign \$4  = \$2  | (* src = "./migen_src/vbits_to_cbits.py:61" *) enc_in;
  always @(posedge clk)
      buff <= \$next\buff ;
  always @* begin
    \$next\buff  = buff;
    casez (latch)
      1'h1:
          \$next\buff  = \$1 [143:0];
    endcase
    casez (rst)
      1'h1:
          \$next\buff  = 144'h000000000000000000000000000000000000;
    endcase
  end
  assign \$1  = \$4 ;
endmodule

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(enc_in_ctr, busy_in, valid_in, in_end, rst, clk, zeros, data_out, valid_out, latch_input, end_out, enc_in);
  wire \$1 ;
  wire [9:0] \$100 ;
  wire [8:0] \$102 ;
  wire [8:0] \$103 ;
  wire [8:0] \$105 ;
  wire [8:0] \$106 ;
  wire \$108 ;
  wire \$11 ;
  wire \$13 ;
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
  wire \$91 ;
  wire \$93 ;
  wire \$95 ;
  wire [9:0] \$97 ;
  wire [8:0] \$98 ;
  (* src = "./migen_src/vbits_to_cbits.py:99" *)
  reg [143:0] \$next\buff ;
  (* src = "./migen_src/vbits_to_cbits.py:100" *)
  reg [7:0] \$next\buff_consum ;
  (* src = "./migen_src/vbits_to_cbits.py:17" *)
  reg [7:0] \$next\buff_pick_buff_consum ;
  (* src = "./migen_src/vbits_to_cbits.py:15" *)
  reg [143:0] \$next\buff_pick_in_signal ;
  (* src = "./migen_src/vbits_to_cbits.py:47" *)
  reg [47:0] \$next\buff_set_enc_in ;
  (* src = "./migen_src/vbits_to_cbits.py:48" *)
  reg [5:0] \$next\buff_set_enc_in_ctr ;
  (* src = "./migen_src/vbits_to_cbits.py:50" *)
  reg \$next\buff_set_latch ;
  (* src = "./migen_src/vbits_to_cbits.py:113" *)
  reg \$next\buff_set_latch$9 ;
  (* src = "./migen_src/vbits_to_cbits.py:103" *)
  reg [31:0] \$next\buffered_output ;
  (* src = "./migen_src/vbits_to_cbits.py:132" *)
  reg \$next\current_end ;
  (* src = "./migen_src/vbits_to_cbits.py:81" *)
  reg [31:0] \$next\data_out ;
  (* src = "./migen_src/vbits_to_cbits.py:83" *)
  reg \$next\end_out ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/dsl.py:244" *)
  reg \$next\fsm_state ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/dsl.py:244" *)
  reg [1:0] \$next\fsm_state$10 ;
  (* src = "./migen_src/vbits_to_cbits.py:75" *)
  reg \$next\latch_input ;
  (* src = "./migen_src/vbits_to_cbits.py:175" *)
  reg [7:0] \$next\new_consum ;
  (* src = "./migen_src/vbits_to_cbits.py:102" *)
  reg [31:0] \$next\output ;
  (* src = "./migen_src/vbits_to_cbits.py:124" *)
  reg \$next\sig1 ;
  (* src = "./migen_src/vbits_to_cbits.py:125" *)
  reg \$next\sig2 ;
  (* src = "./migen_src/vbits_to_cbits.py:82" *)
  reg \$next\valid_out ;
  (* src = "./migen_src/vbits_to_cbits.py:99" *)
  wire [143:0] buff;
  (* init = 8'h00 *)
  (* src = "./migen_src/vbits_to_cbits.py:100" *)
  reg [7:0] buff_consum = 8'h00;
  (* src = "./migen_src/vbits_to_cbits.py:17" *)
  wire [7:0] buff_pick_buff_consum;
  (* src = "./migen_src/vbits_to_cbits.py:15" *)
  wire [143:0] buff_pick_in_signal;
  (* src = "./migen_src/vbits_to_cbits.py:16" *)
  wire [31:0] buff_pick_out_signal;
  (* src = "./migen_src/vbits_to_cbits.py:49" *)
  wire [143:0] buff_set_buff;
  (* src = "./migen_src/vbits_to_cbits.py:47" *)
  wire [47:0] buff_set_enc_in;
  (* src = "./migen_src/vbits_to_cbits.py:48" *)
  wire [5:0] buff_set_enc_in_ctr;
  (* src = "./migen_src/vbits_to_cbits.py:50" *)
  wire buff_set_latch;
  (* src = "./migen_src/vbits_to_cbits.py:113" *)
  wire \buff_set_latch$9 ;
  (* init = 32'd0 *)
  (* src = "./migen_src/vbits_to_cbits.py:103" *)
  reg [31:0] buffered_output = 32'd0;
  (* src = "./migen_src/vbits_to_cbits.py:85" *)
  input busy_in;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input clk;
  (* init = 1'h0 *)
  (* src = "./migen_src/vbits_to_cbits.py:132" *)
  reg current_end = 1'h0;
  (* init = 32'd0 *)
  (* src = "./migen_src/vbits_to_cbits.py:81" *)
  output [31:0] data_out;
  reg [31:0] data_out = 32'd0;
  (* src = "./migen_src/vbits_to_cbits.py:76" *)
  input [47:0] enc_in;
  (* src = "./migen_src/vbits_to_cbits.py:77" *)
  input [5:0] enc_in_ctr;
  (* init = 1'h0 *)
  (* src = "./migen_src/vbits_to_cbits.py:83" *)
  output end_out;
  reg end_out = 1'h0;
  (* init = 1'h0 *)
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/dsl.py:244" *)
  reg fsm_state = 1'h0;
  (* init = 2'h0 *)
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/dsl.py:244" *)
  reg [1:0] \fsm_state$10  = 2'h0;
  (* src = "./migen_src/vbits_to_cbits.py:78" *)
  input in_end;
  (* init = 1'h0 *)
  (* src = "./migen_src/vbits_to_cbits.py:75" *)
  output latch_input;
  reg latch_input = 1'h0;
  (* src = "./migen_src/vbits_to_cbits.py:175" *)
  wire [7:0] new_consum;
  (* src = "./migen_src/vbits_to_cbits.py:102" *)
  wire [31:0] \output ;
  (* src = "/anaconda3/envs/py36/lib/python3.6/site-packages/nmigen/hdl/ir.py:329" *)
  input rst;
  (* src = "./migen_src/vbits_to_cbits.py:124" *)
  wire sig1;
  (* src = "./migen_src/vbits_to_cbits.py:125" *)
  wire sig2;
  (* src = "./migen_src/vbits_to_cbits.py:79" *)
  input valid_in;
  (* init = 1'h0 *)
  (* src = "./migen_src/vbits_to_cbits.py:82" *)
  output valid_out;
  reg valid_out = 1'h0;
  (* src = "./migen_src/vbits_to_cbits.py:24" *)
  input [31:0] zeros;
  assign \$100  = \$98  + (* src = "./migen_src/vbits_to_cbits.py:218" *) enc_in_ctr;
  assign \$103  = buff_consum - (* src = "./migen_src/vbits_to_cbits.py:220" *) 6'h20;
  assign \$106  = buff_consum + (* src = "./migen_src/vbits_to_cbits.py:222" *) enc_in_ctr;
  assign \$108  = sig1 | (* src = "./migen_src/vbits_to_cbits.py:224" *) sig2;
  assign \$11  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$13  = buff_consum < (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$15  = \$13  & (* src = "./migen_src/vbits_to_cbits.py:139" *) current_end;
  assign \$17  = \$11  | (* src = "./migen_src/vbits_to_cbits.py:139" *) \$15 ;
  assign \$1  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:154" *) 1'h0;
  assign \$19  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:154" *) 1'h0;
  assign \$21  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:154" *) 6'h20;
  assign \$23  = \$19  & (* src = "./migen_src/vbits_to_cbits.py:154" *) \$21 ;
  assign \$25  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:161" *) 1'h0;
  assign \$27  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$29  = buff_consum < (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$31  = \$29  & (* src = "./migen_src/vbits_to_cbits.py:139" *) current_end;
  assign \$33  = \$27  | (* src = "./migen_src/vbits_to_cbits.py:139" *) \$31 ;
  assign \$35  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:154" *) 1'h0;
  assign \$37  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:154" *) 6'h20;
  assign \$3  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:154" *) 6'h20;
  assign \$39  = \$35  & (* src = "./migen_src/vbits_to_cbits.py:154" *) \$37 ;
  assign \$41  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:161" *) 1'h0;
  assign \$43  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$45  = buff_consum < (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$47  = \$45  & (* src = "./migen_src/vbits_to_cbits.py:139" *) current_end;
  assign \$49  = \$43  | (* src = "./migen_src/vbits_to_cbits.py:139" *) \$47 ;
  assign \$51  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:154" *) 1'h0;
  assign \$53  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:154" *) 6'h20;
  assign \$55  = \$51  & (* src = "./migen_src/vbits_to_cbits.py:154" *) \$53 ;
  assign \$57  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:161" *) 1'h0;
  assign \$5  = \$1  & (* src = "./migen_src/vbits_to_cbits.py:154" *) \$3 ;
  assign \$59  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$61  = buff_consum < (* src = "./migen_src/vbits_to_cbits.py:139" *) 6'h20;
  assign \$63  = \$61  & (* src = "./migen_src/vbits_to_cbits.py:139" *) current_end;
  assign \$65  = \$59  | (* src = "./migen_src/vbits_to_cbits.py:139" *) \$63 ;
  assign \$67  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:154" *) 1'h0;
  assign \$69  = buff_consum >= (* src = "./migen_src/vbits_to_cbits.py:154" *) 6'h20;
  assign \$71  = \$67  & (* src = "./migen_src/vbits_to_cbits.py:154" *) \$69 ;
  assign \$73  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:161" *) 1'h0;
  assign \$75  = buff_consum <= (* src = "./migen_src/vbits_to_cbits.py:147" *) 6'h20;
  assign \$77  = \$75  & (* src = "./migen_src/vbits_to_cbits.py:147" *) current_end;
  assign \$7  = busy_in == (* src = "./migen_src/vbits_to_cbits.py:161" *) 1'h0;
  assign \$79  = buff_consum <= (* src = "./migen_src/vbits_to_cbits.py:170" *) 6'h20;
  assign \$81  = \$79  & (* src = "./migen_src/vbits_to_cbits.py:170" *) current_end;
  assign \$83  = buff_consum <= (* src = "./migen_src/vbits_to_cbits.py:179" *) 7'h60;
  assign \$85  = new_consum <= (* src = "./migen_src/vbits_to_cbits.py:192" *) 7'h60;
  assign \$87  = new_consum <= (* src = "./migen_src/vbits_to_cbits.py:207" *) 7'h60;
  assign \$89  = buff_consum <= (* src = "./migen_src/vbits_to_cbits.py:179" *) 7'h60;
  assign \$91  = new_consum <= (* src = "./migen_src/vbits_to_cbits.py:192" *) 7'h60;
  assign \$93  = new_consum <= (* src = "./migen_src/vbits_to_cbits.py:207" *) 7'h60;
  assign \$95  = sig1 & (* src = "./migen_src/vbits_to_cbits.py:217" *) sig2;
  assign \$98  = buff_consum - (* src = "./migen_src/vbits_to_cbits.py:218" *) 6'h20;
  always @(posedge clk)
      buff_consum <= \$next\buff_consum ;
  always @(posedge clk)
      current_end <= \$next\current_end ;
  always @(posedge clk)
      \fsm_state$10  <= \$next\fsm_state$10 ;
  always @(posedge clk)
      latch_input <= \$next\latch_input ;
  always @(posedge clk)
      end_out <= \$next\end_out ;
  always @(posedge clk)
      fsm_state <= \$next\fsm_state ;
  always @(posedge clk)
      buffered_output <= \$next\buffered_output ;
  always @(posedge clk)
      valid_out <= \$next\valid_out ;
  always @(posedge clk)
      data_out <= \$next\data_out ;
  buff_pick buff_pick (
    .buff_consum(buff_pick_buff_consum),
    .in_signal(buff_pick_in_signal),
    .out_signal(buff_pick_out_signal),
    .zeros(zeros)
  );
  buff_set buff_set (
    .buff(buff_set_buff),
    .clk(clk),
    .enc_in(buff_set_enc_in),
    .enc_in_ctr(buff_set_enc_in_ctr),
    .latch(buff_set_latch),
    .rst(rst)
  );
  always @* begin
    \$next\data_out  = data_out;
    \$next\data_out  = \output ;
    casez (fsm_state)
      1'h1:
          casez ({ \$7 , \$5  })
            2'bz1:
                /* empty */;
            2'b1z:
                /* empty */;
            2'hz:
                \$next\data_out  = buffered_output;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\data_out  = 32'd0;
    endcase
  end
  always @* begin
    \$next\buff_pick_in_signal  = 144'h000000000000000000000000000000000000;
    \$next\buff_pick_in_signal  = buff;
  end
  always @* begin
    \$next\sig2  = 1'h0;
    \$next\sig2  = \buff_set_latch$9 ;
  end
  always @* begin
    \$next\valid_out  = valid_out;
    casez (fsm_state)
      1'h0:
          casez (\$33 )
            1'h1:
                \$next\valid_out  = 1'h1;
          endcase
      1'h1:
          casez ({ \$41 , \$39  })
            2'bz1:
                \$next\valid_out  = 1'h1;
            2'b1z:
                \$next\valid_out  = 1'h0;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\valid_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\buffered_output  = buffered_output;
    casez (fsm_state)
      1'h0:
          casez (\$49 )
            1'h1:
                \$next\buffered_output  = \output ;
          endcase
      1'h1:
          casez ({ \$57 , \$55  })
            2'bz1:
                \$next\buffered_output  = \output ;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\buffered_output  = 32'd0;
    endcase
  end
  always @* begin
    \$next\fsm_state  = fsm_state;
    casez (fsm_state)
      1'h0:
          casez (\$65 )
            1'h1:
                \$next\fsm_state  = 1'h1;
          endcase
      1'h1:
          casez ({ \$73 , \$71  })
            2'bz1:
                /* empty */;
            2'b1z:
                \$next\fsm_state  = 1'h0;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fsm_state  = 1'h0;
    endcase
  end
  always @* begin
    \$next\end_out  = end_out;
    casez (fsm_state)
      1'h0:
          casez (\$77 )
            1'h1:
                \$next\end_out  = 1'h1;
          endcase
      1'h1:
          casez (\$81 )
            1'h1:
                \$next\end_out  = 1'h1;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\end_out  = 1'h0;
    endcase
  end
  always @* begin
    \$next\latch_input  = latch_input;
    casez (\fsm_state$10 )
      2'h0:
          casez (\$83 )
            1'h1:
                casez (valid_in)
                  1'h1:
                      \$next\latch_input  = 1'h1;
                endcase
          endcase
      2'h1:
          casez (valid_in)
            1'h1:
                casez (\$85 )
                  1'h1:
                      /* empty */;
                  1'hz:
                      \$next\latch_input  = 1'h0;
                endcase
          endcase
      2'h2:
          casez (valid_in)
            1'h1:
                casez (\$87 )
                  1'h1:
                      \$next\latch_input  = 1'h1;
                  1'hz:
                      \$next\latch_input  = 1'h0;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\latch_input  = 1'h0;
    endcase
  end
  always @* begin
    \$next\fsm_state$10  = \fsm_state$10 ;
    casez (\fsm_state$10 )
      2'h0:
          casez (\$89 )
            1'h1:
                casez (valid_in)
                  1'h1:
                      \$next\fsm_state$10  = 2'h1;
                endcase
          endcase
      2'h1:
          casez (valid_in)
            1'h1:
                casez (\$91 )
                  1'h1:
                      \$next\fsm_state$10  = 2'h2;
                  1'hz:
                      \$next\fsm_state$10  = 2'h0;
                endcase
            1'hz:
                \$next\fsm_state$10  = 2'h0;
          endcase
      2'h2:
          casez (valid_in)
            1'h1:
                casez (\$93 )
                  1'h1:
                      /* empty */;
                  1'hz:
                      \$next\fsm_state$10  = 2'h0;
                endcase
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\fsm_state$10  = 2'h0;
    endcase
  end
  always @* begin
    \$next\current_end  = current_end;
    casez (\fsm_state$10 )
      2'h1:
          casez (valid_in)
            1'h1:
                \$next\current_end  = in_end;
          endcase
      2'h2:
          casez (valid_in)
            1'h1:
                \$next\current_end  = in_end;
          endcase
    endcase
    casez (rst)
      1'h1:
          \$next\current_end  = 1'h0;
    endcase
  end
  always @* begin
    \$next\new_consum  = 8'h00;
    casez ({ sig2, sig1, \$95  })
      3'bzz1:
          \$next\new_consum  = \$97 [7:0];
      3'bz1z:
          \$next\new_consum  = \$102 [7:0];
      3'b1zz:
          \$next\new_consum  = \$105 [7:0];
    endcase
  end
  always @* begin
    \$next\buff_consum  = buff_consum;
    casez (\$108 )
      1'h1:
          \$next\buff_consum  = new_consum;
    endcase
    casez (rst)
      1'h1:
          \$next\buff_consum  = 8'h00;
    endcase
  end
  always @* begin
    \$next\buff_pick_buff_consum  = 8'h00;
    \$next\buff_pick_buff_consum  = buff_consum;
  end
  always @* begin
    \$next\output  = 32'd0;
    \$next\output  = buff_pick_out_signal;
  end
  always @* begin
    \$next\buff_set_latch$9  = 1'h0;
    \$next\buff_set_latch$9  = 1'h0;
    casez (\fsm_state$10 )
      2'h1:
          casez (valid_in)
            1'h1:
                \$next\buff_set_latch$9  = 1'h1;
          endcase
      2'h2:
          casez (valid_in)
            1'h1:
                \$next\buff_set_latch$9  = 1'h1;
          endcase
    endcase
  end
  always @* begin
    \$next\buff  = 144'h000000000000000000000000000000000000;
    \$next\buff  = buff_set_buff;
  end
  always @* begin
    \$next\buff_set_enc_in  = 48'h000000000000;
    \$next\buff_set_enc_in  = enc_in;
  end
  always @* begin
    \$next\buff_set_enc_in_ctr  = 6'h00;
    \$next\buff_set_enc_in_ctr  = enc_in_ctr;
  end
  always @* begin
    \$next\buff_set_latch  = 1'h0;
    \$next\buff_set_latch  = \buff_set_latch$9 ;
  end
  always @* begin
    \$next\sig1  = 1'h0;
    \$next\sig1  = 1'h0;
    casez (fsm_state)
      1'h0:
          casez (\$17 )
            1'h1:
                \$next\sig1  = 1'h1;
          endcase
      1'h1:
          casez ({ \$25 , \$23  })
            2'bz1:
                \$next\sig1  = 1'h1;
          endcase
    endcase
  end
  assign \$97  = \$100 ;
  assign \$102  = \$103 ;
  assign \$105  = \$106 ;
  assign new_consum = \$next\new_consum ;
  assign sig2 = \$next\sig2 ;
  assign sig1 = \$next\sig1 ;
  assign buff_set_latch = \$next\buff_set_latch ;
  assign buff_set_enc_in_ctr = \$next\buff_set_enc_in_ctr ;
  assign buff_set_enc_in = \$next\buff_set_enc_in ;
  assign buff = \$next\buff ;
  assign \buff_set_latch$9  = \$next\buff_set_latch$9 ;
  assign \output  = \$next\output ;
  assign buff_pick_buff_consum = \$next\buff_pick_buff_consum ;
  assign buff_pick_in_signal = \$next\buff_pick_in_signal ;
endmodule

