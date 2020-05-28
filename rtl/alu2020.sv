module alu2020 #(parameter XLEN = 32, INPUT_REG = 1, OUTPUT_REG = 1) (
    input  logic clk,
    input  logic [XLEN-1:0] a, b,
    input  logic [3:0] op,
    output logic [XLEN-1:0] s,
    output logic n, z, v, c,
    output logic hata
);

logic [XLEN-1:0] areg, breg, res;
logic [XLEN:0] subreg;
logic nreg, vreg, creg, zreg, err;
logic [3:0] opreg;
logic [4:0] shamt;

// if generate blogu, giris ve cikislara opsyonel register atama
generate
if (INPUT_REG === 1)
begin
    always_ff @(posedge clk) begin
        areg <= a;
        breg <= b;
        opreg <= op;
    end
end
else begin
    assign areg = a;
    assign breg = b;
    assign opreg = op;
end
endgenerate

generate
if (OUTPUT_REG === 1)
begin
    always_ff @(posedge clk) begin
        s <= res;
        hata <= err;
        c <= creg;
        n <= nreg;
        z <= zreg;
        v <= vreg;
    end
end
else begin
    assign s = res;
    assign hata = err;
    assign c = creg;
    assign n = nreg;
    assign z = zreg;
    assign v = vreg;
end
endgenerate

// shift amount
logic [XLEN:0] lsl, lsr;
logic signed [XLEN:0] asr;

assign shamt = breg[4:0];
assign subreg = {1'b0, areg} - {1'b0, breg};

assign lsl = {1'b0, areg} << shamt;
assign lsr = {areg, 1'b0} >> shamt;
assign asr =  $signed({areg, 1'b0}) >>> shamt;

always_comb
begin
    // defaults, will be overwritten if necessary
    creg = 1'b0;
    err = 1'b0;
    if      (opreg == 4'b0000) {creg, res} = areg + breg;
    else if (opreg == 4'b1000) begin
        creg = ~subreg[XLEN];
        res = subreg[XLEN-1:0];
    end
    else if (opreg == 4'b0001) {creg, res} = lsl;
    else if (opreg == 4'b0011) if (areg > breg) res = 32'b1; else res = 32'b0;
    else if (opreg == 4'b0010) if ($signed(areg) > $signed(breg)) res = 32'b1; else res = 32'b0;
    else if (opreg == 4'b0100) res = areg ^ breg;
    else if (opreg == 4'b0101) {res, creg} = lsr;
    else if (opreg == 4'b1101) {res, creg} = asr;
    else if (opreg == 4'b0110) res = areg | breg;
    else if (opreg == 4'b0111) res = areg & breg;
    else begin
        res = 'b0;
        err = 1'b1;
    end
end

assign zreg = (res === 0);
assign nreg = res[XLEN-1];
assign vreg = (res[XLEN-1] != areg[XLEN-1]) && (
    ((opreg == 4'b0000) && (areg[XLEN-1] == breg[XLEN-1])) ||
    ((opreg == 4'b1000) && (areg[XLEN-1] != breg[XLEN-1])) );

endmodule
