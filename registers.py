class registers:
    def __init__(self):
        self.reg=[]
        for i in range(0,32):
            reg[i]=0
        reg[2]=2147483632
        reg[3]=268435456
    def regVal(self,num) :
        return self.reg[num]  
    
    def write_reg(self,num,val):
        if(num==0):
            return  
        else:
            self.reg[num]=val
            
    def ret_reg(self):
        return self.registers
