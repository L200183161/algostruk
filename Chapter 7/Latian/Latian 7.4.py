##  exercise 7.4

import re

pola = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+'

e = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(pola, e)
print(cocok[0])


s = 'Alamatku sri@google.com serta joko@abc.com ok bro. atau don@email.com'

pola1 = r'[\w\.-]+@[\w\.-]+'
e1 = re.findall(pola1, s)
print(e1)

pola2 = r'([\w\.-]+)@([\w\.-]+)'
e2 = re.findall(pola2, s)
print(e2)
for tup in e2:
    print('user', tup[0], 'dengan host:', tup[1])


f = open('test.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()

p = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+'
strings = re.findall(p, teks)
print(strings)
