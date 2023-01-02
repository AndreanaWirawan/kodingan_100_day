print("FORMULIR BUAT KTP".center(40 , ' '))
print()
class masukan:
    def biodata():
        nama = input("Masukan nama anda : ")
        umur = input("Masukan umur anda : ")
        jenis_kelamin = input("Masukan jenis kelamin : ")
        alamat = input("Masukan alamat : ")
        golongan_darah = input("Masukan golongan darah : ")
        tempat_tanggal_lahir = input("Masukan tanggal lahir anda : ")
        status = input("Masukan status anda : ")
        print()
        
        print("Hasil".center(40 ,' '))
        print('Nama : ',nama)
        print('Umur : ',umur)
        print('jenis kelamin : ',jenis_kelamin)
        print('Alamat : ',alamat)
        print("Golongan darah : ",golongan_darah)
        print("Tempat tanggal lahir :",tempat_tanggal_lahir)
        print("status : ",status)
        
        print("Apakah biodata sudah anda sudah cocok?..")
        
masukan.biodata()