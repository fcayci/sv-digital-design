/* basit bir latch devresi */

module latchy (
    input  logic clk,
    input  logic d,
    output logic q
);

// eger clk varsa d q ya atanir,
//   yoksa q degeri kendini korur
always_latch
    if (clk) q <= d;

endmodule