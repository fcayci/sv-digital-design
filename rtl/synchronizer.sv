/* synchronizer devresi */

module synchronizer (
    input  logic clk, rst,
    input  logic btn,
    output logic q
);

logic s1, s2;

// btn girisinin sisteme async geldigini dusunursek
// bir vey iki kere flopladiktan sonra cok yukse ihtimalle
// stabillesecegini varsayabiliriz.

// burada iki kere floplanmis ornek gosteriliyor.
// ayni zamanda btn sinyali baska bir clk domainden de
// olusturulmus olabilirdi
always_ff @(posedge clk, negedge rst)
begin
    if (!rst) begin
        {q, s1, s2} <= 3'b0;
    end
    else begin
        s1 <= btn;
        s2 <= s1;
        q  <= s2;
    end
end

endmodule