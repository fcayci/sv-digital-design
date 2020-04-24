/* half adder */

module half_adder (
    input  logic x, y,
    output logic s, c
);

assign s = x ^ y;
assign c = x & y;

endmodule
