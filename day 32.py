print("MENAMPILKAN TABEL (+,-,X,/")

while True:
    print("1.pertambahan")
    print("2.perkalian")
    print("3.pengurangan")
    print("4.pembagian")

    pilihan = input("masukan pilihan : ")
    if pilihan == "1":
        angka = int(input("ditampilkan pertambahan : "))
        for i in range(1,11):
            print(angka,'+',i,'=',angka+i)
        lanjut = input("lanjut or tidak : ")
        if lanjut == "lanjut":
            print("silahkan masukan kembali")
        elif lanjut =="tidak":
            print("program selesai")
            break
        
    elif pilihan == "2":
        angka = int(input("menampilkan perkalian : "))
        for i in range(1, 11):
            print(angka, 'x',i,'=',angka*i)
        print()             
        lanjut = input("lanjut or tidak :")
        if lanjut == "lanjut":
            print("silahkan masukan kembali")
        elif lanjut == "tidak":
            print("program selesai")
            break

    elif pilihan == "3":
        angka = int(input("menampilkan pengurangan : "))
        for i in range(1, 11):
            print(angka, '-',i,'=',angka-i)
        print()             
        lanjut = input("lanjut or tidak :")
        if lanjut == "lanjut":
            print("silahkan masukan kembali")
        elif lanjut == "tidak":
            print("program selesai")
            break

    elif pilihan == "4":
        angka = int(input("menampilkan pembagian : "))
        for i in range(1, 11):
            print(angka, '/',i,'=',angka/i)
        print()
        lanjut = input("lanjut or tidak :")
        if lanjut == "lanjut":
            print("silahkan masukan kembali")
        elif lanjut == "tidak":
            print("program selesai")
            break

    else:
        print("kode yang anda masukan salah")
        lanjut = input("mau lanjut (y/t)")
        if lanjut == "y":
            print("silahkan masukan kembali")
        elif lanjut == "t":
            print("program berhenti")
        