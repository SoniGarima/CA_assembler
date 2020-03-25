import os
from memory import memory
#data.asm:Fibonacci code
#data2.asm: factorial code
#data4.asm: Bubble Sort
FileName=""
inv=input()
if(inv=='1'):
    FileName="data.asm"
elif(inv=='2'):
    FileName="data2.asm"
elif(inv=='3'):
    FileName="data4.asm"
else:
    print("InvalidInput:Please give a valid input")
    
f1=open(FileName,"r")  ## change the fileName here...
os.remove("coded.mc")
f2=open("coded.mc","x")
os.remove("my_memory.py")
f3=open("my_memory.py","x")
lines=f1.readlines()
mem=memory()
output=[]
n_err=1
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
labels={}
data_parts=[]
data_address=0x10000000
while(k<len(lines) and(case==2 or case==3)):
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
f3.write("mem_from_data=")       
f3.write("{\n")
for i in range(0x10000000,data_address):
    f3.write(str(hex(i))+":"+"\""+(mem.ret_byte((i)))+"\""+",\n")
f3.write("}")   

##### MAIN PART #################################################
pc=0x0
count1=0
pc1=0x0
for line in lines:
    if(line.__contains__(".data") or line.__contains__(".text")):
        pass
    elif line in data_parts:
        pass
    elif(line.strip()==''):
        pass
    elif(line.strip().endswith(":")==1):
        label=line.split(":")
        labels[label[0].strip()]=pc1
    elif(line.__contains__(":")):
        ind=line.find(":")
        label=line[:ind].strip()
        labels[label]=pc1
        pc1+=4
    else:
        pc1+=4
# print("The PCs of labels are",labels)        

