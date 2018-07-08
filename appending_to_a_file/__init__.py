appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close() 


#read from a file
f = open('exampleFile.txt',"r")
readMe = open('exampleFile.txt','r').read()
for line in readMe:
    print(line)
    
    
# for line in f:
#     print(f)

# for reading to memory or excel sheet
# readMe = open('exampleFile.txt','r').readlines()
# print(readMe)

# for not using .close we open the file with with format
with open('exampleFile.txt','r') as f:
    print(f.read())

print(f.closed)









