/* tb_fsm_counter.sv */

`timescale 1ns/1ps

module tb_fsm_counter ();

    logic clk, A;
    logic reset;
    logic unlock, unlock_comb, unlock_comb_reg;

    fsm_counter          dut0(.clk(clk), .reset(reset), .A(A), .unlock(unlock));
    fsm_counter_combined dut1(.clk(clk), .reset(reset), .A(A), .unlock_reg(unlock_comb_reg), .unlock(unlock_comb));

    // clk sinyali olustur
    always
    begin
        clk = 0; #5; clk = 1; #5;
    end

    // active-high reset
    initial
    begin
        A = 0; reset = 1; #20;
        reset = 0; A = 1; #200;
        A = 0; #100;
        A = 1; #200;
        $stop;
    end

endmodule
