//Equipo: Los Muñonez

module memoria_de_instrucciones(
    input wire read_enable,
    input [6:0] address,
    output reg [18:0] o_data
);

reg [18:0] mem [0:99];

always @* begin
    if (read_enable == 1'b1)
    begin
		o_data = mem[address];
	end
    else
    begin
        o_data = 19'dz;
    end
end

endmodule