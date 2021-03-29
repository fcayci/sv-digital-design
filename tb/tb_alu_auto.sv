/* tb_alu_auto.sv
 *
 * testvectorlerinden okuyup otomatik karsilastirma yapan testbench.
 */

`timescale 1ns/1ps

module tb_alu_auto ();

    localparam XLEN = 32; // ALU nun bit uzunlugu

    logic clk;
    logic [XLEN-1:0] a, b;
    logic [3:0] op;
    logic [XLEN-1:0] s, sexp;
    logic n, z, v, c, nexp, zexp, vexp, cexp;
    logic hata;

    // clk port olarak mevcut, fakat iceride bagli degil. (ALU comb. logicden olusuyor sadece)
    // XLEN ALU bit uzunlugu, sizin tasariminizda kullanmayabilirsiniz.
    alu2020 #(XLEN, 0, 0) dut0(
        .clk(clk), .a(a), .b(b), .op(op), .s(s), .n(n), .z(z), .v(v), .c(c), .hata(hata));

    // registersiz halini test ediyoruz, registerlari eklersek
    // sonuclar 1 clk cycle gecikecegi icin ona gore bir test olusturmak gerekir.
    // always begin
    //     clk = 1'b0; #5; clk = 1'b1; #5;
    // end

    initial
    begin
        // file descriptor
        int fd;
        static int flagerr = 0, serr = 0, ntest = 0;

        // test vector dosyasini ac. bu dosya ile ayni klasorde olacak. (videodaki gibi modelsim projeniz sim/ klasorunun altinda ise)
        // yoksa asagidan dogru yere yonlendirin
        fd = $fopen ("misc/alu2020_testvector.txt", "r");
        // eger acildiysa devam et
        if (fd) begin
            // sonuna kadar dosyayi oku
            while (!$feof(fd)) begin
                // her satiri tek tek oku. testvector asagida gosterilen siraya gore olusturulmustur. binary olarak.
                // hata cikisi bulunmamaktadir. (yani hatali bir op degeri yok, TODO: siz birkac hatali ekleyin testvectorlerinin sonuna)
                // 10 ns bekle ve devre sonuclari ile beklenen degerleri kontrol et
                $fscanf(fd, "%b,%b,%b,%b,%b,%b,%b,%b",a, b, op, sexp, nexp, zexp, vexp, cexp); #10;
                if (s !== sexp) begin
                    serr++; // sonuc hatalarini say
                    $display("s icin yanlis deger, op: %b, beklenen: %b, devre: %b", op, sexp, s);
                    $display("|--> a: %b, b: %b", a, b);
                end
                // carry bitini karsilastir.
                // TODO: geri kalan karsilastirmalari da eklemeniz gerekir. (nzv)
                if ({n, z, v, c} !== {nexp, zexp, vexp, cexp}) begin
                    flagerr++; // carry hatalarini say
                    $display("nzvc icin yanlis deger, op: %b, beklenen nzvc: %b,%b,%b,%b, devre: %b,%b,%b,%b", op, nexp, zexp, vexp, cexp, n, z, v, c);
                    $display("|--a: %b, b: %b, s: %b", a, b, s);
                end
                ntest++;
            end

            // yukarida kac hata varsa sayip, genel bir rapor sun
            $display("Simulasyon tamamlandi. %d farkli testte, toplamda %d sonuc hatasi, %d flag hatasi mevcut", ntest, serr, flagerr);
        end
        // acamazsa hata ver
        else
            $display("dosyayi acamadik");

        $fclose(fd);
        $stop;
    end

endmodule
