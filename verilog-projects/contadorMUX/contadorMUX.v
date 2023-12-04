module contadorMUX(clk, sw, rst, display);
	input clk, rst;
   input  [1:0] sw;
	output[6:0] display;
	
	 wire gremio;
    wire[3:0] inter;

    MUX Enterobius(.clock(clk), .switch(sw), .s(gremio));

	contador vermicularis(.clock(gremio), .reset(rst), .s(inter));
	
	decodificador anthropopitheci(.binary(inter), .segmentos(display));
endmodule


module MUX (
    input clock,
    input [1:0] switch,
    output reg s
);

    reg [32:0] out;

    always @(posedge clock) begin
        case (switch)
            2'b00:
                if (out == 32'd25000000) begin
                    out <= 32'd0;
                    s <= 1;
                end else begin
                    out <= out + 1;
                    s <= 0;
                end
            2'b01:
                if (out == 32'd50000000) begin
                    out <= 32'd0;
                    s <= 1;
                end else begin
                    out <= out + 1;
                    s <= 0;
                end
            2'b10:
                if (out == 32'd100000000) begin
                    out <= 32'd0;
                    s <= 1;
                end else begin
                    out <= out + 1;
                    s <= 0;
                end
            2'b11:
                if (out == 32'd300000000) begin
                    out <= 32'd0;
                    s <= 1;
                end else begin
                    out <= out + 1;
                    s <= 0;
                end
            default:
                out <= 32'd0;
                s <= 1'b0;
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
