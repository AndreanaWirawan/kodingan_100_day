print('')
print("MENAMBAHKAN DALAM LIST")
while True:
    list = ['jeruk','mangga','nanas','apel']
    for i in list:
        print(i)
    print()
    masukan = input("Masukan nama buah : ")
    print()
    list.append(masukan)
    for i in list:
        print(i)
    print()
    lanjut = input("lanjut or tidak (y/t):")
    if lanjut == "y":
        print("silahkan masukan kembali")
    elif lanjut == "t":
        print("program selesi")
        break
    else:
        print("kode yang anda masukan salah")
        break
 