############# from here ####################################        
for line in lines:
    if(line.strip()==""):
        continue
    elif(line!=" "):
        count1=count1+1
        # line=line.replace(" ","")
        # line=line.replace("\n","")
        if(line.__contains__(".data") or line.__contains__(".text")):
            continue
        elif(line in data_parts):
            continue
        
        elif(line.strip().endswith(":")==1):
            continue
        else:
            f2.write(str(hex(pc))+"  ")
            if(line.__contains__("add ") or line.__contains__("sub ") or line.__contains__("mul ") or line.__contains__("div ") or line.__contains__("sra ") or line.__contains__("rem ") or line.__contains__("or ") or line.__contains__("srl") or line.__contains__("xor ") or line.__contains__("and ") or line.__contains__("sll ") or line.__contains__("slt ")):
                if(line.__contains__("add ")):
                    try:
                        h=line.find("add ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="000"
                        fun7="0000000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by add are 3, correct your code.") 
                        n_err+=1
                        break 
                if(line.__contains__("sub ")):
                    try:
                        h=line.find("sub ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="000"
                        fun7="0100000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by sub are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("sra ")):
                    try:
                        h=line.find("sra ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="101"
                        fun7="0100000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by sra are 3, correct your code.") 
                        n_err+=1
                        break
                            
                if(line.__contains__("div ")):
                    try:
                        h=line.find("div ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="100"
                        fun7="0000001"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by div are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("mul ")):
                    try:
                        h=line.find("mul ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="000"
                        fun7="0000001"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by mul are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("rem ")):
                    try:
                        h=line.find("rem ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="110"
                        fun7="0000001"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by rem are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("or ")):
                    try:
                        h=line.find("or ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="110"
                        fun7="0000000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by or are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("srl ")):
                    try:
                        h=line.find("srl ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="101"
                        fun7="0000000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by srl are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("xor ")):
                    try:
                        h=line.find("xor ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="100"
                        fun7="0000000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by xor are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("and ")):
                    try:
                        h=line.find("and ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="111"
                        fun7="0000000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by and are 3, correct your code.") 
                        n_err+=1
                        break    
                if(line.__contains__("sll ")):
                    try:
                        h=line.find("sll ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="001"
                        fun7="0000000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by sll are 3, correct your code.")
                        n_err+=1  
                        break  
                if(line.__contains__("slt ")):
                    try:
                        h=line.find("slt ")
                        if(line.__contains__(",")):
                            [k1,k2,k3]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                            k3=k3.strip()
                        else:
                            [k1,k2,k3]=line[h+3:].strip().split()
                        h3=str(bin(int(k1[1:],10))[2:]).zfill(5)
                        h2=str(bin(int(k2[1:],10))[2:]).zfill(5)
                        h1=str(bin(int(k3[1:],10))[2:]).zfill(5)
                        opc="0110011"
                        fun3="010"
                        fun7="0000000"
                        if(int(h1,2)>31 or int(h2,2)>31 or int(h3,3)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        mac_codet=fun7+h1+h2+fun3+h3+opc
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by slt are 3, correct your code.") 
                        n_err+=1
                        break    
            elif(line.__contains__("addi ") or line.__contains__("andi ") or line.__contains__("ori ")):
                funn=""
                if(line.__contains__("addi ")):
                    funn="addi"
                    func3="000"
                    h=line.find("addi ")
                    h=h+4
                elif(line.__contains__("andi ")):
                    funn="andi"
                    func3="111"
                    h=line.find("andi ")
                    h=h+4
                else:
                    funn="ori"
                    func3="110" 
                    h=line.find("ori ")  
                    h=h+3
                try:   
                    if(line.__contains__(",")):
                        [k1,k2,k3]=line[h:].strip().split(",")
                        k1=k1.strip()
                        k2=k2.strip()
                        k3=k3.strip()
                    else:
                        [k1,k2,k3]=line[h:].strip().split()
                    h1=str(bin(int(k1[1:],10))[2:].zfill(5))
                    h2=str(bin(int(k2[1:],10))[2:].zfill(5))
                    if(int(h1,2)>31 or int(h2,2)>31 ):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                    h3=""
                    if(int(k3)>2047 or int(k3)<-2048):
                        print("OutOfRangeError:in line:"+line+"--->"+" 12-bit immediate values can vary from -2048 to 2047") 
                        n_err+=1
                        break 
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
                except:
                    print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by"+funn+ " are 3, with one immediate field,correct your code.") 
                    n_err+=1
                    break     
            
            elif(line.__contains__("sb ") or line.__contains__("sh ") or line.__contains__("sd ") or line.__contains__("sw ")):
                if(line.__contains__("sb ")):
                    try:
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
                        h1=str(bin(int(k1[1:],10))[2:].zfill(5)) 
                        h2= str(bin(int(k2[1:],10))[2:].zfill(5)) 
                        if(int(h1,2)>31 or int(h2,2)>31 ):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        if(int(k3)>2047 or int(k3)<-2048):
                            print("OutOfRangeError:in line:"+line+"--->"+" 12-bit immediate values can vary from -2048 to 2047") 
                            n_err+=1
                            break 
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
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by sb are 3, correct your code.") 
                        n_err+=1
                        break     
                
                if(line.__contains__("sw ")):
                    try:
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
                        h1=str(bin(int(k1[1:],10))[2:].zfill(5)) 
                        h2= str(bin(int(k2[1:],10))[2:].zfill(5)) 
                        if(int(h1,2)>31 or int(h2,2)>31 ):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        if(int(k3)>2047 or int(k3)<-2048):
                            print("OutOfRangeError:in line:"+line+"--->"+" 12-bit immediate values can vary from -2048 to 2047") 
                            n_err+=1
                            break 
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
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by sw are 3, correct your code.") 
                        n_err+=1
                        break        
                
                if(line.__contains__("sd ")):
                    try:
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
                        h1=str(bin(int(k1[1:],10))[2:].zfill(5)) 
                        h2= str(bin(int(k2[1:],10))[2:].zfill(5)) 
                        if(int(h1,2)>31 or int(h2,2)>31 ):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        if(int(k3)>2047 or int(k3)<-2048):
                            print("OutOfRangeError:in line:"+line+"--->"+" 12-bit immediate values can vary from -2048 to 2047") 
                            n_err+=1
                            break 
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
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by sd are 3, correct your code.") 
                        n_err+=1
                        break      
                
                if(line.__contains__("sh ")):
                    try:
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
                        h1=str(bin(int(k1[1:],10))[2:].zfill(5)) 
                        h2= str(bin(int(k2[1:],10))[2:].zfill(5)) 
                        if(int(h1,2)>31 or int(h2,2)>31 ):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        if(int(k3)>2047 or int(k3)<-2048):
                            print("OutOfRangeError:in line:"+line+"--->"+" 12-bit immediate values can vary from -2048 to 2047") 
                            n_err+=1
                            break 
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
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by sh are 3, correct your code.") 
                        n_err+=1
                        break     
                    
            elif(line.__contains__("jalr ") or line.__contains__("lb ") or line.__contains__("lh ") or line.__contains__("lw ") or line.__contains__("ld ")):
                funn=""
                if(line.__contains__("jalr")):
                    funn="jalr"
                    y=line.find("jalr")
                    h=y+4
                    func3="000"
                    opcode="1100111"
                if(line.__contains__("lb")) :
                    funn="lb"
                    y=line.find("lb")
                    h=y+2
                    func3="000"
                    opcode="0000011"
                if(line.__contains__("ld")) :
                    funn="ld"
                    y=line.find("ld")
                    h=y+2
                    func3="011"
                    opcode="0000011"
                if(line.__contains__("lh")) :
                    funn="lh"
                    y=line.find("lh")
                    h=y+2
                    func3="001"
                    opcode="0000011"
                if(line.__contains__("lw")) :
                    funn="lw"
                    y=line.find("lw")
                    h=y+2 
                    func3="010"
                    opcode="0000011"
                try:              
                    y1=line.find("(")
                    y2=line.find(")")
                    if(y1>0 and y2>0):
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
                        h1=str(bin(int(k1[1:],10))[2:].zfill(5)) 
                        h2= str(bin(int(k2[1:],10))[2:].zfill(5)) 
                        if(int(h1,2)>31 or int(h2,2)>31 ):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        if(int(k3)>2047 or int(k3)<-2048):
                            print("OutOfRangeError:in line:"+line+"--->"+" 12-bit immediate values can vary from -2048 to 2047") 
                            n_err+=1
                            break 
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
                        mac_codet=h3+h2+func3+h1+opcode
                        mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                        f2.write("0x"+mac_code+"\n")
                    else:
                        print("Loading value of a variable in register is a pseudo instruction and requires two RISC-V instructions") 
                        n_err+=1
                except:
                    print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by"+funn+" are 3, correct your code.") 
                    n_err+=1
                    break           
                    
            elif (line.__contains__("beq ") or line.__contains__("bge ") or line.__contains__("blt ") or line.__contains__("bne ")):
                if "beq" in line:
                    sa1="beq"
                elif "bge" in line:
                    sa1="bge"
                elif "blt" in line:
                    sa1="blt"
                else:
                    sa1="bne"
                h=line.find(sa1)
                try:
                    if(line.__contains__(",")):
                        [k1,k2,k3]=line[h+3:].strip().split(",")
                        k1=k1.strip()
                        k2=k2.strip()
                        k3=k3.strip()
                    else:
                        [k1,k2,k3]=line[h+3:].strip().split()
                    h1=str(bin(int(k1[1:],10))[2:].zfill(5))
                    h2=str(bin(int(k2[1:],10))[2:].zfill(5))
                    if(int(h1,2)>31 or int(h2,2)>31 ):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                    try:
                        pc_label=labels[k3]
                    except:
                        print("LabelNotDefinedError:in line:"+line+" label '"+k3+"'used, but not defined")  
                        n_err+=1
                        break;  
                    imm0=pc_label-pc
                    if(imm0>2047 or imm0<-2048):
                        print("OutOfRangeError:in line:"+line+"--->"+" 12-bit immediate values can vary from -2048 to 2047") 
                        n_err+=1
                        break 
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
                except:
                    print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by"+sa1+" are 3, correct your code.") 
                    n_err+=1
                    break    

            elif(line.__contains__("lui ") or line.__contains__("auipc ")):
                if(line.__contains__("lui")):
                    try:
                        h=line.find("lui")
                        if(line.__contains__(",")):
                            [k1,k2]=line[h+3:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                        else:
                            [k1,k2]=line[h+3:].strip().split()
                        h1=str(bin(int(k1[1:],10))[2:].zfill(5))
                        if(int(h1,2)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        opcode="0110111"
                        if(k2.startswith("0x")):
                            if(int(k2,16)>1048575 or int(k2,16)<-1048576):
                                print("OutOfRangeError:in line:"+line+"--->"+" 20-bit immediate values can vary from -1048576 to 1048575") 
                                n_err+=1
                                break 
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
                        elif(k2.startswith("0b")):
                            if(int(k2,2)>1048575 or int(k2,2)<-1048576):
                                print("OutOfRangeError:in line:"+line+"--->"+" 20-bit immediate values can vary from -1048576 to 1048575") 
                                n_err+=1
                                break 
                            x2=k2[2:]
                            h2=(hex(int(x2,2))[2:]).zfill(5)
                            ro=(hex(int(h1+opcode,2))[2:]).zfill(3)
                            mac_code=h2+ro  

                        else:
                            if(int(k2,10)>1048575 or int(k2,10)<-1048576):
                                print("OutOfRangeError:in line:"+line+"--->"+" 20-bit immediate values can vary from -1048576 to 1048575") 
                                n_err+=1
                                break 
                            h2=str(bin(int(k2,10))[2:].zfill(20))
                            mac_codet=h2+h1+opcode
                            mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by lui are 2, correct your code.") 
                        n_err+=1
                        break        
                else:
                    try:
                        h=line.find("auipc")
                        if(line.__contains__(",")):
                            [k1,k2]=line[h+5:].strip().split(",")
                            k1=k1.strip()
                            k2=k2.strip()
                        else:
                            [k1,k2]=line[h+5:].strip().split()
                        h1=str(bin(int(k1[1:],10))[2:].zfill(5))
                        if(int(h1,2)>31):
                            print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                            n_err+=1
                            break 
                        opcode="0010111"
                        if(k2.startswith("0x")):
                            if(int(k2,16)>1048575 or int(k2,16)<-1048576):
                                print("OutOfRangeError:in line:"+line+"--->"+" 20-bit immediate values can vary from -1048576 to 1048575") 
                                n_err+=1
                                break 
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
                            if(int(k2,2)>1048575 or int(k2,2)<-1048576):
                                print("OutOfRangeError:in line:"+line+"--->"+" 20-bit immediate values can vary from -1048576 to 1048575") 
                                n_err+=1
                                break 
                            x2=k2[2:]
                            h2=(hex(int(x2,2))[2:]).zfill(5)
                            ro=(hex(int(h1+opcode,2))[2:]).zfill(3)
                            mac_code=h2+ro 

                        else:
                            if(int(k2,10)>1048575 or int(k2,10)<-1048576):
                                print("OutOfRangeError:in line:"+line+"--->"+" 20-bit immediate values can vary from -1048576 to 1048575") 
                                n_err+=1
                                break 
                            h2=str(bin(int(k2,10))[2:].zfill(20)) 
                            mac_codet=h2+h1+opcode
                            mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    except:
                        print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by auipc are 2, correct your code.") 
                        n_err+=1
                        break        
                f2.write("0x"+mac_code+"\n")

            elif(line.__contains__("jal ")):
                h=line.find("jal ")
                try:
                    if(line.__contains__(",")):
                        [k1,k2]=line[h+3:].strip().split(",")
                        k1=k1.strip()
                        k2=k2.strip()
                    else:
                        [k1,k2]=line[h+3:].strip().split()
                    h1=str(bin(int(k1[1:],10))[2:].zfill(5))
                    if(int(h1,2)>31):
                        print("ERROR",n_err,":in line:"+line+"--->"+" There are only 32 registers available. Please use one of them.") 
                        n_err+=1
                        break 
                    try:
                        pc_label=labels[k2]
                    except:
                        print("LabelNotDefinedError:in line:"+line+" label '"+k2+"'used, but not defined")  
                        n_err+=1
                        break;    
                    imm0=labels[k2]-pc
                    if(imm0>1048575 or imm0<-1048576):
                        print("OutOfRangeError:in line:"+line+"--->"+" 20-bit immediate values can vary from -1048576 to 1048575") 
                        n_err+=1
                        break 
                    if(imm0>=0):
                        imm=str(bin(imm0)[2:].zfill(20)) 
                    else:  
                        imm=str(bin(imm0)[3:].zfill(20)) 
                        imm0=int(imm,2)
                        imm0=2**20-imm0
                        imm0=str(imm0)    
                        imm0=str(int(imm0,10)+1)
                        imm=str(bin(int(imm0,10))[2:].zfill(20)) 
                    imm=imm[0]+imm[9:]+imm[8]+imm[1:8]
                    opcode="1101111"
                    mac_codet=imm+h1+opcode
                    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
                    f2.write("0x"+mac_code+"\n")
                except:
                    print("ERROR",n_err,":in line:"+line+"--->"+" The number of arguements taken by jal are 2, correct your code.") 
                    n_err+=1
                    break     
            else:
                print("You have used the RISC-V instruction other than specified one. Please check your code!")
                n_err+=1 
                break       
            pc+=4
if(n_err==1):    
    print("The corresponding machine code is saved in the same folder as this with the name:'coded.mc'\n")

                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                    
                        



                    




