/* basit bir register devresi */

module reg8 (
    input  logic       clk,
    input  logic [7:0] d,
    output logic [7:0] q
);

always_ff @(posedge clk)
    q <= d;

endmodule