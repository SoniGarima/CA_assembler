
# coding: utf-8

# In[4]:

f2=open("coded.mc","x")
lines=f1.readlines()
for line in lines:
    str1,str2=line.split(" ")
    k1,k2,k3=str2.split(",")
    h3=str(bin(int(k1[1],10))[2:]).zfill(5)
    h2=str(bin(int(k2[1],10))[2:]).zfill(5)
    h1=str(bin(int(k3[1],10))[2:]).zfill(5)
    opc="0110011"
    if(str1=="sra" or str1=="sub"):
        fun7="0100000"
    elif(str1=="mul" or str1=="div" or str1=="rem"):
        fun7="0000001"
    else:
        fun7="0000000"
    if(str1=="add" or str1=="sub" or str1=="mul"):
        fun3="000"
    elif(str1=="rem" or str2=="or"):
        fun3="110"
    elif(str1=="sra" or str2=="srl"):
        fun3="101"
    elif(str1=="div" or str1=="xor"):
        fun3="100"
    elif(str1=="and"):
        fun3="111"
    elif(str1=="sll"):
        fun3="001"
    elif(str1=="slt"):
        fun3="010"
    mac_codet=fun7+h1+h2+fun3+h3+opc
    mac_code=str(hex(int(mac_codet,2))[2:].zfill(8))
    #f2.write("0x"+mac_code+"\n")
    f2=str("0x"+mac_code+"\n")
    print(line+"="+f2)


