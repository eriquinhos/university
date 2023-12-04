module contadorFiltro(D, clk, rst, display);
	input D, clk, rst;
	output[6:0] display;
	
	wire gremio;
	wire[3:0] inter;
	
   filtroAssincrono Canis(.D(D), .clk_man(clk), .filtrado(gremio));
	
	contador lupus(.clock(gremio), .reset(rst), .s(inter));
	
	decodificador familiaris(.binary(inter), .segmentos(display));
endmodule
	

module filtroAssincrono(D, clk_man, filtrado);
	input D, clk;
	output reg filtrado;

	reg Q1;

	always @ (posedge clk) begin
		Q1 <= D;
		filtrado <= Q1;
	end
endmodule


module contador(clock, reset, s);
	input clock, reset;
	output reg[2:0] s;
	
	always@(posedge clock or posedge reset) begin
		case (reset)
			s <= 4'b0000;
		endcase
		case (clock)
			if (s > 4'b1001) begin
				s <= 4'b0000;
			end
			else begin
				s <= s+1;
			end
		endcase
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

	assign seg_out = segmentos;
	
endmodule 