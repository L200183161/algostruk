# exercise 7.2

import re

cocok1 = re.findall(r'eee','teeeh')

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil
if cocok1 :
    print('menemukan', cocok1) #'menemukan [kata:teh]' 
else :
    print('tidak menemukan')


cocok2 = re.findall(r'ehs','teeeh')

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil
if cocok2 :
    print('menemukan', cocok2) #'menemukan [kata:teh]' 
else :
    print('tidak menemukan')

cocok3 = re.findall(r'\d\d\d','t123 di 2019 bulan 02')

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil
if cocok3 :
    print('menemukan', cocok3) #'menemukan [kata:teh]' 
else :
    print('tidak menemukan')

cocok4 = re.findall(r'\w\w\w','@@a*bc#def*tghh!!')

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil
if cocok4 :
    print('menemukan', cocok4) #'menemukan [kata:teh]' 
else :
    print('tidak menemukan')

##cocok = re.findall(r'eee','teeeh')
##cocok = re.findall(r'ehs','teeeh')
##cocok = re.findall(r'\d\d\d','t123 di 2019 bulan 02')
##cocok = re.findall(r'\w\w\w','@@a*bc#def*tghh!!')
##
##if cocok :
##    print('menemukan', cocok) #'menemukan [kata:teh]' 
##else :
##    print('tidak menemukan')
    

