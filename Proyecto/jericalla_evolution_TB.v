//Equipo: Los Muñonez

`timescale 1ns/1ns

module jericalla_evolution_TB();

reg clk_TB;
reg [6:0] instruction_amount_TB;
reg reset_TB;

wire [31:0] data_out_TB;
wire zf_TB;

jericalla_evolucion jericalla_inst
(
    .clk(clk_TB),
	.reset(reset_TB),
    .cantidad_instrucciones(instruction_amount_TB),
	.data_out(data_out_TB),
    .zf(zf_TB)
);

initial begin
    clk_TB = 0; 
    forever #10 clk_TB = ~clk_TB;  
end

initial begin
     $readmemb("./Proyecto/datos.txt",jericalla_inst.banco_de_registros_inst.mem);
	 $readmemb("./Proyecto/instrucciones.txt",jericalla_inst.memoria_de_instrucciones_inst.mem);
end

initial begin
	
end

 initial begin
	reset_TB = 1'b1;
	#40;
	reset_TB = 1'b0;
	instruction_amount_TB = 7'd18;
	#1500;
	$stop;
 end
 
 endmodule