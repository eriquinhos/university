module cronometroDigital(clock, startorstop, reset, uneseconde, dixsecondes, uneminute, dixminutes);
    input clock, startorstop, reset;
    output [6:0] uneseconde, dixsecondes, uneminute, dixminutes;

    wire onesec, tensec, onemin, tenmin;
    wire [3:0] umsegundo, dezsegundos, umminuto, dezminutos;

    oneSFreqDiv Drosophila(.CLK(clock), .S(onesec));
    tenSFreqDiv Taenia(.CLK(clock), .S(tensec));
    oneMFreqDiv Ancylostoma(.CLK(clock), .S(onemin));
    tenMFreqDiv Trypanosoma(.CLK(clock), .S(tenmin));

    stopwatch melanogaster(.clock(onesec), .startstop(startorstop), .reset(reset), .out(umsegundo));
    stopwatch solium(.clock(tensec), .startstop(startorstop), .reset(reset), .out(dezsegundos));
    stopwatch duodenale(.clock(onemin), .startstop(startorstop), .reset(reset), .out(umminuto));
    stopwatch cruzi(.clock(tenmin), .startstop(startorstop), .reset(reset), .out(dezminutos));

    decodificador bifurca(.entrada(umsegundo), .saida(uneseconde));
    decodificador saginata(.entrada(dezsegundos), .saida(dixsecondes));
    decodificador braziliense(.entrada(umminuto), .saida(uneminute));
    decodificador vivax(.entrada(dezminutos), .saida(dixminutes));
endmodule

module stopwatch(clock, startstop, reset, out);
    input clock, startstop, reset;
    output reg [3:0] out;
    reg [3:0] x, X;

    parameter A=4'b0000, B=4'b0001, C=4'b0010, D=4'b0011;
    parameter E=4'b0100, F=4'b0101, G=4'b0110, H=4'b0111, I=4'b1000, J=4'b1001;

    always@(startstop or x) begin
        case(x)
            A:  if(startstop==1'b0) begin
                    X = B;
                end
                else if(startstop==1'b1) begin
                    X = A;
                end

            B:  if(startstop==1'b0) begin
                    X = C;
                end
                else if(startstop==1'b1) begin
                    X = B;
                end

            C:  if(startstop==1'b0) begin
                    X = D;
                end
                else if(startstop==1'b1) begin
                    X = C;
                end
            
            D:  if(startstop==1'b0) begin
                    X = E;
                end
                else if(startstop==1'b1) begin
                    X = D;
                end
            
            E:  if(startstop==1'b0) begin
                    X = F;
                end
                else if(startstop==1'b1) begin
                    X = E;
                end

            F:  if(startstop==1'b0) begin
                    X = G;
                end
                else if(startstop==1'b1) begin
                    X = F;
                end
            
            G:  if(startstop==1'b0) begin
                    X = H;
                end
                else if(startstop==1'b1) begin
                    X = G;
                end
            
            H:  if(startstop==1'b0) begin
                    X = I;
                end
                else if(startstop==1'b1) begin
                    X = H;
                end
            
            I:  if(startstop==1'b0) begin
                    X = J;
                end
                else if(startstop==1'b1) begin
                    X = I;
                end
            
            J:  if(startstop==1'b0) begin
                    X = A;
                end
                else if(startstop==1'b1) begin
                    X = J;
                end
        endcase
    end

    always@(posedge clock or posedge reset) begin
        if(reset==1) begin
            x <= A;
        end
        else begin
            x <= X;
        end
    end

    always@(*) begin
        if(x == A) begin
            out = 4'b0000;
        end

        else if(x == B) begin
            out = 4'b0001;
        end

        else if(x == C) begin
            out = 4'b0010;
        end

        else if(x == D) begin
            out = 4'b0011;
        end

        else if(x == E) begin
            out = 4'b0100;
        end

        else if(x == F) begin
            out = 4'b0101;
        end

        else if(x == G) begin
            out = 4'b0110;
        end

        else if(x == H) begin
            out = 4'b0111;
        end

        else if(x == I) begin
            out = 4'b1000;
        end

        else if(x == J) begin
            out = 4'b1001;
        end
    end
endmodule



module oneSFreqDiv(CLK, S); // 1 segundo
    input CLK;
    output reg S;
    reg [35:0] OUT;
    always @ (posedge CLK) begin
        if (OUT ==36'd50000000) begin
            OUT<= 36'd0;
            S <= 1;
        end

        else begin
            OUT<= OUT+1;
            S <= 0;
        end
    end
endmodule


module tenSFreqDiv(CLK, S); // 10 segundos
    input CLK;
    output reg S;
    reg [35:0] OUT;
    always @ (posedge CLK) begin
        if (OUT == 36'd500000000) begin
            OUT<= 36'd0;
            S <= 1;
        end

        else begin
            OUT<= OUT+1;
            S <= 0;
        end
    end
endmodule


module oneMFreqDiv(CLK, S); // 1 minuto
    input CLK;
    output reg S;
    reg [35:0] OUT;
    always @ (posedge CLK) begin
        if (OUT ==36'd3000000000) begin
            OUT<= 36'd0;
            S <= 1;
        end

        else begin
            OUT<= OUT+1;
            S <= 0;
        end
    end
endmodule

module tenMFreqDiv(CLK, S); // 10 minutos
    input CLK;
    output reg S;
    reg [35:0] OUT;
    always @ (posedge CLK) begin
        if (OUT ==36'd30000000000) begin
            OUT<= 36'd0;
            S <= 1;
        end

        else begin
            OUT<= OUT+1;
            S <= 0;
        end
    end
endmodule



module decodificador(entrada, saida);
    input [3:0] entrada;
    output [6:0] saida;

    reg [6:0] segmentos;

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

/*
module decodMUX(clock, reset, HEX0, HEX1, HEX2, HEX3, enable_signal);
    input clock, reset;
    input HEX0, HEX1, HEX2, HEX3;
    output enable_signal;

    localparam N = 18;
    
    reg [N-1:0] contador;

    always @ (posedge clock or posedge reset) begin
        if (reset) begin
            contador <= 0;
        end

        else begin
            contador <= contador + 1;
        end
    end

    reg [6:0] sseg;
    reg [3:0] temp_enable_signal;

    always@(*) begin
        case (contador[N-1:N-2])
            2'b00: begin
                sseg = HEX0;
                temp_enable_signal = 4'b1110;
            end

            2'b01: begin
                sseg = HEX1;
                temp_enable_signal = 4'b1101;
            end

            2'b10: begin
                sseg = HEX2;
                temp_enable_signal = 4'b1011;
            end

            2'b11: begin
                sseg = HEX3;
                temp_enable_signal = 4'b0111;
            end
        endcase
    end

    assign enable_signal = temp_enable_signal;
endmodule
*/