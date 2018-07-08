# classes is somewhat simlar to modules
# way of binding attributes

class calculator:
    
    def __init__(self):
        pass
    
    def addition(x,y):
        added = x+y
        print(added)
        
    def subtraction(x,y):
        sub = x-y
        print(sub)
        
    def multiplication(a,b):
        mul = a*b
        print(mul)
        
    def division(x,y):
        div = x/y
        print(div)
        
calculator.multiplication(3,5)
calculator.subtraction(3,4)
calculator.division(3,4)