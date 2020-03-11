beq x0, x0, label
bge x1, x0, label
label0:bge x2,x0,label
lui x1, 0xDEAD
auipc x4, 0x10
label:blt x0,x2 ,label0
jal x3 ,label
blt x0,x1 ,label0
bne x0, x1,label0 

