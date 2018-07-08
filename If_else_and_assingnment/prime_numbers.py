for n in range(1,101):
    if n < 2:
       status = False
    else:
       status = True
    if n > 2:
       for i in range(2,n):
            if n % i == 0:
                status = False
    
    if status:
            print(n, '', sep=',', end='')
    