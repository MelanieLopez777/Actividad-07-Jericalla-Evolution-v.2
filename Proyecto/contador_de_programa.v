//Equipo: Los Muñonez 

`timescale 1ns / 1ns

module contador_de_programa(
	input clk,
	input wire reset,
    input wire [6:0] cantidad_instrucciones,
	output reg [6:0] o_contador,
    output reg read_e_mem_instrucciones
);

reg [1:0] contador_pulsos;
reg [6:0] contador_programa;

always @(posedge clk) begin
	if(reset == 1'b1)
		begin
            read_e_mem_instrucciones = 1'b1;
            contador_pulsos = 1'b0;
			contador_programa = 1'b0;
		end
	else if(contador_pulsos < 2'd2)
		begin
            contador_pulsos = contador_pulsos + 1'b1;
		end
	else
		begin
            contador_pulsos = 1'b0;
            if(contador_programa < cantidad_instrucciones)
                begin
                    contador_programa = contador_programa + 1'b1;
                    o_contador = contador_programa;
                end
            else
                begin
                    contador_programa = 7'd0;
                    o_contador = contador_programa;
                    read_e_mem_instrucciones = 1'b0;
                end
        end
end

endmodule