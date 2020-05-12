/* tb_fsm_tick.sv
 *
 * 001 pattern yakalamak icin, mealy ve moore testbench
 */

`timescale 1ns/1ps

module tb_fsm_tick ();

    logic clk, A;
    logic reset;
    logic tick, tick_en;

    fsm_tick    dut0(.clk(clk), .reset(reset),        .tick(tick));
    fsm_tick_en dut1(.clk(clk), .reset(reset), .A(A), .tick(tick_en));

    // clk sinyali olustur
    always
    begin
        clk = 0; #5; clk = 1; #5;
    end

    // active-high reset
    initial
    begin
        A = 0; reset = 1; #20;
        reset = 0; A = 1;
        #100; // buraya kadar ikisi ayni kalmasi lazim
        A = 0;
        #30; // burada enabled olan 0 statinde kalmasi lazim
        A = 1;
        #100; // enabled olani tekrar saymaya baslat, ikisi bekleme suresine bagli olarak ayni olmaya bilir.
        $stop;
    end

endmodule
