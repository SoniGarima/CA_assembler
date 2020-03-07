import os
f1=open("data3.asm")
os.remove("coded.mc")
f2=open("coded.mc","x")
lines=f1.readlines()
for line in lines:
    if(line==" "):
        continue
    elif(line!=" "):
        string=line.split()
        if(string[0]=="lui" or string[0]=="auipc"):
            k1,k2=string[1].split(",")
            h1=str(bin(int(k1[1],10))[2:].zfill(5))
            if(string[0]=="lui"):
                opcode="0110111"
                if(k2.startswith("0x")):
                    x2=k2[2:]
                    x2=x2.lower()
                    length=len(x2)
                    string1=""
                    if(length<5):
                        a=5-length
                        for i in range(a):
                            string1=string1+"0"
                    h2=string1+x2
                    mac_codet=h1+opcode
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(3))
                    mac_code=h2+mac_code
                else:
                    h2=str(bin(int(k2,10))[2:].zfill(20))
                    mac_codet=h2+h1+opcode
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
            else:
                opcode="0010111"
                if(k2.startswith("0x")):
                    h2=str(bin(int(k2, 16))[2:].zfill(20))
                else:
                    h2=str(bin(int(k2,10))[2:].zfill(20)) 
                mac_codet=h2+h1+opcode
                mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
            f2.write("0x"+mac_code+"\n")
            
                
