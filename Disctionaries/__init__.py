# unordered
exDict = {'jack':15, 'Bob':22, 'Alice':12, 'kelvin':17}

print(exDict)

print(exDict['jack'])

exDict['tim'] = 14

print(exDict)

exDict['tim'] = 15

print(exDict)

del exDict['tim']

print(exDict)

exDict1 = {'jack':[15,'blonde'], 'Bob':22, 'Alice':12, 'kelvin':17}

print(exDict1)
print(exDict1['jack'][0])