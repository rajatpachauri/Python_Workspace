#for defining we don't use function name as the predefined function
def example():
    print('basic function')
    z = 3+9
    print(z)

example()

def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is ',num1)
    print('num2 is ',num2)
    print('answer is ',answer)
    
simple_addition(2, 3)

#if order of the arguments are not known
simple_addition(num2 = 4, num1 = 1)

#default functions parameters
  
# def simple(num1,num2):
#     pass

def simple(num1,num2 = 5):
    print(num1,num2)
    
def basic_window(width,height,font = 'TNR',
                 bgcolor='w',scrollbar=True):
    print(width,height,font,bgcolor,scrollbar)
    
    
basic_window(300,500)
    
simple(3)