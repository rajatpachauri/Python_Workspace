x = input("enter number1: ")
y = input("enter number2: ")
try:
    z = x/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z = None
except Exception as e:
    print('exception type:',type(e).__name__)
    z = None
print("Division is: ",z)


#how to raise an exception and create your own exception
class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception: ",self.msg)
        
        
try:
    raise Accident('crash between two cars')
except Accident as e:
    e.print_exception()
finally:
    print("cleaning")   
    






        
    