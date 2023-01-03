print("PENGIMPUTAN BIODATA DIRI".center(40 , ' '))
print()
class masukan:
    def biodata_ktp():
        print()
        print("From KTP".center(40 , ' '))
        nama = input("Masukan nama anda : ")
        umur = input("Masukan umur anda : ")
        jenis_kelamin = input("Masukan jenis kelamin : ")
        alamat = input("Masukan alamat : ")
        golongan_darah = input("Masukan golongan darah : ")
        tempat_tanggal_lahir = input("Masukan tanggal lahir anda : ")
        status = input("Masukan status anda : ")
        
        print("Hasil".center(40 ,' '))
        print('Nama : ',nama)
        print('Umur : ',umur)
        print('jenis kelamin : ',jenis_kelamin)
        print('Alamat : ',alamat)
        print("Golongan darah : ",golongan_darah)
        print("Tempat tanggal lahir :",tempat_tanggal_lahir)
        print("status : ",status)
        print("Apakah biodata sudah anda sudah cocok?..")
        print()
        
    def biodata_mahasiswa():
        print()
        print("From Mahasiswa".center(40 , ' '))
        nama = input("Masukan nama anda : ")
        nim = input("Masukan nim mahasiswa : ")
        umur = input("Masukan umur anda : ")
        jenis_kelamin = input("Masukan jenis kelamin : ")
        alamat = input("Masukan alamat : ")
        golongan_darah = input("Masukan golongan darah : ")
        tempat_tanggal_lahir = input("Masukan tanggal lahir anda : ")
        status = input("Masukan status anda : ")
        print()
        
        print("Hasil".center(40 ,' '))
        print('Nama : ',nama)
        print("Nim : ",nim)
        print('Umur : ',umur)
        print('jenis kelamin : ',jenis_kelamin)
        print('Alamat : ',alamat)
        print("Golongan darah : ",golongan_darah)
        print("Tempat tanggal lahir :",tempat_tanggal_lahir)
        print("status : ",status)
        
        print("Apakah biodata sudah anda sudah cocok?..")
        print()
        
def menu():
    Menu = ['1.Isi formulir ktp','2.Isi formulir mahasiswa']
    for i in Menu:
        print(i)
    pilihan = int(input("masukan kode di atas : "))
    if pilihan == 1:
        masukan.biodata_ktp()
    elif pilihan == 2:
        masukan.biodata_mahasiswa()
    else:
        print("coba masukan kode dengan benar!!")
        menu()

menu()