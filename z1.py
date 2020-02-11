import os
f1=open("data.asm")
os.remove("coded.mc")
f2=open("coded.mc","x")
lines=f1.readlines()
for line in lines:
    string,rem=line.split()
    if (string=="addi" or string=="andi" or string=="ori"):
        k1,k2,k3=rem.split(",")
        h1=str(bin(int(k1[1],10))[2:].zfill(5))
        h2=str(bin(int(k2[1],10))[2:].zfill(5))
        if(int(k3)>0):
            if(k3.startswith("0x")):
                h3=str(bin(int(k3, 16))[2:].zfill(12))
            else:    
                h3=str(bin(int(k3,10))[2:].zfill(12)) 
        elif(int(k3)<0):
            if(k3.startswith("0x")):
                h3=str(bin(int(k3, 16))[3:].zfill(12))
            else:    
                h3=str(bin(int(k3,10))[3:].zfill(12)) 
            k3=int(h3,2)
            k3=2**12-k3; 
            k3=str(k3)    
            h3=str(bin(int(k3,10))[2:].zfill(12)) 
            print(h3)              
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
    elif (string=="sw" or string=="sb" or string=="sd" or string=="sh"):
        k1,k2=rem.split(",")
        k3,reg=k2.split("(")
        h1=str(bin(int(k1[1],10))[2:].zfill(5)) 
        h2= str(bin(int(reg[1],10))[2:].zfill(5)) 
        if(int(k3)>=0):
            if(k3.startswith("0x")):
                h3=str(bin(int(k3, 16))[2:].zfill(12))
            else:    
                h3=str(bin(int(k3,10))[2:].zfill(12)) 
        elif(int(k3)<0):
            if(k3.startswith("0x")):
                h3=str(bin(int(k3, 16))[3:].zfill(12))
            else:    
                h3=str(bin(int(k3,10))[3:].zfill(12)) 
            k3=int(h3,2)
            k3=2**12-k3 
            k3=str(k3)    
            h3=str(bin(int(k3,10))[2:].zfill(12)) 
        if(string=="sw"):
            func3="010"
                
        elif(string=="sd"):
            func3="011"
        elif(string=="sh"):
            func3="001"
        else: 
            func3="000"  
        opc="0100011"     
        mac_codet=h3[0:7]+h1+h2+func3+h3[7:]+opc
        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
        f2.write("0x"+mac_code+"\n")
 