class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi**2

class Segitiga(BangunDatar):
    def __init__(self,alas,tinggi) :
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return self.alas * self.tinggi / 2

class Lingkaran(BangunDatar):
    def __init__(self,jari2):
        self.phi = 22/7
        self.jari2 = jari2

    def luas(self):
        return self.phi * (self.jari2**2)
    

def menu_bagundatar():
    print("MENU BAGUN_DATAR".center (40, ' '))
    daftar = ['1.Persegi','2.Segitiga','3.Lingkaran','4.kembali kemenu','5.Exit']
    for i in daftar:
        print(i)
        
    pilihan = int(input("Masukan pilihan anda : "))
    if pilihan == 1 :
        print("Menghitung luas persegi")
        sisi = int(input("Masukan panjang sisi : "))
        persegi = Persegi(sisi)
        print("luas persegi : ",persegi.luas())
                
    elif pilihan == 2 :
        print("menghitung luas segitiga")
        alas = int(input("masukkan panjang alas segitiga : "))
        tinggi = int(input("masukkan panjang tinggi segitiga : "))
        segitiga = Segitiga(alas,tinggi)
        print("luas segitiga = ",segitiga.luas())
    
    elif pilihan == 3:
        print("menghitung luas lingkaran")
        jari2 = int(input("masukkan panjang jari-jari : "))
        lingkaran = Lingkaran(jari2)
        print("luas lingkaran = ",int(lingkaran.luas()))
    
    elif pilihan == 4 :
        pilihan()
    elif pilihan == 5:
        print("Program selesai")
        pass
    else:
        print('Masukan kode dengan benar!')
menu_bagundatar()