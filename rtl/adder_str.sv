/* n-bit adder tasarimi structural */

module adder_str #(parameter N = 8) (
    input  logic [N-1:0] a, b,
    input  logic cin,
    output logic [N-1:0] s,
    output logic cout
);

// intermetidate carry leri tutmak icin degisken tanimla
logic c[N:0];

// giris ve cikis carrylerini interemediate sinyale aktar
// generate te rahatolsun diye
assign c[0] = cin;
assign cout = c[N];

// asagidaki full_adder devresini N kere cagir
// baglantilari da verilen parametrelere gore bagla
// for generate blogu
genvar i;
generate
    for (i=0; i<N; i++) begin: fa
        full_adder fa0 (.a(a[i]), .b(b[i]), .cin(c[i]), .s(s[i]), .cout(c[i+1]));
    end
endgenerate

endmodule