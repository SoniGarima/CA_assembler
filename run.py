import registers
class run:
    def __init__(self):
        PC=0x0
        IR=0

    def fetch(self,mc_code):
        IR=mc_code
	PC_Temp=PC
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
                    print("DECODE: Operation is SUB, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                    print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                    executeR("SUB",rs1,rs2,rd)
                else:
                    print("DECODE: Operation is SRA, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                    print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                    executeR("SRA",rs1,rs2,rd)
            elif(fun7=="0000001"):
                if(fun3=="000"):
                    print("DECODE: Operation is MUL, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                    print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                    executeR("MUL",rs1,rs2,rd)
                elif(fun3=="100"):
                    print("DECODE: Operation is DIV, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                    print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                    executeR("DIV",rs1,rs2,rd)
                elif(fun3=="110"):
                    print("DECODE: Operation is REM, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                    print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                    executeR("REM",rs1,rs2,rd)
            elif(fun7=="0000000"):
                    if(fun3=="000"):
                        print("DECODE: Operation is ADD, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                        print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                        executeR("ADD",rs1,rs2,rd)
                    elif(fun3=="110"):
                        print("DECODE: Operation is OR, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                        print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                        executeR("OR",rs1,rs2,rd)
                    elif(fun3=="101"):
                        print("DECODE: Operation is SRL, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                        print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                        executeR("SRL",rs1,rs2,rd)
                    elif(fun3=="100"):
                        print("DECODE: Operation is XOR, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                        print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                        executeR("XOR",rs1,rs2,rd)
                    elif(fun3=="111"):
                        print("DECODE: Operation is AND, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                        print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                        executeR("AND",rs1,rs2,rd)
                    elif(fun3=="001"):
                        print("DECODE: Operation is SLL, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                        print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                        executeR("SLL",rs1,rs2,rd)
                    elif(fun3=="010"):
                        print("DECODE: Operation is SLT, first operand R"+int(rs1,2)+ " , Second operand R"+int(rs2,2)+", destination register R"+int(rd,2))
                        print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", R"+int(rs2,2)+" = "+registers.registers[int(rs2,2)])
                        executeR("SLT",rs1,rs2,rd)
        elif(opcode=="0010011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is ADDI, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeI("ADDI",rs1,imm,rd)
            if(fun3=="111"):
                print("DECODE: Operation is ANDI, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeI("ANDI",rs1,imm,rd)
            if(fun3=="110"):
                print("DECODE: Operation is ORI, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeI("ORI",rs1,imm,rd)    

        elif(opcode=="0000011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is LB, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeIL("LB",rs1,imm,rd)    
            if(fun3=="011"):
                print("DECODE: Operation is LD, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeIL("LD",rs1,imm,rd)    
            if(fun3=="001"):
                print("DECODE: Operation is LH, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeIL("LH",rs1,imm,rd)    
            if(fun3=="010"):
                print("DECODE: Operation is LW, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeIL("LW",rs1,imm,rd)                        
        elif(opcode="1100111"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is JALR, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeIL("JALR",rs1,imm,rd) 
        elif(opcode="0100011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rs2=curr_bin_ins[7:12]
            imm=curr_bin_ins[0:7]+curr_bin_ins[20:25]
            if(fun3=="010"):
                print("DECODE: Operation is SW, first operand R"+int(rs1,2)+ " , Second operand is Immediate field, destination register R"+int(rd,2))
                print("DECODE: Read registers R"+int(rs1,2)+" = "+registers.registers[int(rs1,2)]+", The immediate value is "+int(imm,2) )
                executeIS("SW",rs1,imm,rd)
                             
        elif(opcode=="0010111"or opcode=="0110111"):
		rd=curr_bin_ins[20:25]
		imm=curr_bin_ins[0:25]
                if(opcode=="0110111"):
			print("DECODE: Operation is LUI, first operand is Immediate field, destination register R",int(rd,2))
                        print("DECODE: The immediate value is",int(imm,2))
                        executeU("LUI",imm,rd,-1)
		elif(opcode=="0010111"):
			print("DECODE: Operation is AUIPC, first operand is Immediate field, destination register R",int(rd,2))
			print("DECODE: The immediate value is",int(imm,2))
                        executeU("AUIPC",imm,rd,PC_Temp)  
    def executeU(self,func,im,r,pc_t):
    	if(func=="LUI"):
		im_=(hex(int(im,2))[2:0]).zfill(5)+"000"
                 reg_update(im_,r)
        elif(fun=="AUIPC"):
		im_=(hex(int(im,2))[2:0]).zfill(5)+"000"
                pc_t=pc_t[2:]
                im_=im_+pc_t
                reg_update(im_,r) 
    def executeR(self,func,r1,r2,r3):
        if(func=="ADD"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1+num2,r3)
        if(func=="SUB"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1-num2,r3)
        if(func=="MUL"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1*num2,r3)
        if(func=="DIV"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1/num2,r3)
        if(func=="SRA"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1>>num2,r3)  ####
        if(func=="SRL"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1+num2,r3)   #####
        if(func=="AND"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1&num2,r3)       
        if(func=="XOR"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1^num2,r3) 
        if(func=="REM"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1%num2,r3)  
        if(func=="SLT"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write((num1<num2)?1:0,r3)
        if(func=="SLL"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1<<num2,r3)
        if(func=="OR"):
            num1=registers.registers[int(r1,2)]
            num2=registers.registers[int(r2,2)]
            mem_write(num1|num2,r3)                                  

    def executeI(self,func,r1,r2,r3):
        if(func=="ADDI"):
            num1=registers.registers[int(r1,2)]
            num2=int(r2,2)
            mem_write(num1+num2,r3) 
        if(func=="ANDI"):
            num1=registers.registers[int(r1,2)]
            num2=int(r2,2)
            mem_write(num1&num2,r3) 
        if(func=="ORI"):
            num1=registers.registers[int(r1,2)]
            num2=int(r2,2)
            mem_write(num1|num2,r3)

     def executeIL(self,func,r1,r2,r3):




               



        
