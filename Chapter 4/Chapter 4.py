import random
class MhsTIF(object):
    def __init__(self, nama, umur, kota, us):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = self.nama + ', umur' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilUmur(self):
        return self.umur
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Juuuh', 10, 'Rembang', 250000)
c1 = MhsTIF('Kon', 14, 'Solo', 210000)
c2 = MhsTIF('Arek', 12, 'Madura', 450000)
c3 = MhsTIF('Gatile', 21, 'Cimahi', 150000)
c4 = MhsTIF('Temen', 20, 'Bogoy', 200000)
c5 = MhsTIF('Kon', 30, 'Jakarta', 450000)
c6 = MhsTIF('Jero', 11, 'Wuhan', 650000)
c7 = MhsTIF('Omah', 13, 'Surabaya', 2750000)
c8 = MhsTIF('Dolan', 16, 'Cilacap', 250000)
c9 = MhsTIF('Klayapan', 6, 'Semarang', 165000)
c10 = MhsTIF('Ae.. Mikir Cok', 5, 'Bandung', 450000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#Numero 1
def cariKota(target):
    z = []
    for i in Daftar:
        if i.kotaTinggal == target:
            hasil = Daftar.index(i)
            z.append(hasil)
    return z
print(cariKota("Rembang"))
#Numero 2
def cariTerkecil(Daftar):
    n = len(Daftar)
    terkecil = Daftar[0]
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil.uangSaku:
            terkecil = Daftar[i]

    return terkecil
print(cariTerkecil(Daftar))

#Numero 3
def cariTerkecil1(Daftar):
    n = len(Daftar)
    terkecil = [Daftar[0]]
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil[0].uangSaku:
            terkecil = [Daftar[i]]
        elif Daftar[i].uangSaku == terkecil[0].uangSaku:
            terkecil.append(Daftar[i])
    return terkecil
print(cariTerkecil1(Daftar))
#Numero 4
def cariDaftarUangSakuKurang(kumpulan):
    b = []
    for i in kumpulan:
        if i.uangSaku < 250000:
            b.append(kumpulan.index(i))
    return b
print(cariDaftarUangSakuKurang(Daftar))
#Numero 5
def cariLinkedList(head, target):
    temp = head
    while temp.data != None:
        if temp.data == target:
            return temp
    return -1

#Numero 6
List = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
def binSe(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1
    data = []

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low <= high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid -1
        #ataukah targetnya di sebelah kanannya?
        else :
            low = mid +1
        #Jika urutannya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False

#Numero 7

def binSearch(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1
    data = []

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low != high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            break
        #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid -1
        #ataukah targetnya di sebelah kanannya?
        else :
            low = mid +1
    for i in range (low, high):
        if target == kumpulan[i]:
            data.append(i)
    return data

a = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]

#Numero 8


def tebakanAngka():
    print("""Permainan tebak angka.
    Saya menyimpan sebuah angka bulat antara 1 sampai 1000. Coba Tebak!""")
    a = random.randint(1, 1001)
    for i in range (10):
        b = int(input("Masukkan tebakkan ke-{}:>".format(i+1)))
        if b == a:
            print ("Ya. Anda benar.")
        elif b > a:
            if i == 10:
                print ("Itu terlalu besar. Coba lagi ")
            else:
                print ("Itu terlalu besar. Coba lagi",a)
        else:
            if i < 10:
                print ("Itu terlalu kecil. Coba Lagi")
            else:
                print ("Itu terlalu kecil. Coba lagi",a)

"""
untuk mencari berapa jumlah tebakan yang digunakan pada tebak angka
yaitu dengan menggunakan Logaritma basis 2 (log2(n))
misalkan :
        // apabila terdapat elemen array berjumlah 100 maka memiliki maksimal 7 kali tebakan
           itu dikarenakan log2(100) = 6.643856189774725 sehingga diperoleh angka 7
           dapat juga diperoleh dari log2(128) = 7 karena yang mendekati dari 100 adalah 128
       //  apabila terdapat elemen array berjumlah 1000 maka memiliki maksimal 10 kali tebakan
           itu dikarenakan log2(1000) = 9.965784284662087 sehingga diperoleh angka 10
           dapat juga diperoleh dari log2(1024) = 10 karena yang mendekati dari 1000 adalah 128
"""
tebakanAngka()