/* parametreli 2-1 MUX */

module mux2 #(parameter W = 3) (
    input  logic [W-1:0] g1, g2,
    input  logic sel,
    output logic [W-1:0] p
);

// conditional sinyal atamasi
assign p = sel ? g1 : g2;

endmodule
