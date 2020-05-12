/* birlestirilmis counter ornegi - orta statede 4 clock bekle
 * unlock_reg sinyali, registera bagli oldugu icin 1 clock cycle gecikmeli cikacaktir
 * unlock sinyali digeri ile ayni cikacaktir
*/

module fsm_counter_combined (
    input  logic clk, reset, A,
    output logic unlock_reg, unlock
);

typedef enum {S0, S1, S2} statetype;
statetype state;

int count = 0;

// tek bir always blogunda next-state logic, registers, ve output logikler mevcut
// output logic yanliz registera baglanacak en son, o yuzden bir clock cycle gecikme yasayacaktir.
always_ff @(posedge clk) begin
    if (reset) begin
        state <= S0;
        count <= 0;
        unlock_reg <= 1'b0;
    end
    else begin
        unlock_reg <= 1'b0; // default olarak
        case (state)
            S0:
                if (A) begin
                    state <= S1;
                    count <= 0; // counteri 0 la
                end
                else   state <= S0;
            S1:
                if (A && count == 4) state <= S2;
                else if (A) begin
                    state <= S1;
                    count <= count + 1'b1;
                end
                else state <= S0;
            S2: begin
                unlock_reg <= 1'b1; // degeri 1 ile guncelle
                state <= S0;
            end
            default: state <= S0;
        endcase
    end
end

// unlock sinyali icin output logic
always_comb
    if (state == S2) unlock = 1'b1;
    else unlock = 1'b0;

endmodule
