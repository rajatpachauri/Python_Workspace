# comma(delimiter) separated variable
import csv

with open('examplecsv.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
#     print(readCSV)
    
    dates = []
    colors = []
    for row in readCSV:
#         print(row)
#         print(row[1])
        color = row[2]
        date = row[3]
        colors.append(color)
        dates.append(date)

print(colors)
print(dates)

# try to use the try and except block as less as possible

try:
    whatcolor = input("what color?  ")
    colidx = colors.index(whatcolor.lower(),)
    print(dates[colidx])
    
except NameError as e:
    print('color not existed ')

except ValueError as v:
    print('value error existed')
    
except Exception as e:
    print(e)

print('continuing')



