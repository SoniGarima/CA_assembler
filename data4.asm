.data
arr: .word 23 45 12 4 51
n: .word 5
arr2: .word  3 3 3 3 3

.text
auipc x10, 65536
addi x10,x10,0
auipc x11,65536
lw x11,12(x11)
auipc x12,65536
addi x12,x12,8
jal x1, bubble
beq x0, x0, exit

bubble:
add x3, x0, x0

loop:
beq x3, x11, copied
addi x31,x0,2
sll x4, x3, x31
add x5, x4, x12
add x4, x4, x10
lw x4, 0(x4)
sw x4, 0(x5)
addi x3, x3, 1
beq x0, x0, loop

copied:
addi x2, x2, -4
sw x1, 0(x2)
jal x1, bubblesort
lw x1, 0(x2)
addi x2, x2, 4
jalr x0, 0(x1)

bubblesort:
addi x2, x2, -8
sw x1, 0(x2)
sw x11, 4(x2)

bne x11, x0, notbase
addi x2, x2, 8
jalr x0, 0(x1)

notbase:
add x6, x0, x11
addi x6, x6, -1
add x7, x0, x0

mainloop:
bge x7, x6, endloop
addi x8, x7, 0
sll x8, x8, x31
add x8, x8, x12
lw x13, 0(x8)
addi x9, x7, 1
sll x9, x9, x31
add x9, x9, x12
lw x14, 0(x9)
blt x13, x14, dontswap
sw x13, 0(x9)
sw x14, 0(x8)
dontswap:
addi x7, x7, 1
beq x0, x0, mainloop

endloop:
addi x11, x11, -1
jal x1, bubblesort
lw x1, 0(x2)
lw x11, 4(x2)
addi x2, x2, 8
jalr x0, 0(x1)
exit: