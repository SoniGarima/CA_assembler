import os
f1=open("data.asm")
os.remove("coded.mc")
f2=open("coded.mc","x")
lines=f1.readlines()
for line in lines:
    string,rem=line.split();
    if string=="addi" or "andi" or "ori":
        k1,k2,k3=rem.split(",")
        h1=str(bin(int(k1[1],10))[2:].zfill(5))
        h2=str(bin(int(k2[1],10))[2:].zfill(5))
        if(k3.startswith("0x")):
            h3=str(bin(int(k3, 16))[2:].zfill(12))
        else:    
            h3=str(bin(int(k3,10))[2:].zfill(12))
        if(string=="addi"):
            func3="000"
        elif( string=="andi"):
            func3="111"
        else:
            func3="110" 
        opc="0010011"      
        mac_codet=h3+h2+func3+h1+opc
        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
        f2.write("0x"+mac_code+"\n")
        

 