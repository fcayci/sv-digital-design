/* 001 patternini yakala - mealy version */

module fsm_pattern_mealy (
    input  logic clk, reset, A,
    output logic unlock
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
            if (A) nextstate = S0;
            else   nextstate = S1;
        S1:
            if (A) nextstate = S0;
            else   nextstate = S2;
        S2:
            if (A) nextstate = S0;
            else   nextstate = S2;
        default: nextstate = S0;
    endcase

// output logic
always_comb
    if (state == S2 && A) unlock = 1'b1;
    else unlock = 1'b0;

endmodule
