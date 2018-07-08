num = int(input('Enter the number for the table: '))
for i in range(1,11):
    print('{} x {} = {}'.format(num,i,(num*i)))
    
for i in range(0,6):
    print('*'*i)
    
for i  in range(0,6):
    print(' '*(6-i)+'*'*(2*i-1))
    
    
#febonacci series
a = 0
b = 1
print(a,end = ', ')
for i in range(1 ,10):
    if i == 9:
        str = ' '
    else: str = ', '
    print(b,end = str)
    c = b
#     b = a+b
#     a = c
    b,a = a+b,c
    
    
