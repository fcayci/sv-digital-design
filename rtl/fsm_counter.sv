/* counter ornegi - orta statede 4 clock bekle */

module fsm_counter (
    input  logic clk, reset, A,
    output logic unlock
);

typedef enum {S0, S1, S2} statetype;
statetype state, nextstate;

int count = 0, nextcount = 0;
// int count, nextcount;
// logic [2:0] count, nextcount;
// logic [2:0] count = 'b0, nextcount = 'b0;

always_ff @(posedge clk) begin
    if (reset) begin
        state <= S0;
        count <= 0;
    end
    else begin
        state <= nextstate;
        count <= nextcount;
    end
end

// next state logic
always_comb begin
    nextcount = count; // default deger
    case (state)
        S0:
            if (A) begin
                nextstate = S1;
                nextcount = 0; // counteri 0 la
            end
            else   nextstate = S0;
        S1:
            if (A && count == 4) nextstate = S2;
            else if (A) begin
                nextstate = S1;
                nextcount = count + 1'b1;
            end
            else nextstate = S0;
        S2: nextstate = S0;
        default: nextstate = S0;
    endcase
end

// output logic
always_comb
    if (state == S2) unlock = 1'b1;
    else unlock = 1'b0;

endmodule
