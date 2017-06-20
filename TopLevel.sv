module TopLevel (
	input clk,    // Clock
	input reset,  // Asynchronous reset active low

	input 	[15:0] GPI,
	output 	[15:0] GPO,
	input 	ready 
	
);

always_ff @(posedge clk or negedge reset) begin : 
	if(~reset) begin
		GPO <= 16'h000f;
	end else begin
		if (ready)
			GPO <= GPO << 1;
	end
end
endmodule