class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi**3

class Limas(BangunRuang):
    def __init__(self,panjang_alas,tinggi_alas,tinggi_limas):
        self.panjang_alas = panjang_alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_limas = tinggi_limas

    def volume(self):
        return (self.panjang_alas*self.tinggi_alas/2) * self.tinggi_limas / 3

class Tabung(BangunRuang):
    def __init__(self,jari2,tinggi):
        self.phi = 22/7
        self.jari2 = jari2
        self.tinggi = tinggi

    def volume(self):
        return self.phi * (self.jari2**2) * self.tinggi
    

def menu_bagunruang():
    print("MENU BAGUN RUANG".center(40 , ' '))
    daftar = ['1.Kubus','2.Limas','3.Tabung','4.Kembali ke menu','5.Exit']
    for i in daftar:
        print(i)
    
    pilihan = int(input("Masukan pilihan anda : "))
    if pilihan == 1 : 
        print("menghitung volume kubus")
        sisi = int(input("masukkan panjang sisi : "))
        kubus = Kubus(sisi)
        print("volume kubus = ",kubus.volume()) 
    elif pilihan == 2 : 
        print("menghitung volume limas segitiga")
        alas = int(input("masukkan panjang alas segitiga : "))
        tinggi_alas = int(input("masukkan panjang tinggi alas segitiga : "))
        tinggi_limas = int(input("masukkan panjang tinggi limas : "))
        limas = Limas(alas,tinggi_alas,tinggi_limas)
        print("volume limas segitiga = ",limas.volume())
    elif pilihan == 3 : 
        print("menghitung volume tabung")
        jari2 = int(input("masukkan panjang jari-jari : "))
        tinggi = int(input("masukkan tinggi tabung : "))
        tabung = Tabung(jari2,tinggi)
        print("volume tabung = ",int(tabung.volume()))
    elif pilihan == 4 : 
        pilihan()
    elif pilihan == 5 :
        print('Program selesai')
        pass
    else : 
        print("masukkan kode menu dengan benar!")
menu_bagunruang()