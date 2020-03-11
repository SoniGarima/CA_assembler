class registers:
    def __init__(self):
        self.reg=[]
        for i in range(0,32):
            reg[i]=0
        reg[2]=2147483632
        reg[3]=268435456
    def regVal(self,bin_str) :
        return self.reg[int(bin_str,2)]  
    
    def write_reg(self,bin_str,val):
        if(bin_str=="00000"):
            return  
        else:
            self.reg[int(bin_str,2)]=val
            
    def ret_reg(self):
        return self.registers
