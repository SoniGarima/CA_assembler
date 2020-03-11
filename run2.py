from registers import registers
from memory import memory
my_mem=memory()
my_reg=registers()
from my_memory import mem_from_data
for key in mem_from_data:
    my_mem[key]=mem_from_data[key]
print(my_mem)
print(mem_from_data)    
class run:
    def __init__(self):
        PC=0x0
        IR=0
        PC_temp=PC

    def fetch(self,mc_code):
        IR=mc_code
        PC_temp=PC
        PC+=4
        print("FETCH:Fetch instruction"+IR+" from address "+str(PC))
        decode(IR)
    
    def decode(self):
        curr_bin_ins=bin(int(IR[2:],16))[2:].zfill(32)    
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
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("SUB",rs1,rs2,rd)
                else:
                    print("DECODE: Operation is SRA, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("SRA",rs1,rs2,rd)
            elif(fun7=="0000001"):
                if(fun3=="000"):
                    print("DECODE: Operation is MUL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("MUL",rs1,rs2,rd)
                elif(fun3=="100"):
                    print("DECODE: Operation is DIV, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("DIV",rs1,rs2,rd)
                elif(fun3=="110"):
                    print("DECODE: Operation is REM, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("REM",rs1,rs2,rd)
            elif(fun7=="0000000"):
                if(fun3=="000"):
                    print("DECODE: Operation is ADD, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("ADD",rs1,rs2,rd)
                elif(fun3=="110"):
                    print("DECODE: Operation is OR, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",registers.registers[int(rs1,2)],", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("OR",rs1,rs2,rd)
                elif(fun3=="101"):
                    print("DECODE: Operation is SRL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("SRL",rs1,rs2,rd)
                elif(fun3=="100"):
                    print("DECODE: Operation is XOR, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("XOR",rs1,rs2,rd)
                elif(fun3=="111"):
                    print("DECODE: Operation is AND, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("AND",rs1,rs2,rd)
                elif(fun3=="001"):
                    print("DECODE: Operation is SLL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("SLL",rs1,rs2,rd)
                elif(fun3=="010"):
                    print("DECODE: Operation is SLT, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                    executeR("SLT",rs1,rs2,rd)
        elif(opcode=="0010011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is ADDI, first operand R",int(rs1,2), " , Second operand is Immediate field,destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeI("ADDI",rs1,imm,rd)
            if(fun3=="111"):
                print("DECODE: Operation is ANDI, first operand R",int(rs1,2), " , Second operand is Immediate field,destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeI("ANDI",rs1,imm,rd)
            if(fun3=="110"):
                print("DECODE: Operation is ORI, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeI("ORI",rs1,imm,rd)    

        elif(opcode=="0000011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is LB, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIL("LB",rs1,imm,rd)    
            elif(fun3=="011"):
                print("DECODE: Operation is LD, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIL("LD",rs1,imm,rd)    
            elif(fun3=="001"):
                print("DECODE: Operation is LH, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIL("LH",rs1,imm,rd)    
            elif(fun3=="010"):
                print("DECODE: Operation is LW, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIL("LW",rs1,imm,rd)  
                                                
        elif(opcode=="1100111"):                                                
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is JALR, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIJ(rs1,imm,rd) 
        elif(opcode=="0100011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rs2=curr_bin_ins[7:12]
            imm=curr_bin_ins[0:7]+curr_bin_ins[20:25]
            if(fun3=="010"):
                print("DECODE: Operation is SW, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIS("SW",rs1,imm,rd)
            elif(fun3=="011"):    
                print("DECODE: Operation is SD, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIS("SD",rs1,imm,rd)
            elif(fun3=="000"):
                print("DECODE: Operation is SB, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIS("SB",rs1,imm,rd)
            elif(fun3=="001"):
                print("DECODE: Operation is SH, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", The immediate value is ",int(imm,2) )
                executeIS("SH",rs1,imm,rd)
        elif(opcode=="1100011"):        
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rs2=curr_bin_ins[7:12]
            imm=curr_bin_ins[0:7]+curr_bin_ins[20:25]
            if(fun3=="000"):
                print("DECODE: Operation is BEQ, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", Second register R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                executeSB("BEQ",rs1,imm,rs2)
            if(fun3=="001"):    
                print("DECODE: Operation is BNE, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", Second register R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                executeSB("BNE",rs1,imm,rs2)
		    if(fun3=="100"):
                print("DECODE: Operation is BLT, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", Second register R",int(rs2,2)," = "+registers.registers[int(rs2,2)])
                executeSB("BLT",rs1,imm,rs2)
		    if(fun3=="101"):
                print("DECODE: Operation is BGE, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = "+registers.registers[int(rs1,2)]+", Second register R",int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                executeSB("BGE",rs1,imm,rs2)
	
        elif(opcode=="0010111" or opcode=="0110111"):
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:25]
            if(opcode=="0110111"): 
                print("DECODE: Operation is LUI, first operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: The immediate value is",int(imm,2))
                executeU("LUI",imm,rd,-1)
            elif(opcode=="0010111"):
		        print("DECODE: Operation is AUIPC, first operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: The immediate value is"+int(imm,2))
                executeU("AUIPC",imm,rd,PC_Temp)  
        elif(opcode=="1101111"):
		    rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:25]
            imm0=imm[0]
            imm1=imm[1:11]
            imm2=imm[11]
            imm3=imm[12:20]
            imm_=imm1+imm2+imm3+imm4
            print("DECODE: Operation is JAL,the first operand is Immediate field, destination register R",int(rd,2))
            print("DECODE: The immediate value is",int(imm_,2))
            executeUj("JAL",imm_,rd,PC_Temp)
    
    def executeUj(self,func,im,r,pc_t):
		pc_t=pc_t[2:]
        pc_temp=hex(int(pc_t,16))
        pc_temp+=4
        PC+=im
        reg_update((pc_temp),r)             
                
    def executeR(self,func,r1,r2,r3):
        if(func=="ADD"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1+num2)
        if(func=="SUB"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1-num2)
        if(func=="MUL"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1*num2)
        if(func=="DIV"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1/num2)
        if(func=="SRA"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            xx=bin(num1)[2:]
            my_msb=xx[31]
            aa=str(num1>>num2)
            aa[0:num2]=my_msb
            my_reg.write_reg(int(r3,2),int(aa,2))##############
        if(func=="SRL"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1>>num2)###############3
        if(func=="AND"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1&num2)     
        if(func=="XOR"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1^num2)
        if(func=="REM"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1%num2)
        if(func=="SLT"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            if(num1>num2):
                my_reg.write_reg(int(r3,2),0)
            else:
                my_reg.write_reg(int(r3,2),1)             
        if(func=="SLL"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1<<num2)
        if(func=="OR"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            my_reg.write_reg(int(r3,2),num1|num2)                            

    def executeI(self,func,r1,r2,r3):
        if(func=="ADDI"):
            num1=registers.registers[int(r1,2)]
            num2=int(r2,2)
            my_reg.write_reg(int(r3,2),num1+num2)
        if(func=="ANDI"):
            num1=registers.registers[int(r1,2)]
            num2=int(r2,2)
            my_reg.write_reg(int(r3,2),num1&num2)
        if(func=="ORI"):
            num1=registers.registers[int(r1,2)]
            num2=int(r2,2)
            my_reg.write_reg(int(r3,2),num1|num2)
	
    def executeU(self,func,im,r,pc_t):
    	    if(func=="LUI"):
		    im_=(hex(int(im,2))[2:0]).zfill(5)+"000"
		    reg_update(im_,r)
	    elif(fun=="AUIPC"):
		    im_=(hex(int(im,2))[2:0]).zfill(5)+"000"
		    im_=im_+pc_t
		    reg_update(im_,r)	

    def executeIS(self,func,r1,r2,r3):
        eff_address=my_reg[int(r3,2)]+int(r2,2)
        if(func="SB"):
            my_mem.write_byte(eff_address,my_reg[int(r1,2)])
        elif(func=="SH"):
            my_mem.write_half(eff_address,my_reg[int(r1,2)])
        elif(func=="SW"):
            my_mem.write_word(eff_address,my_reg[int(r1,2)])
        else:
            my_mem.write_db(eff_address,my_reg[int(r1,2)])

    def executeSB(self,func,r1,r2,r3):
        if(func=="BEQ"):
            if(int(r1,2)==int(r3,2)):
                PC=PC+int(r2,2)
        elif(func=="BNE"):
            if(int(r1,2)!=int(r3,2)):
                PC=PC+int(r2,2)
        elif(func=="BLT"):
            if(int(r1,2)<int(r3,2)):
                PC=PC+int(r2,2)  
        elif(func=="BGE"):
            if(int(r1,2)>=int(r3,2)):
                PC=PC+int(r2,2)      

    def executeIL(self,func,r1,r2,r3):
        eff_address=my_reg[int(r3,2)]+int(r2,2)
        if(func=="LB"):
            retu=my_mem.ret_byte(eff_address)
            my_reg.write_reg(retu)
        if(func=="LH"):
            retu=my_mem.ret_half(eff_address)
            my_reg.write_reg(retu)
        if(func=="LW"):
            retu=my_mem.ret_word(eff_address)
            my_reg.write_reg(retu)
        if(func=="LD"):
            retu=my_mem.ret_db(eff_address)
            my_reg.write_reg(retu)  



    def executeIJ(self,r1,r2,r3):
        eff_address=my_reg[int(r1,2)]+int(r2,2)     
        my_reg.write_reg(int(r3,2),PC+4)
        PC=eff_address

        








              







    
