## exercise 7.3.1

import re

cocok1 = re.findall(r'te+','ghdteeeh')
if cocok1 :
    print('menemukan', cocok1) 
else :
    print('tidak menemukan')


cocok2 = re.findall(r'e+','teeheeee')
if cocok2 :
    print('menemukan', cocok2)
else :
    print('tidak menemukan')


polanya = r'\d\s*\d\s*\d'

cocok3 = re.findall(polanya, 'xx1 2  3xx')
if cocok3 :
    print('menemukan', cocok3)
else :
    print('tidak menemukan')


cocok4 = re.findall(polanya, 'xx12  3xx')
if cocok4 :
    print('menemukan', cocok4)
else :
    print('tidak menemukan')


cocok5 = re.findall(polanya, 'xx123xx')
if cocok5 :
    print('menemukan', cocok5)
else :
    print('tidak menemukan')


cocok6 = re.findall(r'^k\w+', 'mejakursi')
if cocok6 :
    print('menemukan', cocok6)
else :
    print('tidak menemukan')


cocok7 = re.findall(r'k[\w\s]+', 'mejakursi tamu saya')
if cocok7 :
    print('menemukan', cocok7)
else :
    print('tidak menemukan')


# mengekstrak email
e = 'Alamatku adalah dita-b@google.com mas'
cocok8 = re.findall(r'\w+@\w+', e)
print(cocok8[0])


## exercise 7.3.2

cocok9 = re.findall(r'[\w.-]+@[\w.-]+', e)
print(cocok9[0])
