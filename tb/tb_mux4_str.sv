/* tb_mux4_str.sv
 */

`timescale 1ns/1ps

module tb_mux4_str ();

    logic [2:0] a, b, c, d;
    logic [1:0] s;
    logic [2:0] y;

    mux4_str dut0(a, b, c, d, s, y);

    initial
    begin
        a = 3'b001; b = 3'b011; c = 3'b101; d = 3'b110;

        s = 2'b00; #10;
        s = 2'b01; #10;
        s = 2'b10; #10;
        s = 2'b11; #10;

        $stop;
    end

endmodule
