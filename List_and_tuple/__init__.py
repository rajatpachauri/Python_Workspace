# tuple

x = 5,6,2,6
# x = (4,7,6,3)
z = range(4)

print(x[-1])
# list
y = [5,6,3,4]

def example():
    return 1,3,4,5

# z[0],z[1],z[2],z[3] = example() generate error

a,b,c,d = example()
# print(example()) this will print the variable returned by function

print(a,b,c,d)