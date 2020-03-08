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
        line=line.replace(" ","")
        if (line.startswith("beq") or line.startswith("bge") or line.startswith("blt") or line.startswith("bne")):
            string=line[:3]+" "+line[3:]
            len1=len(string)
            string=string[:(len1-1)]
            string=string.split(" ")
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
                if(string1[0].startswith(kd)):
                    break
            if(count2>count1):
                count2=(count2-count1)-1
            else:
                count3=0
                count4=0
                for k in lines:
                    string1=k.split()
                    if(k!=" "):
                        count3=count3+1
                    if(count3>(count2-1) and count3<count1):
                        if(k.endswith(":") and string1[0]!=kd):
                            continue
                        else:
                            count4=count4+1
                count2=(-1*count4)+1
            imm0=4*count2
            if(imm0>=0):
                imm=str(bin(imm0)[2:].zfill(12)) 
            else:  
                imm=str(bin(imm0)[3:].zfill(12)) 
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
            f2.write("0x"+mac_code+"\n")
        elif(line.startswith("lui") or line.startswith("auipc")):
            if(line.startswith("lui")):
                string=line[:3]+" "+line[3:]
                len1=len(string)
                string=string[:(len1-1)]
                string=string.split(" ")

                k1,k2=string[1].split(",")
                h1=str(bin(int(k1[1],10))[2:].zfill(5))
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
                string=line[:5]+" "+line[5:]
                len1=len(string)
                string=string[:(len1-1)]
                string=string.split(" ")
                k1,k2=string[1].split(",")
                h1=str(bin(int(k1[1],10))[2:].zfill(5))
                opcode="0010111"
                if(k2.startswith("0x")):
                    h2=str(bin(int(k2, 16))[2:].zfill(20))
                else:
                    h2=str(bin(int(k2,10))[2:].zfill(20)) 
                mac_codet=h2+h1+opcode
                mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
            f2.write("0x"+mac_code+"\n")
        elif(line.startswith("jal")):
            string=line[:3]+" "+line[3:]
            len1=len(string)
            string=string[:(len1-1)]
            string=string.split(" ")
            k1,k2=string[1].split(",")
            h1=str(bin(int(k1[1],10))[2:].zfill(5))
            st=":"
            kd=k2+st
            count2=0
            for l in lines:
                string1=l.split()
                if(l!=" "):
                    count2=count2+1
                if(string1[0]==kd):
                    count2=count2+1
                    break
            if(count2<count1):
                count3=0
                count4=0
                for m in lines:
                    string1=m.split()
                    if(j!=" "):
                        count3=count3+1
                    if(count3>(count2-1) and count3<count1):
                        if(m.endswith(":") and string1[0]!=kd):
                            continue
                        else:
                            count4=count4+1
                count2=(-1*count4)+1
            else:
                count2=(count2-count1)-1
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
            
