/* memory.sv
 *
 * iki portlu hafiza devresi ornegi
 * birinci port sadece yazmak icin,
 * ikinci port sadece okumak icin kullaniliyor
 */
module memory (
    input  logic clk, reset,
    input  logic we,
    input  logic [2:0] waddr, addr,
    input  logic [15:0] din,
    output logic [15:0] dout
);

// mem adında 16-bit uzunluğunda 8 elemanlı bir hafiza olustur.
// mem[0], mem[1], ... mem[7] olacak
// ve her biri 16 bit uzunlugunda olacak
logic [15:0] mem [0:7];

// baslangicta hafizayi reg_image dosyasindaki degerlerle doldur
// reg_image dosyasindaki degerleri hex olarak okuyacak
// binary icin readmemb
initial begin
    $readmemh("reg_image.mem", mem);
end

// write portu
// rising edge clk geldiğinde eger we biti aktif ise
// din i mem dizisinin waddr inci elemanına aktar.
// istersek initial vermeyip, sifirlayabiliriz
integer i;
always_ff @(posedge clk)
    if (!reset) for (i=0; i<8; i=i+1) mem[i] <= 16'b0;
    else if (we) mem[waddr] <= din;

// read portu combinational olarak kullan
// extra read portu buraya eklenebilir
assign dout = mem[addr];

endmodule
