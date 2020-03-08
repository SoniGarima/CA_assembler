import os
f1=open("data4.asm")
os.remove("coded.mc")
f2=open("coded.mc","x")
lines=f1.readlines()
count1=0
for line in lines:
    if(line==" "):
        continue
    elif(line!=" "):
        count1=count1+1
        string=line.split()
        if(string[0]=="jal"):
            k1,k2=string[1].split(",")
            h1=str(bin(int(k1[1],10))[2:].zfill(5))
            st=":"
            kd=k2+st
            count2=0
            for j in lines:
                string1=j.split()
                if(j!=" "):
                    count2=count2+1
                if(string1[0]==kd):
                    count2=count2+1
                    break
            if(count2>count1):
                count2=(count2-count1)-1
            else:
                count2=(count2-count1)
            print(count2)
            imm0=4*count2
            if(imm0>=0):
                imm=str(bin(imm0)[2:].zfill(20)) 
            else:  
                imm=str(bin(imm0)[3:].zfill(20)) 
                imm0=int(imm,2)
                imm0=2**20-imm0
                imm0=str(imm0)    
                imm0=str(int(imm0,10)+1)
                imm=str(bin(int(imm0,10))[2:].zfill(20)) 
            imm=imm[0]+imm[9:]+imm[9]+imm[2:9]
            opcode="1101111"
            mac_codet=imm+h1+opcode
            mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
            f2.write("0x"+mac_code+"\n")
            
