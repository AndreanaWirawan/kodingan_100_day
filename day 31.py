print("MENAMBAHKAN NAMA DALAM LIST")
while True:
    list = ['jeruk','mangga']
    print(list)
    a = input("Masukan :")
    list.append(a)
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
 