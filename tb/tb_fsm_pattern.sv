/* tb_fsm_pattern.sv
 *
 * 001 pattern yakalamak icin, mealy ve moore testbench
 */

`timescale 1ns/1ps

module tb_fsm_pattern ();

    logic clk, A;
    logic reset;
    logic unlock_mealy, unlock_moore;
    logic [15:0] pattern = 16'b1010010011010011; // 3 adet 001 pattern mevcut

    fsm_pattern_moore dut_moore(.clk(clk), .reset(reset), .A(A), .unlock(unlock_moore));
    fsm_pattern_mealy dut_mealy(.clk(clk), .reset(reset), .A(A), .unlock(unlock_mealy));

    // clk sinyali olustur
    always
    begin
        clk = 0; #5; clk = 1; #5;
    end

    // active-high reset
    initial
    begin
        A = 0; reset = 1; #20;
        reset = 0; #5; // clock rising edgele ayni anda gonder datayi
        for (int i=0; i<16; i++) begin
            A = pattern[15];
            pattern = pattern << 1'b1;
            #10;
        end
        #20;
        $stop;
    end

endmodule
