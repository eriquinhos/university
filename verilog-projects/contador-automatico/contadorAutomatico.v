module contadorAutomatico(clk, rst, display);
	input clk, rst;
	output[6:0] display;
	
	wire gremio;
    wire[3:0] inter;

    divisorFrequencia Taenia(.clk(clk), .s(gremio));
	
	contador solium(.clock(gremio), .reset(rst), .s(inter));
	
	decodificador saginata(.binary(inter), .segmentos(display));
endmodule
	

module divisorFrequencia(clk, s);
    input clk;
    output reg s;

    reg [25:0] out;
    
    always @ (posedge clk) begin
        if (out ==26'd50000000) begin
            out <= 26'd0;
            s <= 1;
        end

        else begin
            out<= out+1;
            s <= 0;
        end
    end
endmodule


module contador(clock, reset, s);
	input clock, reset;
	output reg[2:0] s;
	
	always@(posedge clock or posedge reset) begin
		if (reset) begin
            s<=3'b000;
        end

        else begin
            s = s+1;
        end
	end
endmodule


module decodificador(
    input[3:0] binary,
	output[6:0] segmentos
    );

	reg [6:0] seg_out;

	always @ (binary) begin
	
		case(binary)
		
			4'b0000: seg_out = 7'b0000001;
			4'b0001: seg_out = 7'b1001111;
			4'b0010: seg_out = 7'b0010010;
			4'b0011: seg_out = 7'b0000110;
			4'b0100: seg_out = 7'b1001100;
			4'b0101: seg_out = 7'b0100100;
			4'b0110: seg_out = 7'b0100000;
			4'b0111: seg_out = 7'b0001111;
			4'b1000: seg_out = 7'b0000000;
			4'b1001: seg_out = 7'b0000100;
			default: seg_out = 7'b1111111;
		
		endcase
	
	end

	assign segmentos = seg_out;
	
endmodule 
