class registers:
    def __init__(self):
        self.reg=[0,0,2147483632,268435456,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def regVal(self,num) :
        return self.reg[num]  
    
    def write_reg(self,num,val):
        if(num==0):
            return  
        else:
            self.reg[num]=val
            
    def ret_reg(self):
        return self.reg
