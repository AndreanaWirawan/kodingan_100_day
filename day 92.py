print("Kartu kip kuliah dgital\n")
print("Silahkan masukkan identitas anda\n")
nama = input("masukkan nama anda :")
nim = input("Masukkan nim anda (tanpa titik) :\n")

pilih = 1
while pilih != 0:
    print("Daftar beasiswa yang tersedia")
    print("1. Beasiswa berprestasi")
    print("2. Beasiswa kurang mampu")
    
    pilih=int(input("Masukkan pilihan anda (1/2):"))
    print()
    if pilih == 1:
        nilai = float(input("Masukkan nilai IPK :"))
        if nilai >= 3.5:
            print("\n\n")
            print("NAMA\t:",nama)
            print("NIM\t :",nim)
            print()
            print("Selamat anda lolos seleksi beasiswa Berprestasi")
            print("\n\n")
        else:
            print("Mohon maaf anda belum lolos seleksi beasiswa berprestasi")
        
    elif pilih == 2:
        penghasilan=int(input("Masukkan penghasilan orang tua perbulan (tanpa titik) :"))
        if penghasilan <= 1500000:
            print("\n\n")
            print("NAMA\t:",nama)
            print("NIM\t:",nim)
            print()
            print("Selamat anda lolos seleksi beasiswa kurang mampu")
            print("\n\n")
        else:
            print("Mohon maaf anda belum lolos seleksi beasiswa kurang mampu")
            print()
            
    else:
        print("Masukkan pilihan anda dengan benar!")
        print()
            