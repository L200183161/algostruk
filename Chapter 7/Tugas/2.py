#Numero 2
import re

f = open('indonesia.txt', 'r', encoding='latin1')
teks=f.read()
f.close()
c=r'di\w+'
strings1 = re.findall(c,teks)
print(strings1)
