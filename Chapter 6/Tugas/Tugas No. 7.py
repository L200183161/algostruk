from time import time as detak
from random import shuffle as kocok
import time


## Merge Sort 1
def mergeSort(A):
    ##print("Membelah      ",A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSort(separuhkiri)
        mergeSort(separuhkanan)

        i = 0;
        j = 0;
        k = 0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k = k + 1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k = k + 1

        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k = k + 1
    ##print("Menggabungkan",A)


## Quick Sort 1
def partisi(A, awal, akhir):
    nilaipivot = A[awal]

    penandakiri = awal + 1
    penandakanan = akhir

    selesai = False
    while not selesai:

        while penandakiri <= penandakanan and A[penandakiri] <= nilaipivot:
            penandakiri = penandakiri + 1

        while penandakanan >= penandakiri and A[penandakanan] >= nilaipivot:
            penandakanan = penandakanan - 1

        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp

    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan


def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)


def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)


## Merge Sort 2
def mergeSort2(A, awal, akhir):
    mid = (awal + akhir) // 2
    if awal < akhir:
        mergeSort2(A, awal, mid)
        mergeSort2(A, mid + 1, akhir)

    a, f, l = 0, awal, mid + 1
    tmp = [None] * (akhir - awal + 1)
    while f <= mid and l <= akhir:
        if A[f] < A[l]:
            tmp[a] = A[f]
            f += 1
        else:
            tmp[a] = A[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = A[f:mid + 1]

    if l <= akhir:
        tmp[a:] = A[l:akhir + 1]

    a = 0
    while awal <= akhir:
        A[awal] = tmp[a]
        awal += 1
        a += 1


def mergeSortNew(A):
    mergeSort2(A, 0, len(A) - 1)


# Quick Sort 3
def partisiNew(A, awal, akhir):
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


def quickSortBantuNew(A, awal, akhir):
    hasil = 0
    if awal < akhir:
        titikBelah, hasil = partisiNew(A, awal, akhir)
        hasil += quickSortBantuNew(A, awal, titikBelah)
        hasil += quickSortBantuNew(A, titikBelah + 1, akhir)
    return hasil


def quickSortNew(A):
    quickSortBantuNew(A, 0, len(A))


k = [[i] for i in range(1, 6001)]
kocok(k)
u_mrg = k[:]
u_qck = k[:]
u_mrgNew = k[:]
u_qckNew = k[:]

aw = detak();
mergeSort(u_mrg);
ak = detak();
print("merge: %g detik" % (ak - aw));
aw = detak();
quickSort(u_qck);
ak = detak();
print("quick: %g detik" % (ak - aw));
aw = detak();
mergeSortNew(u_mrgNew);
ak = detak();
print("merge v2: %g detik" % (ak - aw));
aw = detak();
quickSortNew(u_qckNew);
ak = detak();
print("quick v2: %g detik" % (ak - aw));
