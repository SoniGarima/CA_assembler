import os
f1=open("data.asm")
os.remove("coded.mc")
f2=open("coded.mc","x")
lines=f1.readlines()
for line in lines:
    string,rem=line.split()