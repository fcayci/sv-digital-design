/* 2-1 MUX kullanarak 4-1 MUX */

module mux4_str (
    input  logic [2:0] a, b, c, d,
    input  logic [1:0] s,
    output logic [2:0] y
);

logic [2:0] n0, n1;

mux2 #(3)     m00 (.g1( a), .g2( b), .sel(s[0]), .p(n0));
mux2 #(.W(3)) m01 (.g1( c), .g2( d), .sel(s[0]), .p(n1));
mux2 #(3)     m1  (.g1(n0), .g2(n1), .sel(s[1]), .p( y));

endmodule
