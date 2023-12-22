module statesMachine(clk, rst, cmd, out);
    input clk, rst;
    input [1:0] cmd;
    output [6:0] out;

    wire inter;
    wire [3:0] gremio;

    divisorfreq Ancylostoma(.CLK(clk), .S(inter));
    maquininha duodenale(.clock(inter), .reset(rst), .command(cmd), .saida(gremio));
    decodificador braziliense(.entrada(gremio), .saida(out));
endmodule

module maquininha(clock, reset, command, saida);
    //Sequência: 2-5-8-2-4-0-2-9-7
    input clock, reset;
    input [1:0] command;
    output reg [3:0] saida;
    reg [3:0] x, X;

    parameter A=4'b0000, B=4'b0001, C=4'b0010, D=4'b0011;
    parameter E=4'b0100, F=4'b0101, G=4'b0110, H=4'b0111, I=4'b1000, J=4'b1001;

    always@(command or x) begin
        case(x)
            A: if(command==2'b00) begin
                    X = A;
                end

                else if(command==2'b01) begin
                    X = I;
                end

                else if(command==2'b10) begin
                    X = B;
                end
                else if(command==2'b11) begin
                    X = J;
                end

            B: if(command==2'b00) begin
                    X = B;
                end

                else if(command==2'b01) begin
                    X = A;
                end

                else if(command==2'b10) begin
                    X = C;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            C: if(command==2'b00) begin
                    X = C;
                end

                else if(command==2'b01) begin
                    X = B;
                end

                else if(command==2'b10) begin
                    X = D;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            D: if(command==2'b00) begin
                    X = D;
                end

                else if(command==2'b01) begin
                    X = C;
                end

                else if(command==2'b10) begin
                    X = E;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            E: if(command==2'b00) begin
                    X = E;
                end

                else if(command==2'b01) begin
                    X = D;
                end

                else if(command==2'b10) begin
                    X = F;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            F: if(command==2'b00) begin
                    X = F;
                end

                else if(command==2'b01) begin
                    X = E;
                end

                else if(command==2'b10) begin
                    X = G;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            G: if(command==2'b00) begin
                    X = G;
                end

                else if(command==2'b01) begin
                    X = F;
                end

                else if(command==2'b10) begin
                    X = H;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            H: if(command==2'b00) begin
                    X = H;
                end

                else if(command==2'b01) begin
                    X = G;
                end

                else if(command==2'b10) begin
                    X = I;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            I: if(command==2'b00) begin
                    X = I;
                end

                else if(command==2'b01) begin
                    X = H;
                end

                else if(command==2'b10) begin
                    X = A;
                end
                else if(command==2'b11) begin
                    X = J;
                end
            J: if(command==2'b00) begin
                    X = J;
                end

                else if(command==2'b01) begin
                    X = A;
                end

                else if(command==2'b10) begin
                    X = A;
                end
                else if(command==2'b11) begin
                    X = J;
                end
        endcase
    end

    always@(posedge clock or posedge reset) begin
        if(reset==1) begin
          x<=A;
        end
        else begin
          x<=X;
        end
    end
    
    //Sequência: 2-5-8-2-4-0-2-9-7
    
    always@(*) begin
			if(x==A) begin
                saida<=4'b0010; //2
            end
            else if(x==B) begin
                saida<=4'b0101; //5
            end
            else if(x==C) begin
                saida<=4'b1000; //8
            end
            else if(x==D) begin
                saida<=4'b0010; //2
            end
            else if(x==E) begin
                saida<=4'b0100; //4
            end
            else if(x==F) begin
                saida<=4'b0000; //0
            end
            else if(x==G) begin
                saida<=4'b0010; //2
            end
            else if(x==H) begin
                saida<=4'b1001; //9
            end
            else if(x==I) begin
                saida<=4'b0111; //7
            end
            else if(x==J) begin
                saida<=4'b1111; //15
            end
    end
endmodule



module divisorfreq (CLK, S);
    input CLK;
    output reg S;
    reg [25:0] OUT;
    always @ (posedge CLK) begin
        if (OUT ==26'd50000000) begin
            OUT<= 26'd0;
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