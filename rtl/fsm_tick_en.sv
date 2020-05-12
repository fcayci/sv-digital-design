/* A girisi varken her uc clockda bit tick olustur, yokken resetle */

module fsm_tick_en (
    input  logic clk, reset,
    input  logic A,
    output logic tick
);

typedef enum {S0, S1, S2} statetype;
statetype state, nextstate;

always_ff @(posedge clk)
    if (reset) state <= S0;
    else       state <= nextstate;

// next state logic
always_comb
    case (state)
        S0:
        begin
           if (A) nextstate = S1;
           else nextstate = S0;
        end
        S1:
        begin
           if (A) nextstate = S2;
           else nextstate = S0;
        end
        S2:      nextstate = S0;
        default: nextstate = S0;
    endcase

// output logic
assign tick = (state == S2);

endmodule
