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
print(pc_dict)    
class pipelining:
    def __init__(self):
        self.PC=0x0
        self.IR=0
        self.PC_temp=self.PC
        self.clock=0 
        self.Cycles = 0
        self.IF = '';
        self.ID = {};
        self.IE = {};
        self.IM = [];  
    
    def pipeline(self):
        while(self.PC in pc_dict):
            if(self.Cycles == 0):
                self.fetch(pc_dict[self.PC])
                self.Cycles+=1
            if(self.Cycles == 1):
                print("-----------------------------------------------------------------------")
                self.ID = self.decode(self.IF)
                self.fetch(pc_dict[self.PC])
                self.Cycles+=1
            if(self.Cycles == 2):
                print("-----------------------------------------------------------------------")
                if(self.ID['Format']=='R'):
                    self.IE = self.executeR(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])
                if(self.ID['Format'] == 'I'):
                    self.IE = self.executeI(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
                if(self.ID['Format'] == 'IL'):
                    self.IE = self.executeIL(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'IJ'):
                    self.IE = self.executeIJ(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'IS'):
                    self.IE = self.executeIS(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
                if(self.ID['Format'] == 'SB'):
                    self.IE = self.executeSB(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'U'):
                    self.IE = self.executeU(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1]) 
                    print(self.IE)
                if(self.ID['Format'] == 'UJ'):
                    self.IE = self.executeUj(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1])  
            
                self.ID = self.decode(self.IF)
                self.fetch(pc_dict[self.PC])
                self.Cycles+=1
            if(self.Cycles == 3):
                print("-----------------------------------------------------------------------")
                print(self.IE)
                self.IM = self.IE['RegUpdate']
                if(self.IE['MemWrite'][0]):
                    if(self.IE['MemWrite'][1]=='w'):
                        if(self.IE['MemWrite'][4]=='byte'):
                            my_mem.write_byte(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                        if(self.IE['MemWrite'][4]=='word'):
                            my_mem.write_word(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                        if(self.IE['MemWrite'][4]=='half'):
                            my_mem.write_half(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                    else:
                        if(self.IE['MemWrite'][3]=='byte'):
                            retu = my_mem.ret_byte(self.IE['MemWrite'][2])
                            self.IM[2] = int(retu,2)
                        if(self.IE['MemWrite'][3]=='word'):
                            retu = my_mem.ret_word(self.IE['MemWrite'][2])
                            self.IM[2] = int(retu,2)
                        if(self.IE['MemWrite'][3]=='half'):
                            retu = my_mem.ret_half(self.IE['MemWrite'][2])
                            self.IM[2] = int(retu,2)
                        print("MEMORY ACCESSED")
                        
                        
                if(self.ID['Format']=='R'):
                    self.IE = self.executeR(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])
                if(self.ID['Format'] == 'I'):
                    self.IE = self.executeI(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
                if(self.ID['Format'] == 'IL'):
                    self.IE = self.executeIL(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'IJ'):
                    self.IE = self.executeIJ(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'IS'):
                    self.IE = self.executeIS(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
                if(self.ID['Format'] == 'SB'):
                    self.IE = self.executeSB(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'U'):
                    self.IE = self.executeU(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1]) 
                    print(self.IE)
                if(self.ID['Format'] == 'UJ'):
                    self.IE = self.executeUj(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1])  
                self.ID = self.decode(self.IF)
                self.fetch(pc_dict[self.PC])
                self.Cycles+=1
            if(self.Cycles >= 4):
                print("-----------------------------------------------------------------------")
                if(self.IM[0]):
                    my_reg.write_reg(self.IM[1],self.IM[2])
                print("REGISTER UPDATED")
                self.IM = self.IE['RegUpdate']
                if(self.IE['MemWrite'][0]):
                    if(self.IE['MemWrite'][1]=='w'):
                        if(self.IE['MemWrite'][4]=='byte'):
                            my_mem.write_byte(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                        if(self.IE['MemWrite'][4]=='word'):
                            my_mem.write_word(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                        if(self.IE['MemWrite'][4]=='half'):
                            my_mem.write_half(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                    else:
                        if(self.IE['MemWrite'][3]=='byte'):
                            retu = my_mem.ret_byte(self.IE['MemWrite'][2])
                            self.IM[2] = int(retu,2)
                        if(self.IE['MemWrite'][3]=='word'):
                            retu = my_mem.ret_word(self.IE['MemWrite'][2])
                            self.IM.append(int(retu,2))
                        if(self.IE['MemWrite'][3]=='half'):
                            retu = my_mem.ret_half(self.IE['MemWrite'][2])
                            self.IM[2] = int(retu,2)
                    print("MEMORY ACCESSED")
                        
                        
                if(self.ID['Format']=='R'):
                    self.IE = self.executeR(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])
                if(self.ID['Format'] == 'I'):
                    self.IE = self.executeI(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
                if(self.ID['Format'] == 'IL'):
                    self.IE = self.executeIL(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'IJ'):
                    self.IE = self.executeIJ(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'IS'):
                    self.IE = self.executeIS(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
                if(self.ID['Format'] == 'SB'):
                    self.IE = self.executeSB(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
                if(self.ID['Format'] == 'U'):
                    self.IE = self.executeU(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1]) 
                    print(self.IE)
                if(self.ID['Format'] == 'UJ'):
                    self.IE = self.executeUj(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1])  
                self.ID = self.decode(self.IF)
                self.fetch(pc_dict[self.PC])
                self.Cycles+=1
        
        print("-----------------------------------------------------------------------")
        if(self.IM[0]):
            my_reg.write_reg(self.IM[1],self.IM[2])
        print("REGISTER UPDATED")
        self.IM = self.IE['RegUpdate']
        if(self.IE['MemWrite'][0]):
            if(self.IE['MemWrite'][1]=='w'):
                if(self.IE['MemWrite'][4]=='byte'):
                    my_mem.write_byte(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                if(self.IE['MemWrite'][4]=='word'):
                    my_mem.write_word(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                if(self.IE['MemWrite'][4]=='half'):
                    my_mem.write_half(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
            else:
                if(self.IE['MemWrite'][3]=='byte'):
                    retu = my_mem.ret_byte(self.IE['MemWrite'][2])
                    self.IM[2] = int(retu,2)
                if(self.IE['MemWrite'][3]=='word'):
                    retu = my_mem.ret_word(self.IE['MemWrite'][2])
                    self.IM.append(int(retu,2))
                if(self.IE['MemWrite'][3]=='half'):
                    retu = my_mem.ret_half(self.IE['MemWrite'][2])
                    self.IM[2] = int(retu,2)
            print("MEMORY ACCESSED")
                
                
        if(self.ID['Format']=='R'):
            self.IE = self.executeR(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])
        if(self.ID['Format'] == 'I'):
            self.IE = self.executeI(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
        if(self.ID['Format'] == 'IL'):
            self.IE = self.executeIL(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
        if(self.ID['Format'] == 'IJ'):
            self.IE = self.executeIJ(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
        if(self.ID['Format'] == 'IS'):
            self.IE = self.executeIS(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
        if(self.ID['Format'] == 'SB'):
            self.IE = self.executeSB(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
        if(self.ID['Format'] == 'U'):
            self.IE = self.executeU(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1]) 
            print(self.IE)
        if(self.ID['Format'] == 'UJ'):
            self.IE = self.executeUj(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1])  
        self.ID = self.decode(self.IF)
        self.Cycles+=1
        print("-----------------------------------------------------------------------")
        if(self.IM[0]):
            my_reg.write_reg(self.IM[1],self.IM[2])
        print("REGISTER UPDATED")
        self.IM = self.IE['RegUpdate']
        if(self.IE['MemWrite'][0]):
            if(self.IE['MemWrite'][1]=='w'):
                if(self.IE['MemWrite'][4]=='byte'):
                    my_mem.write_byte(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                if(self.IE['MemWrite'][4]=='word'):
                    my_mem.write_word(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                if(self.IE['MemWrite'][4]=='half'):
                    my_mem.write_half(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
            else:
                if(self.IE['MemWrite'][3]=='byte'):
                    retu = my_mem.ret_byte(self.IE['MemWrite'][2])
                    self.IM[2] = int(retu,2)
                if(self.IE['MemWrite'][3]=='word'):
                    retu = my_mem.ret_word(self.IE['MemWrite'][2])
                    self.IM.append(int(retu,2))
                if(self.IE['MemWrite'][3]=='half'):
                    retu = my_mem.ret_half(self.IE['MemWrite'][2])
                    self.IM[2] = int(retu,2)
            print("MEMORY ACCESSED")
                
                
        if(self.ID['Format']=='R'):
            self.IE = self.executeR(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])
        if(self.ID['Format'] == 'I'):
            self.IE = self.executeI(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
        if(self.ID['Format'] == 'IL'):
            self.IE = self.executeIL(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
        if(self.ID['Format'] == 'IJ'):
            self.IE = self.executeIJ(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
        if(self.ID['Format'] == 'IS'):
            self.IE = self.executeIS(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2])   
        if(self.ID['Format'] == 'SB'):
            self.IE = self.executeSB(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1],self.ID['operands'][2]) 
        if(self.ID['Format'] == 'U'):
            self.IE = self.executeU(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1]) 
            print(self.IE)
        if(self.ID['Format'] == 'UJ'):
            self.IE = self.executeUj(self.ID['Instruction'],self.ID['operands'][0],self.ID['operands'][1])  
        self.Cycles+=1
        
        print("-----------------------------------------------------------------------")
        if(self.IM[0]):
            my_reg.write_reg(self.IM[1],self.IM[2])
        print("REGISTER UPDATED")
        self.IM = self.IE['RegUpdate']
        if(self.IE['MemWrite'][0]):
            if(self.IE['MemWrite'][1]=='w'):
                if(self.IE['MemWrite'][4]=='byte'):
                    my_mem.write_byte(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                if(self.IE['MemWrite'][4]=='word'):
                    my_mem.write_word(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
                if(self.IE['MemWrite'][4]=='half'):
                    my_mem.write_half(self.IE['MemWrite'][2],self.IE['MemWrite'][3])
            else:
                if(self.IE['MemWrite'][3]=='byte'):
                    retu = my_mem.ret_byte(self.IE['MemWrite'][2])
                    self.IM[2] = int(retu,2)
                if(self.IE['MemWrite'][3]=='word'):
                    retu = my_mem.ret_word(self.IE['MemWrite'][2])
                    self.IM.append(int(retu,2))
                if(self.IE['MemWrite'][3]=='half'):
                    retu = my_mem.ret_half(self.IE['MemWrite'][2])
                    self.IM[2] = int(retu,2)
            print("MEMORY ACCESSED")
        self.Cycles+=1
        print("-----------------------------------------------------------------------")
        if(self.IM[0]):
            my_reg.write_reg(self.IM[1],self.IM[2])
        print("REGISTER UPDATED")
        self.Cycles+=1   
                
    def fetch(self,mc_code):
        self.IF=mc_code
        self.PC_temp=self.PC
        self.PC+=4
        print("FETCH:Fetch instruction "+self.IF+" from address "+str(self.PC-4))
    
    def decode(self,Ins):
        out={}
        curr_bin_ins=bin(int(Ins[2:],16))[2:].zfill(32)   
        opcode=curr_bin_ins[25:32]
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
                    out['Format'] = 'R'
                    out['Instruction'] = 'SUB'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                else:
                    print("DECODE: Operation is SRA, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'SRA'
                    out['operands'] = [rs1,rs2,rd]
                    return out
            elif(fun7=="0000001"):
                if(fun3=="000"):
                    print("DECODE: Operation is MUL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'MUL'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="100"):
                    print("DECODE: Operation is DIV, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'DIV'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="110"):
                    print("DECODE: Operation is REM, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'REM'
                    out['operands'] = [rs1,rs2,rd]
                    return out
            elif(fun7=="0000000"):
                if(fun3=="000"):
                    print("DECODE: Operation is ADD, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'ADD'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="110"):
                    print("DECODE: Operation is OR, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'OR'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="101"):
                    print("DECODE: Operation is SRL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'SRL'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="100"):
                    print("DECODE: Operation is XOR, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'XOR'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="111"):
                    print("DECODE: Operation is AND, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'AND'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="001"):
                    print("DECODE: Operation is SLL, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'SLL'
                    out['operands'] = [rs1,rs2,rd]
                    return out
                elif(fun3=="010"):
                    print("DECODE: Operation is SLT, first operand R",int(rs1,2), " , Second operand R",int(rs2,2),", destination register R",int(rd,2))
                    print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                    out['Format'] = 'R'
                    out['Instruction'] = 'SLT'
                    out['operands'] = [rs1,rs2,rd]
                    return out
        elif(opcode=="0010011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is ADDI, first operand R",int(rs1,2), " , Second operand is Immediate field,destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                out['Format'] = 'I'
                out['Instruction'] = 'ADDI'
                out['operands'] = [rs1,imm,rd]
                return out
            if(fun3=="111"):
                print("DECODE: Operation is ANDI, first operand R",int(rs1,2), " , Second operand is Immediate field,destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                out['Format'] = 'I'
                out['Instruction'] = 'ANDI'
                out['operands'] = [rs1,imm,rd]
            if(fun3=="110"):
                print("DECODE: Operation is ORI, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                out['Format'] = 'I'
                out['Instruction'] = 'ORI'
                out['operands'] = [rs1,imm,rd] 

        elif(opcode=="0000011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            out['Format'] = 'IL'
            out['operands'] = [rs1,imm,rd]
            if(fun3=="000"):
                print("DECODE: Operation is LB, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                out['Instruction'] = 'LB'   
            # elif(fun3=="011"):
            #     print("DECODE: Operation is LD, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
            #     print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
            #     out['Instruction'] = 'LD'    
            elif(fun3=="001"):
                print("DECODE: Operation is LH, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                out['Instruction'] = 'LH'      
            elif(fun3=="010"):
                print("DECODE: Operation is LW, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                out['Instruction'] = 'LW'  
                                                
        elif(opcode=="1100111"):                                                
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:12]
            if(fun3=="000"):
                print("DECODE: Operation is JALR, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2))
                out['Format'] = 'IJ'
                out['Instruction'] = 'JALR'
                out['operands'] = [rs1,imm,rd] 
        elif(opcode=="0100011"):
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rd=curr_bin_ins[7:12]
            imm=curr_bin_ins[0:7]+curr_bin_ins[20:25]
            out['Format'] = 'IS'
            out['operands'] = [rs1,imm,rd] 
            if(fun3=="010"):
                print("DECODE: Operation is SW, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                out['Instruction'] = 'SW'
            # elif(fun3=="011"):    
            #     print("DECODE: Operation is SD, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
            #     print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
            #     out['Instruction'] = 'SD'
            elif(fun3=="000"):
                print("DECODE: Operation is SB, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                out['Instruction'] = 'SB'
            elif(fun3=="001"):
                print("DECODE: Operation is SH, first operand R",int(rs1,2), " , Second operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", The immediate value is ",int(imm,2) )
                out['Instruction'] = 'SH'
        elif(opcode=="1100011"):        
            fun3=curr_bin_ins[17:20]
            rs1=curr_bin_ins[12:17]
            rs2=curr_bin_ins[7:12]
            imm=curr_bin_ins[0:7]+curr_bin_ins[20:25]
            out['Format'] = 'SB'
            out['operands'] = [rs1,imm,rs2] 
            if(fun3=="000"):
                print("DECODE: Operation is BEQ, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                out['Instruction'] = 'BEQ'
            if(fun3=="001"):    
                print("DECODE: Operation is BNE, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                out['Instruction'] = 'BNE'
            if(fun3=="100"):    
                print("DECODE: Operation is BLT, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                out['Instruction'] = 'BLT'
            if(fun3=="101"):    
                print("DECODE: Operation is BGE, first operand R",int(rs1,2), " ,  second operand R",int(rs2,2))
                print("DECODE: Read registers R",int(rs1,2)," = ",my_reg.regVal(int(rs1,2)),", Second register R",int(rs2,2)," = ",my_reg.regVal(int(rs2,2)))
                out['Instruction'] = 'BGE'
    
        elif(opcode=="0010111" or opcode=="0110111"):
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:20]
            if(opcode=="0110111"): 
                print("DECODE: Operation is LUI, first operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: The immediate value is",int(imm,2))
                out['Format'] = 'U'
                out['Instruction'] = 'LUI'
                out['operands'] = [imm,rd]
            elif(opcode=="0010111"):
                print("DECODE: Operation is AUIPC, first operand is Immediate field, destination register R",int(rd,2))
                print("DECODE: The immediate value is",int(imm,2))
                out['Format'] = 'U'
                out['Instruction'] = 'AUIPC'
                out['operands'] = [imm,rd]
        elif(opcode=="1101111"):
            rd=curr_bin_ins[20:25]
            imm=curr_bin_ins[0:20]
            # print(imm)
            imm0=imm[0]
            imm1=imm[1:12]
            imm2=imm[12]
            imm3=imm[13:20]
            imm_=imm0+imm3+imm2+imm1
            # print(imm_)
            print("DECODE: Operation is JAL,the first operand is Immediate field, destination register R",int(rd,2))
            print("DECODE: The immediate value is",int(imm_,2))
            out['Format'] = 'UJ'
            out['Instruction'] = 'JAL'
            out['operands'] = [imm_,rd]
        return out    
    
    def executeUj(self,func,im,r):
        out = {}
        if(im[0]=='1'):
            val=-2**20+int(im,2)-1
        else:
            val=int(im,2) 
        out['MemWrite']= [False]
        out['RegUpdate']=[True]
        out['RegUpdate']+=[int(r,2),self.PC]
        self.PC=self.PC_temp+val 
        print("EXECUTED")
        return out        
                
    def executeR(self,func,r1,r2,r3):
        out={}
        out['MemWrite'] = [False]
        out['RegUpdate'] = [True]
        if(func=="ADD"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1+num2]
            print("EXECUTED")
            return out
        if(func=="SUB"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1-num2]
            print("EXECUTED")
            return out
        if(func=="MUL"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1*num2]
            print("EXECUTED")
            return out
        if(func=="DIV"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1/num2]
            print("EXECUTED")
            return out
        if(func=="SRA"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            xx=bin(num1)[2:]
            my_msb=xx[31]
            aa=str(num1>>num2)
            aa[0:num2]=my_msb
            out['RegUpdate']+=[int(r3,2),int(aa,2)]
            print("EXECUTED")
            return out
        if(func=="SRL"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1>>num2]
            print("EXECUTED")
            return out
        if(func=="AND"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1&num2]
            print("EXECUTED")
            return out    
        if(func=="XOR"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1^num2]
            print("EXECUTED")
            return out  
        if(func=="REM"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1%num2]
            print("EXECUTED")
            return out  
        if(func=="SLT"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            if(num1>num2):
                out['RegUpdate']+=[int(r3,2),0]
                print("EXECUTED")
                return out  
            else:
                out['RegUpdate']+=[int(r3,2),1]
                print("EXECUTED")
                return out            
        if(func=="SLL"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1<<num2]
            print("EXECUTED")
            return out  
        if(func=="OR"):
            num1=my_reg.regVal(int(r1,2))
            num2=my_reg.regVal(int(r2,2))
            out['RegUpdate']+=[int(r3,2),num1|num2]
            print("EXECUTED")
            return out                                   

    def executeI(self,func,r1,r2,r3):
        out={}
        out['MemWrite'] = [False]
        out['RegUpdate'] = [True]
        if(func=="ADDI"):
            num1=my_reg.regVal(int(r1,2))
            num2=int(r2,2)
            if(r2[0]=='1'):
                num2=-2**12+num2
            out['RegUpdate']+=[int(r3,2),num1+num2]
        if(func=="ANDI"):
            num1=my_reg.regVal(int(r1,2))
            num2=int(r2,2)
            if(r2[0]=='1'):
                num2=-2**12+num2
            out['RegUpdate']+=[int(r3,2),num1&num2]
        if(func=="ORI"):
            num1=my_reg.regVal(int(r1,2))
            num2=int(r2,2)
            if(r2[0]=='1'):
                num2=-2**12+num2
            out['RegUpdate']+=[int(r3,2),num1|num2]
        print("EXECUTED")
        return out     
    
    def executeU(self,func,im,r):
        out={}
        out['MemWrite'] = [False]
        out['RegUpdate'] = [True]
        if(func=="LUI"):
            im=im+"000000000000"
            im=int(im,2)
            out['RegUpdate']+=[int(r,2),im]
        else:
            im=im+"000000000000"
            im=int(im,2)
            im=im+self.PC_temp
            out['RegUpdate']+=[int(r,2),im]
        print("EXECUTED")
        return out                                                     

    def executeIS(self,func,r1,r2,r3):
        out={}
        out['MemWrite'] = [True]
        out['RegUpdate'] = [False]
        if(r2[0]=='1'):
            eff_address=my_reg.regVal(int(r1,2))-2**12+int(r2,2)
        else:    
            eff_address=my_reg.regVal(int(r1,2))+int(r2,2)
        if(func=="SB"):
            out['MemWrite']+=['w',eff_address,my_reg.regVal(int(r3,2)),'byte']
        elif(func=="SH"):
            out['MemWrite']+=['w',eff_address,my_reg.regVal(int(r3,2)),'half']
        elif(func=="SW"):
            out['MemWrite']+=['w',eff_address,my_reg.regVal(int(r3,2)),'word']
        print("EXECUTED")
        return out    

    def executeSB(self,func,r1,r2,r3):
        out={}
        out['MemWrite'] = [False]
        out['RegUpdate'] = [False]
        if(r2[0]=='1'):
            val=-2**12+int(r2,2)-1
        else:
            val=int(r2,2)    
        if(func=="BEQ"):
            if(my_reg.regVal(int(r1,2))==my_reg.regVal(int(r3,2))):
                self.PC=self.PC_temp+val
        elif(func=="BNE"):
            if(my_reg.regVal(int(r1,2))!=my_reg.regVal(int(r3,2))):
                self.PC=self.PC_temp+val
        elif(func=="BLT"):
            if(my_reg.regVal(int(r1,2))<my_reg.regVal(int(r3,2))):
                self.PC=self.PC_temp+val
        elif(func=="BGE"):
            if(my_reg.regVal(int(r1,2))>=my_reg.regVal(int(r3,2))):
                self.PC=self.PC_temp+val 
        print("EXECUTED")
        return out           

    def executeIL(self,func,r1,r2,r3):
        out={}
        out['MemWrite'] = [True]
        out['RegUpdate'] = [True]
        if(r2[0]=='1'):
            eff_address=my_reg.regVal(int(r1,2))-2**12+int(r2,2)
        else:    
            eff_address=my_reg.regVal(int(r1,2))+int(r2,2)
        if(func=="LB"):
            out['MemWrite']+=['r',eff_address,'byte']
            out['RegUpdate']+=[int(r3,2)]
        if(func=="LH"):
            out['MemWrite']+=['r',eff_address,'half']
            out['RegUpdate']+=[int(r3,2)]
        if(func=="LW"):
            out['MemWrite']+=['r',eff_address,'word']
            out['RegUpdate']+=[int(r3,2)]
        print("EXECUTED")
        return out  


    def executeIJ(self,func,r1,r2,r3):
        out={}
        out['MemWrite'] = [False]
        out['RegUpdate'] = [True]
        if(r2[0]=='1'):
            eff_address=my_reg.regVal(int(r1,2))-2**12+int(r2,2)
        else:    
            eff_address=my_reg.regVal(int(r1,2))+int(r2,2)  
        out['RegUpdate'].append(int(r3,2))  
        out['RegUpdate'].append(self.PC)     
        self.PC=eff_address
        print("EXECUTED")
        return out  
my_pipeline = pipelining()
my_pipeline.pipeline()  
print("--------------------------------------------------------------")
print("NO. of Cycles: ",my_pipeline.Cycles)  
print("------------------Registers------------------------------\n\n")
mr=my_reg.ret_reg()
for i in range(0,32):
    print("x"+str(i)+":"+str(mr[i]))
print("\n")
pr=my_mem.returnAll()
print("--------------------Memory-------------------------------\n\n")
for key in pr:
    print(hex(key),":"+pr[key]+"\n")
        
                
            
    
