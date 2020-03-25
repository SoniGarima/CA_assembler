.data
f1: .word 1
f2: .word 2
n: .word 6
arr: .word -1

.text
auipc x5,65536
addi x5,x5,12
auipc x6,65536
lw x6,0(x6)
jal x1, fibonacci
beq x0, x0, exit

fast:

fibonacci:
addi x4, x0, 1
bne x4, x6, notone
auipc x10,65536
lw x10,-32(x10)
sw x10, 0(x5)
jalr x0, 0(x1)

notone:
addi x4, x0, 2
bne x4, x6, nottwo
auipc x10,65536
lw x10,-56(x10)
sw x10, 0(x5)
auipc x10,65536
lw x10,-64(x10)
sw x10, 4(x5)
jalr x0, 0(x1)

nottwo:
addi x2, x2, -8
sw x1, 0(x2)
sw x9, 4(x2)
addi x6, x6, -1
jal x1, fibonacci
add x9, x0, x10
addi x6, x6, -1
jal x1, fibonacci
add x10, x10, x9
addi x6, x6, 2
add x9, x6, x0
addi x31,x0,2
sll x9, x9, x31
add x9, x9, x5
addi x9, x9, -4
sw x10, 0(x9)
lw x1, 0(x2)
lw x9, 4(x2)
addi x2, x2, 8
jalr x0, 0(x1)

exit:





