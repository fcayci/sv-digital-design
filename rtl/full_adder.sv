/* full adder */

module full_adder (
    input  logic a, b, cin,
    output logic s, cout
);

assign s = a ^ b ^ cin;
assign cout = (a & b) | (a & cin) | (b & cin);

endmodule
