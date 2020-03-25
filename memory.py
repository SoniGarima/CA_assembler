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
            return self.memory[address]
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
        if(int(value)<0):
            h3 = str(bin(int(value)))[3:].zfill(32)  
            k3=int(h3,2)
            k3=2**32-k3; 
            k3=str(k3)    
            value=str(bin(int(k3,10))[2:].zfill(32)) 
            
        else:         
            value = str(bin(int(value)))[2:].zfill(32)
        b3 = value[0:8]
        b2 = value[8:16]
        b1 = value[16:24]
        b0 = value[24:32]
        self.memory[address] = b0
        self.memory[address+1] = b1
        self.memory[address+2] = b2
        self.memory[address+3] = b3

    def write_byte(self,address,value):
        if(int(value)<0):
            h3 = str(bin(int(value)))[3:].zfill(8)  
            k3=int(h3,2)
            k3=2**32-k3; 
            k3=str(k3)    
            value=str(bin(int(k3,10))[2:].zfill(8)) 
        else:    
            value = str(bin(int(value)))[2:].zfill(8)
        self.memory[address] = value

    def write_db(self,address,value):
        if(int(value)<0):
            h3 = str(bin(int(value)))[3:].zfill(64)  
            k3=int(h3,2)
            k3=2**32-k3; 
            k3=str(k3)    
            value=str(bin(int(k3,10))[2:].zfill(64)) 
        else:
            value = str(bin(int(value)))[2:].zfill(64)
        self.memory[address+7] = value[56:64]
        self.memory[address+6] = value[48:56]
        self.memory[address+5] = value[40:48]
        self.memory[address+4] = value[32:40]
        self.memory[address+3] = value[24:32]
        self.memory[address+2] = value[16:24]
        self.memory[address+1] = value[8:16]
        self.memory[address] = value[0:8]

    def write_asciiz(self,address,value):
        value = str(bin(int(str(ord(value)))))[2:].zfill(8)
        self.memory[address] = value
        
    def write_half(self,address,value): 
        if(int(value)<0):
            h3 = str(bin(int(value)))[3:].zfill(16)  
            k3=int(h3,2)
            k3=2**32-k3; 
            k3=str(k3)    
            value=str(bin(int(k3,10))[2:].zfill(16))  
        else:    
            value = str(bin(int(value)))[2:].zfill(16)
        self.memory[address] = value[0:8]
        self.memory[address+1] = value[8:16]  
        
    def printall(self):
        print(self.memory)

    def returnAll(self):
        return self.memory

