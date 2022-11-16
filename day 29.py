print('PROGRAM UNTUK MENAMPILKAN PERTAMBAHAN')
while True:
    angka = int(input("ditampilkan pertambahan : "))
    for i in range(1,11):
        print(angka,'+',i,'=',angka+i)
    lanjut = input("lanjut or tidak : ")
    if lanjut == "lanjut":
        print("silahkan masukan kembali")
    elif lanjut =="tidak":
        break
    else:
        print("kode yang anda masukan salah")
        break