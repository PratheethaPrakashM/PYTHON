class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        return self.a
    
    def sub(self):
        return self.a
    
    def mul(self):
        return self.a * self
    
    def div(self):
        if self.b==0:
            return"not possible"  
               
        return self.a//self.b
    
calc=calculator()
print(calc.add(2,3)) 
print(calc.sub(5,3))
print(calc.mul(5,4))
print(calc.div(5,2))
