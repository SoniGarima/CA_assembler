import os
f1=open("data1.asm")
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
        if (string[0]=="beq" or string[0]=="bge" or string[0]=="blt" or string[0]=="bne"):
            k1,k2,k3=string[1].split(",")
            h1=str(bin(int(k1[1],10))[2:].zfill(5))
            h2=str(bin(int(k2[1],10))[2:].zfill(5))
            st=":"
            kd=k3+st
            count2=0
            for j in lines:
                string1=j.split()
                if(j!=" "):
                    count2=count2+1
                if(string1[0]==kd):
                    break
            if(count2>count1):
                count2=(count2-count1)-1
            else:
                count2=(count2-count1)+1
            print(count2)
            imm0=4*count2
            if(imm0>=0):
                imm=str(bin(imm0)[2:].zfill(12)) 
            else:  
                imm=str(bin(imm0)[3:].zfill(12)) 
                print(imm)
                imm0=int(imm,2)
                imm0=2**12-imm0
                imm0=str(imm0)    
                imm0=str(int(imm0,10)+1)
                imm=str(bin(int(imm0,10))[2:].zfill(12)) 
            imm1=imm[:7]
            imm2=imm[7:]
            if(string[0]=="beq"):
                func3="000"
            elif(string[0]=="bne"):
                func3="001"
            elif(string[0]=="blt"):
                func3="100"
            else:
                func3="101"
            opcode="1100011"
            mac_codet=imm1+h2+h1+func3+imm2+opcode
            mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
            print(mac_codet)
            f2.write("0x"+mac_code+"\n")
        






