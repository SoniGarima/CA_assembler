class memory:
    def __init__(self):
        self.memory = {}
    
    def ret_word(self,address):
        ret_ = ""
        for i in range(4):
            if address+i in self.memory:
                ret_ = ret_+self.memory[address+i]
            else:
                ret_ = "00000000" + ret_
            return ret_    

    def ret_byte(self,address):
        if address in self.memory:
            return bin(self.memory[address])[2:].zfill(8)
        else:
            return "00000000"

    def ret_db(self, address):
        ret_ = ""
        for i in range(8):
            if address+i in self.memory:
                ret_ = ret_+self.memory[address+i]
            else:
                ret_ = "00000000" + ret_
        return ret_        
                
    def ret_half(self,address):
        ret_ = ""
        for i in range(2):
            if address+i in self.memory:
                ret_ = ret_+self.memory[address+i]
            else:
                ret_ = "00000000" + ret_
        return ret_        

    def ret_asciiz(self,address):
        if address in self.memory:
            return self.memory[address]
        else:
            return "00000000" 
    
    def write_word(self,address,value):        
        value = str(bin(int(str(value),16)))[2:].zfill(32)
        b3 = value[0:8]
        b2 = value[8:16]
        b1 = value[16:24]
        b0 = value[24:32]
        self.memory[address] = b0
        self.memory[address+1] = b1
        self.memory[address+2] = b2
        self.memory[address+3] = b3

    def write_byte(self,address,value):
        value = str(bin(int(str(value),16)))[2:].zfill(8)
        self.memory[address] = value

    def write_db(self,address,value):
        value = str(bin(int(str(value),16)))[2:].zfill(64)
        self.memory[address+7] = value[56:64]
        self.memory[address+6] = value[48:56]
        self.memory[address+5] = value[40:48]
        self.memory[address+4] = value[32:40]
        self.memory[address+3] = value[24:32]
        self.memory[address+2] = value[16:24]
        self.memory[address+1] = value[8:16]
        self.memory[address] = value[0:8]

    def write_asciiz(self,address,value):
        self.memory[address] = value
        
    def write_half(self,address,value):        
        value = str(bin(int(str(value),16)))[2:].zfill(32)
        self.memory[address] = value[0:8]
        self.memory[address+1] = value[8:16]  
        
    def printall(self):
        print(self.memory)

    def returnAll(self):
        return self.memory

