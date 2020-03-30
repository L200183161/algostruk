class MhsTIF(object):
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = str(self.NIM) + " " + self.nama + " " + self.kotaTinggal + " " + str(self.uangSaku)
        return x
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.NIM
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 2400000)
c1 = MhsTIF('Budi', 51, 'Seragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#Numero 1
def mhsSort(A):
    n= len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos>0 and nilai.NIM<A[pos-1].NIM:
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos] = nilai

mhsSort(Daftar)
print('\n'.join(map(str, Daftar)))

#Numero 2
A=[1,3,5,7,9]
B=[2,4,8,10,12]

def comb(a,b):
    c=a+b
    n=len(c)
    for i in range(1,n):
        nilai = c[i]
        pos = i
        while pos>0 and nilai<c[pos-1]:
            c[pos]=c[pos-1]
            pos=pos-1
        c[pos] = nilai
    print(c)

comb(A,B)
