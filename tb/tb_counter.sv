/* tb_counter.sv
 */

`timescale 1ns/1ps

module tb_counter ();

    localparam N = 4;

    logic         clk;
    logic         reset;
    logic [N-1:0] count;
    logic         done;

    counter  #(N) dut0(clk, reset, count, done);

    always
    begin
        clk = 0; #5; clk = 1; #5;
    end

    initial
    begin
        reset = 0; #20; reset =1;
    end

    initial
    begin
        #1000;
        $stop;
    end

endmodule
