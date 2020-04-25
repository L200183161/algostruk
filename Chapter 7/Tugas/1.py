#Numero 1
import re
s='sebuah contoh kata:es teh!!'
cocok=re.findall(r'kata:\w*\s*\w*',s)
if cocok:
    print('nemu', cocok)
else:
    print('tidak nemu')
