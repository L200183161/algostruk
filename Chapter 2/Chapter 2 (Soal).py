from datetime import date
# Numero Satu
class Pesan(object):

    def __init__(self, kata):
        self.kata = kata

    def apakahTerkandung(self, ok):
        if ok in self.kata:
            return True
        else:
            return False

    def hitungKonsonan(self):
        v = "aiueoAIUEO"
        h = 0
        for kon in self.kata:
            if kon not in self.kata:
                h +=1
            return h

    def hitungVokal(self):
        v = "aiueoAIUEO"
        h = 0
        for kon in self.kata:
            if kon in self.kata:
                h +=1
            return h

# Numero Dua dan Tiga
class mahasiswa(object):
    """Class mahasiswa yang dibangun dari class manusia"""
    def __init__(self, nama, NIM, kota,us,kuliah):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []
        self.kuliah = kuliah

    def __str__(self):
        s = self.nama + ", NIM " + str(self.NIM) \
            + ". Tinggal di "+ self.kotaTinggal \
            + ". Uang Saku Rp. " + str(self.uangSaku) \
            + " tiap bulannya. " + self.kuliah +" Kuliahnya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode "makannya" class Manusia
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = "kenyang"
#     a.
    def ambilKotaTinggal(self):
        return self.kotaTinggal
#     b.
    def perbaruiKotaTinggal(self,kot):
        self.kotaTinggal = kot
#     c.
    def tambahUangSaku(self, tambahSaku):
        self.uangSaku += tambahSaku
#     Nomer 4.
    def ListKuliah(self):
        return self.listKuliah
    def ambilKuliah(self, tambahKuliah):
        self.listKuliah.append(tambahKuliah)
#   Nomer 5
    def hapusListKuliah(self, hapusKuliah):
        for i in self.listKuliah:
            if hapusKuliah in self.listKuliah:
                self.listKuliah.remove(hapusKuliah)
            else:
                print("Im sorry your subject doesnt appear in this list")

# #     Nomer Tiga
# inp1 = input("Nama Anda pliss..... : ")
# inp2 = input("NIM Anda plis....... : ")
# inp3 = input("Your Address please..: ")
# inp4 = input("Your Monthly money please... : ")
# hasil = mahasiswa(inp1,inp2,inp3,inp4)
# print(hasil)

# m = mahasiswa("Donny",200183161,"Rembang",150000)

# Nomer 6
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'

    def __ini__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print('Salam, namaku', self.nama)

    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'

    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'

    def mengalikanDenganDua(self, n):
        return n * 2


class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = NIS
        self.umur = umur
        self.uangSaku = us

    def __str__(self):
        s = self.nama + ', NIS ' + str(self.nis) \
            + '. Berumur ' + str(self.umur) \
            + '. Uang saku Rp. ' + str(self.uangSaku) \
            + ' tiap harinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIS(self):
        return self.nis
    def ambilUmur(self):
        return self.umur
    def ambilUangSaku(self):
        return self.uangSaku
    def tahunLahir(self):
        now = date.today().year
        tahun = now - self.umur
        return tahun

Siswa = SiswaSMA("Rizal",8594,20,15000)

# Nomer 7
class MhsTIF(mahasiswa):
    def whereKuliah(self):
        return self.kuliah

coba = MhsTIF("Donny",161,"Rembang",10000,"UMS") #
coba.ambilKuliah("Informatika") # from class Mahasiswa
coba.listKuliah # from class Mahasiswa
coba.whereKuliah() #from class MhsTIF


