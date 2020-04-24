/* farkli d-flip-flop devreleri */

module flops (
    input  logic       clk,
    input  logic       rst,
    input  logic       en,
    input  logic       d,
    output logic [6:0] q
);

// positif edge clk oldugu zaman d girisini q[0] a aktar
always @(posedge clk)
    q[0] <= d;

// yukaridaki ile ayni fakat SystemVerilog ifadesini kullanarak
always_ff @(posedge clk)
    q[1] <= d;

// negatif edge clk
always_ff @(negedge clk)
    q[2] <= d;

// async reset active-low bagli
always_ff @(posedge clk, negedge rst)
    if (!rst) q[3] <= 1'b0;
    else      q[3] <= d;

// async reset active-high bagli
always_ff @(posedge clk, posedge rst)
    if (rst) q[4] <= 1'b0;
    else     q[4] <= d;

// ff with enable
always_ff @(posedge clk)
    if(en) q[5] <= d;

// ff with enable, async reset
always_ff @(posedge clk, negedge rst)
    if (!rst)   q[6] <= 1'b0;
    else if(en) q[6] <= d;

endmodule