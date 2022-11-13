print("TABEL PERKALIAN")
while True:
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
    else:
        print("maaf kode anda salah")
        break