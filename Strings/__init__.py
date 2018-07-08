firstName = input("Enter first name : ")
lastName = input("Enter last name : ")

address = input("कृपया अपना पता डाले : ")

print("Welcome".center(150))

print("Hello",firstName.lower(),lastName.lower())

print("Hello",firstName.replace(firstName,'Virat'), lastName.replace(lastName,'Kohli'))

# UTF-8 - Universal Text Format
# Internationalization ( I18N )
print("हेल्लो",firstName.encode('UTF-8'))
