beq x0, x0, label
bge x1, x0, label
label0:
lui x1, 0xDEAD
auipc x4, 0x10
jal x3 ,label
blt x0,x1 ,label0
bne x0, x1,label0 
label:
