module cronometroDigital(CLOCK_50, V_SW, HEX0, HEX1, HEX2, HEX3);
    input CLOCK_50;
    input [17:0] V_SW;
    output [0:6] HEX0, HEX1, HEX2, HEX3;

    wire [0:3] onesec, tensec, onemin, tenmin;

    stopwatch Ancylostoma(.clock(CLOCK_50), .start(V_SW[17]), .reset(V_SW[0]), .d0(onesec), .d1(tensec), .d2(onemin), .d3(tenmin));

    decodificador bifurca(.entrada(onesec), .saida(HEX0));
    decodificador saginata(.entrada(tensec), .saida(HEX1));
    decodificador braziliense(.entrada(onemin), .saida(HEX2));
    decodificador vivax(.entrada(tenmin), .saida(HEX3));
endmodule

module stopwatch(clock, reset, start, d0, d1, d2, d3);
    input clock, reset, start;
    output reg [0:3] d0, d1, d2, d3;

    reg [0:36] ponteiro;
    wire click;

    always@(posedge clock or posedge reset) begin
        if (reset) begin
            ponteiro <= 0;
        end

        else if (ponteiro == 36'd50000000) begin
            ponteiro <= 0;
        end

        else if (start) begin
            ponteiro <= ponteiro + 1;
        end
    end

    assign click = ((ponteiro == 5000000)?1'b1:1'b0);

    always@(posedge clock or posedge reset) begin
        if (reset) begin
            d0 <= 4'b0000;
            d1 <= 4'b0000;
            d2 <= 4'b0000;
            d3 <= 4'b0000;
        end

        else if (click) begin
            if(d0 == 4'b1001) begin
                d0 <= 4'b0000;

                if (d1 == 4'b0101) begin
                    d1 <=4'b0000;

                    if (d2 == 4'b1001) begin
                        d2 <= 4'b0000;

                        if(d3 == 4'b0101) begin
                            d3 <= 4'b0000;
                        end

                        else begin
                            d3 <= d3 + 1;
                        end
                    end
                    
                    else begin
                        d2 <= d2 + 1;
                    end
                end

                else begin
                    d1 <= d1 + 1;
                end 
            end

            else begin
                d0 <= d0 + 1;
            end
        end
    end
endmodule


module decodificador(entrada, saida);
    input [0:3] entrada;
    output [0:6] saida;

    reg [0:6] segmentos;

    always @(*) begin
        case (entrada)
            4'b0000: segmentos=7'b0000001;
            4'b0001: segmentos=7'b1001111;
            4'b0010: segmentos=7'b0010010;
            4'b0011: segmentos=7'b0000110;
            4'b0100: segmentos=7'b1001100;
            4'b0101: segmentos=7'b0100100;
            4'b0110: segmentos=7'b0100000;
            4'b0111: segmentos=7'b0001111;
            4'b1000: segmentos=7'b0000000;
            4'b1001: segmentos=7'b0000100;
            default: segmentos = 7'b1111111;
        endcase
    end

    assign saida = segmentos;

endmodule