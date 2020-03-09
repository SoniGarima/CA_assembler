import os
f1=open("data.asm","r")
os.remove("coded.mc")
f2=open("coded.mc","x")
lines=f1.readlines()
print(lines)
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
memory={}
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
            labels_vars[lines[k][0:colon]]=data_address;
            t1=(lines[k]).find(".byte")
            t2=(lines[k]).find(".word")
            t3=(lines[k]).find(".dword")
            t4=(lines[k]).find(".asciiz")
            t5=(lines[k]).find(".half")
            if(t1>=0):
                num_list=(lines[k][t1+5:].strip()).split()
                for num in num_list:
                    memory[str(hex(data_address))]=num
                    data_address+=1 
            elif(t2>=0):
                num_list=(lines[k][t2+5:].strip()).split()
                for num in num_list:
                    memory[str(hex(data_address))]=num
                    data_address+=4
            elif(t3>=0):
                num_list=(lines[k][t3+6:].strip()).split()
                for num in num_list:
                    memory[str(hex(data_address))]=num
                    data_address+=8
            elif(t5>=0):
                num_list=(lines[k][t5+5:].strip()).split()
                for num in num_list:
                    memory[str(hex(data_address))]=num
                    data_address+=2
            else:
                my_str_list=(lines[k][t4+7:].strip())  
                for c in my_str_list[1:len(my_str_list)-1]:
                    memory[str(hex(data_address))]=c
                    data_address+=1  
            data_parts.append(lines[k])                                                   
    k=k+1
print(data_parts)      
for key in memory:
    print(key+":"+memory[key]+"\n")     

##### MAIN PART #####################

for line in lines:
    if(line.__contains__(".data") or line.__contains__(".text")):
        pass
    elif(line in data_parts):
        pass
    else:
        if(line.__contains__("add") or line.__contains__("sub") or line.__contains__("mul") or line.__contains__("div") or line.__contains__("sra") or line.__contains__("rem") or line.__contains__("or") or line.__contains__("srl") or line.__contains__("xor") or line.__contains__("and") or line.__contains__("sll") or line.__contains__("slt")):
            if(line.__contains__("add")):
                h=line.find("add")
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
            if(line.__contains__("or")):
                h=line.find("or")
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
            if(line.__contains__("and")):
                h=line.find("and")
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
                h=line.find("010")
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
            
            
            
            



    




