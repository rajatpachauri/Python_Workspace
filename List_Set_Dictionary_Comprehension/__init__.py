numbers = [1,2,3,4,5,6,7]
even = []
for i in numbers:
    if(i%2==0):
        even.append(i)
        
print(even)

#list comprehension
even = [i for i in numbers if i%2==0]
print(even)


set1  = set([1,2,3,2,4,5,6,8])
print(set1)
#set comprehension
even1 = {i for i in set1 if i%2==0}

print(even1)

#Dictionary comprehension
cities = ["Mumbai","new York","Paris"]
countries = ["India","USA","England"]
z = zip(cities,countries)
print(z)
for a in z:
    print(a)
    
d = {city:country for city,country in zip(cities, countries)}
print(d)