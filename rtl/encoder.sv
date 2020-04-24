/* 4-2 encoder */

module encoder (
    input  logic [3:0] a,
    output logic [1:0] y
);

assign y = a[3] ? 2'b01 :
           a[2] ? 2'b11 :
           a[1] ? 2'b10 :
           a[0] ? 2'b00 : 2'bzz;

endmodule
