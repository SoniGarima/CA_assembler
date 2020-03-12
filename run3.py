import os
f1=open("coded.mc")
lines=f1.readlines()
pc_dict={}
for line in lines:
    [a1,a2]=line.split()
    pc_dict[int(a1,16)]=a2
from registers import registers
from memory import memory
my_mem=memory()
my_reg=registers()
from my_memory import mem_from_data
for key in mem_from_data:
    my_mem.write_byte(key,int(mem_from_data[key],2))
key+=1
class run:
    def __init__(self):
        self.PC=0x0
        self.IR=0
        self.PC_temp=self.PC
    def operation(self):
        while self.PC in pc_dict:
            mac_code=pc_dict[self.PC]
            self.fetch(mac_code)    

    def fetch(self,mc_code):
        self.IR=mc_code
        self.PC_temp=self.PC
        self.PC+=4
        print("FETCH:Fetch instruction "+self.IR+" from address "+str(self.PC-4))
        self.decode(self.IR)
    
    def decode(self,Ins):
        curr_bin_ins=bin(int(Ins[2:],16))[2:].zfill(32)    
        opcode=curr_bin_ins[25:]
        if(opcode=="0110011"):
            fun7=curr_bin_ins[0:7]
            fun3=curr_bin_ins[17:20]
            rs2=curr_bin_ins[7:12]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            if(fun7=="0100000"):
                if(fun3=="000"):
                    print("DECODE: Operation is SUB, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("SUB",rs1,rs2,rd)
                else:
                    print("DECODE: Operation is SRA, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("SRA",rs1,rs2,rd)
            elif(fun7=="0000001"):
                if(fun3=="000"):
                    print("DECODE: Operation is MUL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("MUL",rs1,rs2,rd)
                elif(fun3=="100"):
                    print("DECODE: Operation is DIV, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("DIV",rs1,rs2,rd)
                elif(fun3=="110"):
                    print("DECODE: Operation is REM, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("REM",rs1,rs2,rd)
            elif(fun7=="0000000"):
                if(fun3=="000"):
                    print("DECODE: Operation is ADD, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("ADD",rs1,rs2,rd)
                elif(fun3=="110"):
                    print("DECODE: Operation is OR, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("OR",rs1,rs2,rd)
                elif(fun3=="101"):
                    print("DECODE: Operation is SRL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("SRL",rs1,rs2,rd)
                elif(fun3=="100"):
                    print("DECODE: Operation is XOR, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("XOR",rs1,rs2,rd)
                elif(fun3=="111"):
                    print("DECODE: Operation is AND, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("AND",rs1,rs2,rd)
                elif(fun3=="001"):
                    print("DECODE: Operation is SLL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("SLL",rs1,rs2,rd)
                elif(fun3=="010"):
                    print("DECODE: Operation is SLT, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    self.executeR("SLT",rs1,rs2,rd)
        elif(opcode=="0010011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is ADDI, first operand R",int(rs1,2), " , Second operand is Immediate field,destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                self.executeI("ADDI",rs1,imm,rd)
            if(fun3=="111"):
                print("DECODE: Operation is ANDI, first operand R",int(rs1,2), " , Second operand is Immediate field,destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                self.executeI("ANDI",rs1,imm,rd)
            if(fun3=="110"):
                print("DECODE: Operation is ORI, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                self.executeI("ORI",rs1,imm,rd)    

        elif(opcode=="0000011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is LB, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIL("LB",rs1,imm,rd)    
            elif(fun3=="011"):
                print("DECODE: Operation is LD, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIL("LD",rs1,imm,rd)    
            elif(fun3=="001"):
                print("DECODE: Operation is LH, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIL("LH",rs1,imm,rd)    
            elif(fun3=="010"):
                print("DECODE: Operation is LW, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIL("LW",rs1,imm,rd)  
                                                
        elif(opcode=="1100111"):                                                
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is JALR, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                self.executeIJ(rs1,imm,rd) 
        elif(opcode=="0100011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[7:12]
            imm=curr_bin_ins[0:7]+curr_bin_ins[20:25]
            if(fun3=="010"):
                print("DECODE: Operation is SW, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIS("SW",rs1,imm,rd)
            elif(fun3=="011"):    
                print("DECODE: Operation is SD, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIS("SD",rs1,imm,rd)
            elif(fun3=="000"):
                print("DECODE: Operation is SB, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIS("SB",rs1,imm,rd)
            elif(fun3=="001"):
                print("DECODE: Operation is SH, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                self.executeIS("SH",rs1,imm,rd)
        elif(opcode=="1100011"):        
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rs2=curr_bin_ins[7:12]
            imm=curr_bin_ins[0:7]+curr_bin_ins[20:25]
            if(fun3=="000"):
                print("DECODE: Operation is BEQ, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                self.executeSB("BEQ",rs1,imm,rs2)
            if(fun3=="001"):    
                print("DECODE: Operation is BNE, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                self.executeSB("BNE",rs1,imm,rs2)
            if(fun3=="100"):    
                print("DECODE: Operation is BLT, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                self.executeSB("BLT",rs1,imm,rs2)
            if(fun3=="101"):    
                print("DECODE: Operation is BGE, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)+" = ",my_reg.regVal(int(rs2,2)))
                self.executeSB("BGE",rs1,imm,rs2)
    
        elif(opcode=="0010111" or opcode=="0110111"):
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:25]
            if(opcode=="0110111"): 
                print("DECODE: Operation is LUI, first operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: The immediate value is",int(imm,2))
                self.executeU("LUI",imm,rd,-1)
            elif(opcode=="0010111"):
                print("DECODE: Operation is AUIPC, first operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: The immediate value is"+int(imm,2))
                self.executeU("AUIPC",imm,rd,self.PC_Temp)  
        elif(opcode=="1101111"):
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:25]
            imm0=imm[0]
            imm1=imm[1:11]
            imm2=imm[11]
            imm3=imm[12:20]
            imm_=imm1+imm2+imm3+imm0
            print("DECODE: Operation is JAL,the first operand is Immediate field, destination register R",int(rd,2))
            print("DECODE: The immediate value is",int(imm_,2))
            self.executeUj("JAL",imm_,rd,self.PC_Temp)
    
    def executeUj(self,func,im,r,pc_t):
        pc_t=pc_t[2:]
        pc_temp=hex(int(pc_t,16))
        pc_temp+=4
        PC+=im
        reg_update((pc_temp),r)             
                
    def executeR(self,func,r1,r2,r3):
        if(func=="ADD"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1+num2)
        if(func=="SUB"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1-num2)
        if(func=="MUL"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1*num2)
        if(func=="DIV"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1/num2)
        if(func=="SRA"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            xx=bin(num1)[2:]
            my_msb=xx[31]
            aa=str(num1>>num2)
            aa[0:num2]=my_msb
            my_reg.write_reg(int(r3,2),int(aa,2))##############
        if(func=="SRL"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1>>num2)###############3
        if(func=="AND"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1&num2)     
        if(func=="XOR"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1^num2)
        if(func=="REM"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1%num2)
        if(func=="SLT"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            if(num1>num2):
                my_reg.write_reg(int(r3,2),0)
            else:
                my_reg.write_reg(int(r3,2),1)             
        if(func=="SLL"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1<<num2)
        if(func=="OR"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            my_reg.write_reg(int(r3,2),num1|num2)                            

    def executeI(self,func,r1,r2,r3):
        if(func=="ADDI"):
            num1=my_reg.regVal(int(r1,2))
            num2=int(r2,2)
            my_reg.write_reg(int(r3,2),num1+num2)
        if(func=="ANDI"):
            num1=my_reg.regVal(int(r1,2))
            num2=int(r2,2)
            my_reg.write_reg(int(r3,2),num1&num2)
        if(func=="ORI"):
            num1=my_reg.regVal(int(r1,2))
            num2=int(r2,2)
            my_reg.write_reg(int(r3,2),num1|num2)
    
    def executeU(self,func,im,r,pc_t):
        if(func=="LUI"):
            im_=(hex(int(im,2))[2:0]).zfill(5)+"000"
            im_=int(im_,16)
            reg_update(im_,r)
        else:
            im_=(hex(int(im,2))[2:0]).zfill(5)+"000"
            im_=im_+pc_t
            reg_update(im_,r)     
                                                                               

    def executeIS(self,func,r1,r2,r3):
        eff_address=my_reg.regVal(int(r3,2))+int(r2,2)
        if(func=="SB"):
            my_mem.write_byte(eff_address,my_reg.regVal(int(r1,2)))
        elif(func=="SH"):
            my_mem.write_half(eff_address,my_reg.regVal(int(r1,2)))
        elif(func=="SW"):
            my_mem.write_word(eff_address,my_reg.regVal(int(r1,2)))
        else:
            my_mem.write_db(eff_address,my_reg.regVal(int(r1,2)))

    def executeSB(self,func,r1,r2,r3):
        if(func=="BEQ"):
            if(int(r1,2)==int(r3,2)):
                self.PC=self.PC+int(r2,2)
        elif(func=="BNE"):
            if(int(r1,2)!=int(r3,2)):
                self.PC=self.PC+int(r2,2)
        elif(func=="BLT"):
            if(int(r1,2)<int(r3,2)):
                self.PC=self.PC+int(r2,2)  
        elif(func=="BGE"):
            if(int(r1,2)>=int(r3,2)):
                self.PC=self.PC+int(r2,2)      

    def executeIL(self,func,r1,r2,r3):
        eff_address=my_reg[int(r3,2)]+int(r2,2)
        if(func=="LB"):
            retu=my_mem.ret_byte(eff_address)
            my_reg.write_reg(eff_address,retu)
        if(func=="LH"):
            retu=my_mem.ret_half(eff_address)
            my_reg.write_reg(eff_address,retu)
        if(func=="LW"):
            retu=my_mem.ret_word(eff_address)
            my_reg.write_reg(eff_address,retu)
        if(func=="LD"):
            retu=my_mem.ret_db(eff_address)
            my_reg.write_reg(eff_address,retu)  



    def executeIJ(self,r1,r2,r3):
        eff_address=my_reg[int(r1,2)]+int(r2,2)     
        my_reg.write_reg(int(r3,2),self.PC+4)
        self.PC=eff_address

sess=run()
sess.operation()
for i in range(0,32):
    print(my_reg.regVal(i))
    








              







    
