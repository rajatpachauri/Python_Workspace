book = {}
book['tom'] = {
    'name':'tom',
    'address':'1 red street, NY',
    'phone':989989898
    }

book['rajat'] = {
    'name':'rajat',
    'address':'1 egree street, NY',
    'phone':989989898
    }

import json
s = json.dumps(book)
f = open('exampleFile.txt','r')
t = f.read()
with open('exampleFile.txt','w') as f:
    f.write(s)
    
print(json.loads(t))