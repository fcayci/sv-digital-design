/* her uc clockda bit tick olustur */

module fsm_tick (
    input  logic clk, reset,
    output logic tick
);

// logic [1:0] olarak tanimladigimiz icin statetype 2-bitlik bir logic
// komple kaldirip, anonymous (unnamed) integer type da yapabilirdik.
// Compiler/Synthesizer otomatik karar verecekti nasil kullanacagina.
typedef enum logic [1:0] {S0, S1, S2} statetype;

// anonymous (unnamed) integer data type
// typedef enum {S0, S1, S2} statetype;

// statelerin degerlerini girdik. Hepsi 3'er bit (implicit)
// typedef enum {S0= 'b001, S1= 'b010, S2= 'b100} statetype;

// statelerin degerlerini girdik. Hepsi 3'er bit (explicit)
// typedef enum {S0=3'b001, S1=3'b010, S2=3'b100} statetype;

// logic data type ve statelerin degerlerini girdik. Hepsi 3'er bit (explicit)
//typedef enum logic [2:0] {S0=3'b001, S1=3'b010, S2=3'b100} statetype;

// statelerin degerlerini 0 dan degil 2 den baslattik
// typedef enum {S0= 2, S1= 3, S2= 4} statetype;

// 3 state genere ettik. state adlari S0, S1, S2 olacak
// typedef enum {S[3]} statetype;

// iki tane degisken olusturup, default state degerlerini verdik
statetype state = S0, nextstate = S0;

always_ff @(posedge clk)
    if (reset) state <= S0;
    else       state <= nextstate;

// next state logic
always_comb
    case (state)
        S0:      nextstate = S1;
        S1:      nextstate = S2;
        S2:      nextstate = S0;
        default: nextstate = S0;
    endcase

// output logic
assign tick = (state == S2);

endmodule
