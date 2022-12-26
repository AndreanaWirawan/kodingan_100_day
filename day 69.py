print("MENAMBAHKAN NAMA DALAM LIST")
while True:
    list = ['jeruk','mangga','nanas','apel']
    print(list)
    masukan = input("Masukan nama buah :")
    list.append(masukan)
    print(list)
    lanjut = input("lanjut or tidak (y/t):")
    if lanjut == "y":
        print("silahkan masukan kembali")
    elif lanjut == "t":
        print("program selesi")
        break
    else:
        print("kode yang anda masukan salah")
        break
 