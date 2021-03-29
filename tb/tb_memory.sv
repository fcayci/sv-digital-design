/* tb_memory.sv
 */

`timescale 1ns/1ps

module tb_memory ();

    logic clk, reset;
    logic we;
    logic [2:0] waddr, addr;
    logic [15:0] din;
    logic [15:0] dout;

    memory dut0(clk, reset, we, waddr, addr, din, dout);

    always begin
        clk <= 0; #5; clk <= 1; #5;
    end

    // sadece oku
    initial
    begin
        we = 0; reset = 0; din = 16'b0;
        addr = 3'b000; # 10;
        addr = 3'b001; # 10;
        addr = 3'b010; # 10;
        addr = 3'b011; # 10;
        addr = 3'b100; # 10;
        addr = 3'b101; # 10;
        addr = 3'b110; # 10;
        addr = 3'b111; # 100;
        $stop;
    end

endmodule
