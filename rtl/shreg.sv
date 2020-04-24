/* farkli shift register tasarimlari */

module shreg (
    input  logic       clk,
    input  logic       sin,
    input  logic       load,
    input  logic [7:0] load_value,
    output logic [4:0] sout,
    output logic [7:0] q1, q2, q3, q4, q5
);

// asagidaki butun yontemler -load versiyonu haric-
// ayni devreyi sentezleyecek ve ayni sonucu verecektir.


// birinci yontem, butun cikislari clk
// geldigi zaman bir sonraki girise aktar
// parametre kullanarak yapilamaz
assign sout[0] = q1[7];

always_ff @(posedge clk)
begin
    q1[7] <= q1[6];
    q1[6] <= q1[5];
    q1[5] <= q1[4];
    q1[4] <= q1[3];
    q1[3] <= q1[2];
    q1[2] <= q1[1];
    q1[1] <= q1[0];
    q1[0] <= sin;
end

// ikinci yontem, butun cikislari clk
// geldigi zaman bir sonraki girise aktar
// fakat parametre kullanabilmek icin for loop kullan
//    i.e. 7 ler yerine devre parametresi N yazilabilir
assign sout[1] = q2[7];

always_ff @(posedge clk)
begin
    q2[0] <= sin;
    for (int i=0; i<7; i++)
        q2[i+1] <= q2[i];
end


// ucuncu yontem, >> veta << operatorunu kullanarak
// hangi tarafa gittigi sout pininden MSB veya LSB first
// olarak cikmasini degistirecektir
// assign ve always_ff bloklarinin sirasinin onemi yok.
//   hatta bu koddaki butun bloklarin sirasinin bir onemi yok.
always_ff @(posedge clk)
begin
    q3 <= q3 << 1;
    q3[0] <= sin;
end

assign sout[2] = q3[7];


// dorduncu yontem, bitlerin baglantilariyla
// oynayip oyle atama yaparak.
always_ff @(posedge clk)
    q4 <= {q4[6:0], sin};

assign sout[3] = q4[7];


// parallel load sinyali ile yukleme yapmak
// oynayip oyle atama yaparak.
always_ff @(posedge clk)
begin
    if (load) q5 <= load_value;
    else      q5 <= {q5[6:0], sin};
end

assign sout[4] = q5[7];

endmodule
