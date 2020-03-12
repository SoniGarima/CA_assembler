import os
from memory import memory
f1=open("data.asm","r")
os.remove("coded.mc")
f2=open("coded.mc","x")
os.remove("my_memory.py")
f3=open("my_memory.py","x")
lines=f1.readlines()
mem=memory()
output=[]
#Firstly, checking where is data declared!
if(lines.__contains__(".data\n")):
    k =lines.index(".data\n")
else:
    k=-1        
if(lines.__contains__(".text\n")):
    m =lines.index(".text\n")    
else:
    m=-1
    
case=0
if(m<0 and k<0):
    case=0
elif(m>=0 and k<0):
    case=1
elif(m<0 and k>=0):
    case=2
else:
    case=3            
k=k+1
labels_vars={}
data_parts=[]
data_address=0x10000000
while(k<len(lines) and(case==2 or case==3)):
    print(k)
    if(lines[k]==".text\n"):
        break
    else:
        if(lines[k].find(":")>0):
            colon=lines[k].find(":")
            labels_vars[lines[k][0:colon]]=data_address
            t1=(lines[k]).find(".byte")
            t2=(lines[k]).find(".word")
            t3=(lines[k]).find(".dword")
            t4=(lines[k]).find(".asciiz")
            t5=(lines[k]).find(".half")
            if(t1>=0):
                num_list=(lines[k][t1+5:].strip()).split()
                for num in num_list:
                    mem.write_byte(data_address,num)
                    data_address+=1 
            elif(t2>=0):
                num_list=(lines[k][t2+5:].strip()).split()
                for num in num_list:
                    mem.write_word(data_address,num)
                    data_address+=4
            elif(t3>=0):
                num_list=(lines[k][t3+6:].strip()).split()
                for num in num_list:
                    mem.write_db(data_address,num)
                    data_address+=8
            elif(t5>=0):
                num_list=(lines[k][t5+5:].strip()).split()
                for num in num_list:
                    mem.write_half(data_address,num)
                    data_address+=2
            else:
                my_str_list=(lines[k][t4+7:].strip())  
                for c in my_str_list[1:len(my_str_list)-1]:
                    mem.write_asciiz(data_address,c)
                    data_address+=1  
            # lines[k]=lines[k].replace(" ","")
            # lines[k]=lines[k].replace("\n","")        
            data_parts.append(lines[k])                                                   
    k=k+1   
print(mem.ret_byte(0x10000000))
f3.write("mem_from_data=")       
f3.write("{\n")
for i in range(0x10000000,data_address):
    print((i))
    print(mem.ret_byte((i)))
    f3.write(str(hex(i))+":"+"\""+(mem.ret_byte((i)))+"\""+",\n")
f3.write("}")   

