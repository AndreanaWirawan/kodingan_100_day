def lanjut():
    while True:  
        lanjut = input("lanjut or tidak :")
        if lanjut == "lanjut":
            print("silahkan isi kembali biodata")
            print()
            biodata()
        elif lanjut == "tidak":
            print("program selesai")
            break        
        else:
            print("kode anda masukan salah")

print("SELAMAT DATANG RUMAH SAKIT MANAKKARA")
print()
def biodata ():
    nama = input("masukan nama paisen :")
    biodata.umur = input("masukan umur pasien :")
    alamat = input("masukan alamat pasien :")
    biodata.keluhan = input("masukan keluahan pasien :")
    print()
    print("BIODATA DIRI PASIEN")
    print("Nama :",nama)
    print("Umur :",biodata.umur)
    print("Alamat :",alamat)
    print("keluhan :",biodata.keluhan)
    print()
    obat()

def obat ():
    if biodata.keluhan == "flu" or biodata.keluhan == "1":
        print("Nama Obat")
        print("ultra flu")
        print()
        lanjut()
    elif biodata.keluhan == "batuk" or biodata.keluhan == "2":
        print("Nama Obat")
        print("laserin")
        print()
        lanjut()
    elif biodata.keluhan == "sakit kepala" or biodata.keluhan == "3":
        print("Nama Obat")
        print("paramex")
        print()
        lanjut()
    elif biodata.keluhan == "panas" or biodata.keluhan == "4":
        print("Nama Obat")
        print("paracetamol")
        print()
        lanjut()
    elif biodata.keluhan == "sakit gigi" or biodata.keluhan == "5":
        print("Nama Obat")
        print("asam mefanamat")
        print()
        lanjut()    
    elif biodata.keluhan == "maag" or biodata.keluhan == "6":
        print("Nama Obat")
        print("promag")
        print()
        lanjut()
    else:
        print("maaf rumah sakit ini hanya melayani penyakit")
        list = ['1.flu','2.batuk','3,sakit kepala','4.panas','5.sakit gigi','6.maag']
        for i in list:
            print(i)
            biodata()

biodata()

        
    
    
    
    

    


        






