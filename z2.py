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
        line=line.replace("\n","")
        if (line.__contains__("beq") or line.__contains__("bge") or line.__contains__("blt") or line.__contains__("bne")):
            if "beq" in line:
                sa1="beq"
            elif "bge" in line:
                sa1="bge"
            elif "blt" in line:
                sa1="blt"
            else:
                sa1="bne"
            string=line.split(sa1)
            string=string[1]
            k1,k2,k3=string.split(",")
            h1=str(bin(int(k1[1],10))[2:].zfill(5))
            h2=str(bin(int(k2[1],10))[2:].zfill(5))
            count2=0
            for j in lines:
                string1=j.split()
                if(j!=" "):
                    if(j.endswith(':')):
                        if k3 not in j:
                            continue
                    else:
                        count2=count2+1
                if(string1[0].__contains__(":")):
                    string2=string1[0].split(":")
                    if(string2[0]==k3):
                        break
            count4=0
            count3=0
            if(count2<count1):
                for t in lines:
                    if(t!=" "):
                        count3=count3+1
                        if(count3>=count2):
                            if(t.__contains__(":")):
                                string4=t.split(":")
                                if(string4[0]!=k3 and string4[1]=="\n"):
                                    count4=count4+1
                                if(string4[0]==k3 and string4[1]=="\n"):
                                    count4=count4+1
                    if(count3==count1):
                        countx=count1-count4
                        count2=count2-countx
                        break
            else:
                for t in lines:
                    if(t!=" "):
                        count3=count3+1
                        if(count3>count1):
                            if(t.__contains__(":")):
                                string4=t.split(":")
                                if(string4[0]!=k3 and string4[1]=="\n"):
                                    count4=count4+1
                    if(count3==count2):
                        countx=count2-count4
                        count2=countx-count1
                        break
          
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
            if(line.__contains__("beq")):
                func3="000"
            elif(line.__contains__("bne")):
                func3="001"
            elif "blt" in line:
                func3="100"
            else:
                func3="101"
            opcode="1100011"
            mac_codet=imm1+h2+h1+func3+imm2+opcode
            mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
            f2.write("0x"+mac_code+"\n")
        elif(line.__contains__("lui") or line.__contains__("auipc")):
            if(line.__contains__("lui")):
                string=line.split("lui")
                string=string[1]
                k1,k2=string.split(",")
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
                string=line.split("auipc")
                string=string[1]
               
                k1,k2=string.split(",")
                h1=str(bin(int(k1[1],10))[2:].zfill(5))
                opcode="0010111"
                if(k2.startswith("0x")):
                    x2=k2[2:]
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
                elif(k2.startswith("0b")):
                    x2=k2[2:]
                    h1=(hex(int(x2,2))[2:]).zfill(5)
                    ro=(hex(int(rd+opcode,2))[2:]).zfill(3)
                    mac_code=h1+ro
                else:
                    h2=str(bin(int(k2,10))[2:].zfill(20)) 
                    mac_codet=h2+h1+opcode
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
            f2.write("0x"+mac_code+"\n")
        elif(line.__contains__("jal")):
            string=line.split("jal")
            string=string[1]
            k1,k2=string.split(",")
            h1=str(bin(int(k1[1],10))[2:].zfill(5))
            count2=0
            for l in lines:
                string1=l.split()
                if(l!=" "):
                    if(l.endswith(":")):
                        if k3 not in l:
                            continue
                    else:
                        count2=count2+1
                if(string1[0].__contains__(":")):
                    string2=string1[0].split(":")
                    if(string2[0]==k2):
                        break
            count4=0
            count3=0
            if(count2<count1):
                for t in lines:
                    if(t!=" "):
                        count3=count3+1
                        if(count3>=count2):
                            if(t.__contains__(":")):
                                string4=t.split(":")
                                if(string4[0]!=k2 and string4[1]=="\n"):
                                    count4=count4+1
                                if(string4[0]==k2 and string4[1]=="\n"):
                                    count4=count4+1
                    if(count3==count1):
                        countx=count1-count4
                        count2=count2-countx
                        break
            else:
                for t in lines:
                    if(t!=" "):
                        count3=count3+1
                        if(count3>count1):
                            if(t.__contains__(":")):
                                string4=t.split(":")
                                if(string4[0]!=k2 and string4[1]=="\n"):
                                    count4=count4+1
                    if(count3==count2):
                        countx=count2-count4
                        count2=countx-count1
                        break
            
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
            

