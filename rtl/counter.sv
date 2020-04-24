/* n-bit sayici */

module counter #(parameter N = 8) (
    input  logic         clk, reset,
    output logic [N-1:0] count,
    output logic         done
);

logic c;

// rising edge triggered ff with async reset
always_ff @(posedge clk, negedge reset)
    if (!reset)
        {c, count} <= {N+1{1'b0}};
    else
        {c, count} <= count + 1'b1;

assign done = (c);

endmodule
