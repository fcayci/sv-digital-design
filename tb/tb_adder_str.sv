/* tb_adder_str.sv
 */

`timescale 1ns/1ps

module tb_adder_str ();

    localparam N = 5;

    logic [N-1:0] a, b;
    logic cin;
    logic [N-1:0] s, sbek;
    logic cout, cbek;

    adder_str  #(N) dut0(a, b, cin, s, cout);

    initial
    begin
        for (int c=0; c<2; c++) begin
            cin = c;
            for (int i=0; i<2**N-1; i++) begin
                for (int j=0; j<2**N-1; j++) begin
                    a = i; b = j;
                    {cbek, sbek} = a + b + cin;
                    #10;
                    if ({cout, s} !== {cbek, sbek}) begin
                        $display("hata: a:%d, b:%d, cin:%d, s:%d, cout:%d", a, b, cin, s, cout);
                        $display("|-- beklenen: sbek:%d, cbek:%d", sbek, cbek);
                    end
                end
            end
        end
        $stop;
    end

endmodule
