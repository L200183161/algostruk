from math import sqrt as sq
from random import randint
def cetakSiku(x):
    for i in range (x):
        print ("*"*i)

def gambarlahPersegiEmpat(x,y):
    print("@"*y)
    for i in range(0,x-2):
        print("@"+" "*(y-2)+"@")
    print("@"*y)

def jumlahHurufVokal(x):
    h = 0
    v = "aiueoAIUEO"
    for i in x:
        if i in v:
            h = h+1
    return (len(x),h)

def jumlahHurufKonsonan(x):
    h = 0
    k = "aiueoAIUEO"
    for i in x:
        if i not in k:
            h = h+1
    return (len(x),h)

def rerata(x):
    a = []
    for i in x:
        a.append(i)
    c = sum(a)
    return int((c/int(len(x))))

def varians(x):
    a = []
    for i in x:
        a.append(i)
    c = sum(a)
    d = int((c/int(len(x))))
    e = int(sum([((x-d)**2) for x in x]) / len(x))
    return int(e)

def standardDeviation(x):
    a = []
    for i in x:
        a.append(i)
    c = sum(a)
    d = int((c/int(len(x))))
    e = int(sum([((x - d) ** 2) for x in x]) / len(x))
    f = str(e**0.5)
    return str(f)

def apakahPrima(n):
   n = int(n)
   assert n>=0
   primaKecil = [2,3,5,7,11]
   bukanPrKecil = [0,1,4,6,8,9,10]
   if n in primaKecil:
       return True
   elif n in bukanPrKecil:
       return False
   else:
       for i in range(2,int(sq(n))+1):
           if n%1 == 0:
               return True
           else:
               return False

def cekPrime():
    for num in range(2,1001):
        if num > 1:
            for i in range (2, num):
                if (num % i == 0):
                    break
            else:
                print (num)

def factorPrime(x):
    a = []
    if x > 1:
        i = 2
        while x % i != 0:
            i += 1
        a.append(i)
        a.extend(factorPrime(x/i))
    return a

def apakahTerkandung(x, y):
    for k in x:
        if k in y:
            return False
        else:
            return True

def kelipatan3(x,y):
    for i in range (x,y+1):
        if (i%3) == 0 and (i%5) == 0:
            print ("Python UMS")
        elif (i%3) == 0:
            print ("Python")
        elif (i%5) == 0:
            print ("UMS")
        else:
            print(i)

def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if D<0:
        hasil="Determinannya negatif. Persamaan tidak mempunyai akar real."
    else:
        x1 = (-b + sq(D))/(2*a)
        x2 = (-b - sq(D))/(2*a)
        hasil=(x1,x2)
    return str(hasil)

def apakahKabisat(h):
    if h%4==0:
        if h%100==0:
            if h%400==0:
                h=str(h)
                print (h+" tahun kabisat")
            else:
                h=str(h)
                print(h+" bukan tahun kabisat")
        else:
            h=str(h)
            print(h+" tahun kabisat")
    else:
        h=str(h)
        print(h+" bukan tahun kabisat")

def tebakanAngka():
    print("""Permainan tebak angka.
    Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba Tebak!""")
    a = randint(1, 100)
    for i in range (3):
        b = int(input("Masukkan tebakkan ke-{}:>".format(i+1)))
        if b == a:
            print ("Ya. Anda benar.")
        elif b > a:
            if i >= 2:
                print ("Itu terlalu besar. Kesempatan habis. Nilainya adalah",a)
            else:
                print ("Itu terlalu besar. Coba lagi")
        else:
            if i >= 2:
                print ("Itu terlalu kecil. Kesempatan habis. Nilainya adalah",a)
            else:
                print ("Itu terlalu kecil. Coba lagi")


def katakan(angka):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    for x in angka[::-1]:
        seribu = False
        if idx == 2 and x[-1]!="0":
            if int(x)< 2 :
                katakan.append("seribu")
                seribu = True
            else:
                katakan.append("ribu")
        if idx == 3 and x[-1]!="0":
            katakan.append("juta")
        if seribu == False:
            if int(x[-2:])<20 and int(x[-2:])>0:
                katakan.append(satuan[int(x[-2:])-1])
            elif int(x[-2:])>0:
                if int(x[-1])!=0:
                    katakan.append(satuan[int(x[-1])-1])
                if int(x[-2]) != 0:
                    katakan.append(satuan[int(x[-2])-1]+" puluh")
        if int(x[0]) > 2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            katakan.append("seratus")
        idx+=1
    return " ".join(katakan[::-1])

def formatRupiah(n):
    x = '{:,}'.format(n).replace(',', '.')
    return "Rp " + x

# #Numero Uno (1)
# x = int(input("Masukin sikunya gan : "))
# res = cetakSiku(x)
#
# #Numero Due (2)
# x=int(input("Enter the first side of the square : "))
# y=int(input("Enter the second side of the square : "))
# hasil = gambarlahPersegiEmpat(x,y)
#
# #Numero Tre (3)
# print(jumlahHurufVokal("Surakarta"))
# print(jumlahHurufKonsonan("Surakarta"))
#
# #Numero Quattro (4)
# rerata([1,2,3,4,5])
# Varianssss = str(varians([1,2,3,4,5]))
# print("The Variance of this product :" + str(Varianssss))
# sd = str(standardDeviation([1,2,3,4,5]))
# print("The Standard of deviation of this product : " + str(sd))
#
# #Numero Cinque (5)
# print(apakahPrima(13))
#
# #Numero Sei (6)
# # cekPrime()
#
# #Numero Sette (7)
# print(factorPrime(15))

# #Numero Otto (8)
# x = "Surakarta"
# y = "Cok Kon"
# print(apakahTerkandung(x,y))

# #Numero Nove (9)
# kelipatan3(1,100)

# #Numero Dieci (10)
# print(selesaikanABC(1,4,2))

# #Numero Undici (11)
# apakahKabisat(1900)

# #Numero Dodici (12)
# tebakanAngka()

# #Numero Tredici (13)
# print(katakan(142342))

# #Numero Quattordici (14)
# print(formatRupiah(15000))

# Collected in the internet by Donny (not all sigh :3)