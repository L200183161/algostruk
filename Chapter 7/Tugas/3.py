# Numero 3

import re

z = open('indonesia.txt', 'r', encoding = 'latin1')
teks = z.read()
z.close()

pola = r'di\s\w+'
string = re.findall(pola, teks)
print(string)
