/* * operatoru ile multiplier devresi */

module mult #(parameter N = 8) (
    input  logic [N-1:0]   a, b,
    output logic [2*N-1:0] s
);

assign s = a * b;

endmodule
