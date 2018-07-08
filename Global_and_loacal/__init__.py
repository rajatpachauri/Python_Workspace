x = 6

def example():
    x = 5
    print(x)
    x += 5
    print(x)
    
def example2():
    global x
    print(x)
    print(x+6)
#     the line written blow will give error
#     x += 6
#     global x
    print(x)
    x+=5
    print(x)
    
# in the companies the idea of using global keyword is omitted by instead assinging that variale to another variable and perform the required computation
    
    
def example3():
    globx = x
    print(globx)
    globx += 5
    print(globx)
    
    
    
example()
example2()
example3()
print(x)