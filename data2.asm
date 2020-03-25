.data
n: .word 3

.text
auipc x10 65536
lw x10 0(x10)
jal x1, factorial
addi x8, x0,1000
beq x0, x0, EXIT

factorial:
addi x2, x2, -8				
sw x1, 4(x2)				
sw x10, 0(x2)				
addi x5, x10, -1			
bge x5, x0, loop		
addi x10, x0, 1				
addi x2, x2, 8		
jalr x0, 0(x1)				

loop:
addi x10, x10, -1	
jal x1 factorial
addi x6, x10, 0
lw x10, 0(x2)			
lw x1, 4(x2)		
mul x10, x10, x6	
addi x2, x2, 8			
jalr x0, 0(x1)			

EXIT:
