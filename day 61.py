class bagun_datar ():
    def persegi():      
        print()
        print('Persegi'.center(40, ' '))  
        sisi = int(input('Masukan nilai sisi : '))
        luas = sisi * sisi
        print('Hasil :',int(luas)) 
        
    def segitiga():
        print()
        print('Segitiga'.center(40, ' ')) 
        alas = int(input('Masukan nilai alas : '))
        tinggi = int(input('masukan nilai tinggi : '))
        luas = 0.5 * alas * tinggi
        print('Hasil : ',int(luas))
    
    def lingkaran():
        print()
        print('Lingkaran'.center(40, ' ')) 
        jari = int(input('masukan nilai jari-jari : '))
        luas = 22/7 * jari * jari
        print('Hasil :',int(luas))
        
class bagun_ruang():
    def kubus ():
        print()
        print('Kubus'.center(40, ' ')) 
        rusuk = int(input("Masukan nilai sisi 1 : "))
        luas = rusuk**3   
        print('Hasil ',int(luas)) 
    
    def  limas_segitiga ():
        print()
        print('Limas Segitiga'.center(40, ' ')) 
        alas = int(input('Masukan nilai alas : '))
        tinggi = int(input('Masukan nilai tinggi segitiga : '))
        tinggi_limas = int(input('Masukan nilai tinggi limas :'))
        luas = alas * tinggi/2
        volume = 1/3 * luas * tinggi_limas
        print('Hasil :',int(volume))
    
    def tabung ():
        print()
        print('Tabung'.center(40, ' ')) 
        jari = int(input('Masukan nilai jari-jari : '))
        tinggi = int(input('Masukan nilai tinggi : '))
        luas = 22/7 * jari * jari
        volume = luas * tinggi
        print('Hasil : ',int(volume))
        
def kembali ():
    lanjut = input('Lanjut or No (y.n)')
    if lanjut == "y":
        menu()
    elif lanjut == "n":
        print('program selesai')
    else:
        pass
        
      

def menu():      
    print("MENU".center(40, ' '))
    list = ['1.Persegi','2.Segitiga','3.Lingkaran','4.Kubus','5.Limas segitiga','6.Tabung']
    for i in list:
        print(i)     
    pilihan = input('Masukan pilihan anda : ')
    if pilihan ==   "1":
        bagun_datar.persegi()    
        kembali()       
            
    elif pilihan == "2":
        bagun_datar.segitiga()
        kembali()
        
    elif pilihan == "3":
        bagun_datar.lingkaran()
        kembali()
        
    elif pilihan == "4":
        bagun_ruang.kubus()
        kembali()
        
    elif pilihan == "5":
        bagun_ruang.limas_segitiga()
        kembali()
        
    elif pilihan == "6":
        bagun_ruang.tabung()
        kembali()
        
    else:
        print('pilihan kosong')
        kembali()
        
menu()   

   
