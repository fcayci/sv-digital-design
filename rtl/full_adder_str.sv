/* full adder structural design */

module full_adder_str (
    input  logic a, b, cin,
    output logic s, cout
);

logic s0, c0, c1;

// half_adder devresini iki kere instantiate et
// o devrenin portlarini yazarak asagidaki gibi template olustur
//
// half_adder instname (.x( ), .y( ), .s( ), .c( ));
//
// sonra devre semasina bakarak baglantilari yap
// ismi olmayan baglantilar icin intermedate sinyal olustur s0, c0, c1 gibi

// bloklarin siralamasinin bir onemi yok
assign cout = c0 | c1;

half_adder ha0 (.x(a), .y(b), .s(s0), .c(c0));
half_adder ha1 (.x(s0), .y(cin), .s(s), .c(c1));

endmodule
