class MhsTIF(object):
    def __init__(self,nama,nim,tinggal,us):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.us = us

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

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
def partisi(A, awal, akhir):
    hasil = 0
    pivot, pidx = median_dari_tiga(A, awal, akhir)
    A[awal], A[pidx] = A[pidx], A[awal]
    i = awal + 1
    for j in range(awal + 1, akhir, 1):
        hasil += 1
        if (A[j] < pivot):
            A[i], A[j] = A[j], A[i]
            i += 1
    A[awal], A[i - 1] = A[i - 1], A[awal]
    return i - 1, hasil


def median_dari_tiga(A, awal, akhir):
    tengah = (awal + akhir - 1) // 2
    a = A[awal]
    b = A[tengah]
    c = A[akhir - 1]
    if a <= b <= c:
        return b, tengah
    if c <= b <= a:
        return b, tengah
    if a <= c <= b:
        return c, akhir - 1
    if b <= c <= a:
        return c, akhir - 1
    return a, awal


def quickSortBantu(A, awal, akhir):
    hasil = 0
    if awal < akhir:
        titikBelah, hasil = partisi(A, awal, akhir)
        hasil += quickSortBantu(A, awal, titikBelah)
        hasil += quickSortBantu(A, titikBelah + 1, akhir)
    return hasil


def quickSort(A):
    quickSortBantu(A, 0, len(A))


def convert(arr, obj):
    hasil = []
    for x in range(len(arr)):
        for i in range(len(arr)):
            if arr[x] == obj[i].nim:
                hasil.append(obj[i])
    return hasil


A = []
for x in Daftar:
    A.append(x.nim)

print("QUICK SORT v2 BY NIM")
quickSort(A)
for i in convert(A, Daftar):
    print("[", i.nama, i.nim, i.tinggal, i.us, "]")


