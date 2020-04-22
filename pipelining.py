import os
f1=open("coded.mc")
lines=f1.readlines()
pc_dict={}
for line in lines:
    [a1,a2]=line.split()
    pc_dict[int(a1,16)]=a2
from registers import registers
from memory import memory
my_mem=memory()
my_reg=registers()
from my_memory import mem_from_data
for key in mem_from_data:
    my_mem.write_byte(key,int(mem_from_data[key],2))
print(pc_dict)    
from Run import run
class pipelining:
    Cycles = 0
    sess = run()
    IF = 0;
    ID = -1;
    IE = -2;
    IM = -3;
    IRG = -4;
    while(sess.PC in pc_dict):
        if(IF >=0):
            sess.fetch(pc_dict[IF]);
            
            
    
