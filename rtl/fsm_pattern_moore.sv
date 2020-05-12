/* 001 patternini yakala - moore version */

module fsm_pattern_moore (
    input  logic clk, reset, A,
    output logic unlock
);

typedef enum {S0, S1, S2, S3} statetype;
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
            if (A) nextstate = S3;
            else   nextstate = S2;
        S3:
            if (A) nextstate = S0;
            else   nextstate = S1;
        default: nextstate = S0;
    endcase

// output logic
assign unlock = (state == S3);

endmodule