##### MAIN PART #####################
pc=0x0
count1=0
for line in lines:
    if(line==" "):
        continue
    elif(line!=" "):
        count1=count1+1
        # line=line.replace(" ","")
        # line=line.replace("\n","")
        if(line.__contains__(".data") or line.__contains__(".text")):
            continue
        elif(line in data_parts):
            continue
        #ek case empty label ka bhi lagega, laga do yar koi!
        else:
            f2.write(str(hex(pc))+"  ")
            print(line)
            if(line.__contains__("add ") or line.__contains__("sub") or line.__contains__("mul") or line.__contains__("div") or line.__contains__("sra") or line.__contains__("rem") or line.__contains__("or ") or line.__contains__("srl") or line.__contains__("xor") or line.__contains__("and ") or line.__contains__("sll") or line.__contains__("slt")):
                if(line.__contains__("add ")):
                    h=line.find("add ")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="000"
                    fun7="0000000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("sub")):
                    h=line.find("sub")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="000"
                    fun7="0100000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("sra")):
                    h=line.find("sra")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="101"
                    fun7="0100000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("div")):
                    h=line.find("div")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="100"
                    fun7="0000001"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("mul")):
                    h=line.find("mul")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="000"
                    fun7="0000001"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("rem")):
                    h=line.find("rem")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="110"
                    fun7="0000001"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("or ")):
                    h=line.find("or ")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="110"
                    fun7="0000000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("srl")):
                    h=line.find("srl")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="101"
                    fun7="0000000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("xor")):
                    h=line.find("xor")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="100"
                    fun7="0000000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("and ")):
                    h=line.find("and ")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="111"
                    fun7="0000000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("sll")):
                    h=line.find("sll")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="001"
                    fun7="0000000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                if(line.__contains__("slt")):
                    h=line.find("slt")
                    [k1,k2,k3]=line[h+3:].strip().split()
                    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
                    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
                    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
                    opc="0110011"
                    fun3="010"
                    fun7="0000000"
                    mac_codet=fun7+h1+h2+fun3+h3+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
            elif(line.__contains__("addi") or line.__contains__("andi") or line.__contains__("ori")):
                if(line.__contains__("addi")):
                    func3="000"
                    h=line.find("addi")
                    h=h+4
                elif(line.__contains__("andi")):
                    func3="111"
                    h=line.find("andi")
                    h=h+4
                else:
                    func3="110" 
                    h=line.find("ori")  
                    h=h+3   
                [k1,k2,k3]=line[h:].strip().split(",")
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
                opc="0010011"      
                mac_codet=h3+h2+func3+h1+opc
                mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                f2.write("0x"+mac_code+"\n")    
            
            elif(line.__contains__("sb") or line.__contains__("sh") or line.__contains__("sd") or line.__contains__("sw")):
                if(line.__contains__("sb")):
                    y=line.find("sb")
                    y1=line.find("(")
                    y2=line.find(")")
                    j1=line[y+2:y1]
                    if(line.find(",")>=0):
                        [k1,k3]=j1.split(",")
                        k1=k1.strip()
                        k3=k3.strip()
                    else:
                        [k1,k3]=j1.split()
                        k1=k1.strip()
                        k3=k3.strip()    
                    k2=line[y1+1:y2].strip()
                    h1=str(bin(int(k1[1],10))[2:].zfill(5)) 
                    h2= str(bin(int(k2[1],10))[2:].zfill(5)) 
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
                    func3="000"
                    opc="0100011"
                    mac_codet=h3[0:7]+h1+h2+func3+h3[7:]+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n") 
                
                if(line.__contains__("sw")):
                    y=line.find("sw")
                    y1=line.find("(")
                    y2=line.find(")")
                    j1=line[y+2:y1]
                    if(line.find(",")>=0):
                        [k1,k3]=j1.split(",")
                        k1=k1.strip()
                        k3=k3.strip()
                    else:
                        [k1,k3]=j1.split()
                        k1=k1.strip()
                        k3=k3.strip()    
                    k2=line[y1+1:y2].strip()
                    h1=str(bin(int(k1[1],10))[2:].zfill(5)) 
                    h2= str(bin(int(k2[1],10))[2:].zfill(5)) 
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
                    func3="010"
                    opc="0100011"
                    mac_codet=h3[0:7]+h1+h2+func3+h3[7:]+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")     
                
                if(line.__contains__("sd")):
                    y=line.find("sd")
                    y1=line.find("(")
                    y2=line.find(")")
                    j1=line[y+2:y1]
                    if(line.find(",")>=0):
                        [k1,k3]=j1.split(",")
                        k1=k1.strip()
                        k3=k3.strip()
                    else:
                        [k1,k3]=j1.split()
                        k1=k1.strip()
                        k3=k3.strip()    
                    k2=line[y1+1:y2].strip()
                    h1=str(bin(int(k1[1],10))[2:].zfill(5)) 
                    h2= str(bin(int(k2[1],10))[2:].zfill(5)) 
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
                    func3="011"
                    opc="0100011"
                    mac_codet=h3[0:7]+h1+h2+func3+h3[7:]+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")     
                
                if(line.__contains__("sh")):
                    y=line.find("sh")
                    y1=line.find("(")
                    y2=line.find(")")
                    j1=line[y+2:y1]
                    if(line.find(",")>=0):
                        [k1,k3]=j1.split(",")
                        k1=k1.strip()
                        k3=k3.strip()
                    else:
                        [k1,k3]=j1.split()
                        k1=k1.strip()
                        k3=k3.strip()    
                    k2=line[y1+1:y2].strip()
                    h1=str(bin(int(k1[1],10))[2:].zfill(5)) 
                    h2= str(bin(int(k2[1],10))[2:].zfill(5)) 
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
                    func3="000"
                    opc="1100111"
                    mac_codet=h3[0:7]+h1+h2+func3+h3[7:]+opc
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")     
                    
            elif(line.__contains__("jalr") or line.__contains__("lb") or line.__contains__("lh") or line.__contains__("lw") or line.__contains__("ld")):
                if(line.__contains__("jalr")):
                    y=line.find("jalr")
                    h=y+4
                    func3="000"
                    opcode="1100111"
                if(line.__contains__("lb")) :
                    y=line.find("lb")
                    h=y+2
                    func3="000"
                    opcode="0000011"
                if(line.__contains__("ld")) :
                    y=line.find("ld")
                    h=y+2
                    func3="011"
                    opcode="0000011"
                if(line.__contains__("lh")) :
                    y=line.find("lh")
                    h=y+2
                    func3="001"
                    opcode="0000011"
                if(line.__contains__("lw")) :
                    y=line.find("lw")
                    h=y+2 
                    func3="010"
                    opcode="0000011"          
                y1=line.find("(")
                y2=line.find(")")
                j1=line[h:y1]
                if(line.find(",")>=0):
                    [k1,k3]=j1.split(",")
                    k1=k1.strip()
                    k3=k3.strip()
                else:
                    [k1,k3]=j1.split()
                    k1=k1.strip()
                    k3=k3.strip()    
                k2=line[y1+1:y2].strip()
                print(k1)
                print(k2)
                print(k3)
                h1=str(bin(int(k1[1],10))[2:].zfill(5)) 
                h2= str(bin(int(k2[1],10))[2:].zfill(5)) 
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
                    k3=2**12-k3; 
                    k3=str(k3)    
                    h3=str(bin(int(k3,10))[2:].zfill(12))     
                mac_codet=h3+h2+func3+h1+opcode
                mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                f2.write("0x"+mac_code+"\n")
                    
            elif (line.__contains__("beq") or line.__contains__("bge") or line.__contains__("blt") or line.__contains__("bne")):
                if "beq" in line:
                    sa1="beq"
                elif "bge" in line:
                    sa1="bge"
                elif "blt" in line:
                    sa1="blt"
                else:
                    sa1="bne"
                h=line.find(sa1)
                [k1,k2,k3]=line[h+3:].strip().split(",")
                print(k2[1])
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
                    h=line.find("lui")
                    [k1,k2]=line[h+3:].strip().split(",")
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
                    h=line.find("auipc")
                    [k1,k2]=line[h+5:].strip().split(",")
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
                    else:
                        h2=str(bin(int(k2,10))[2:].zfill(20)) 
                        mac_codet=h2+h1+opcode
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                f2.write("0x"+mac_code+"\n")

            elif(line.__contains__("jal ")):
                h=line.find("jal ")
                [k1,k2]=line[h+3:].strip().split(",")
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
        pc=pc+4        


                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                    
                        



                    




