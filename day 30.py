print("PROGRAM MENENTUKAN BILANGAN GANJIL DAN GENAP")
while True:
    nilai_akhir = int(input("masukan nilai akhir : "))
    print("1.ganjil")
    print("2.genap")
    pilihan = input("masukan pilihan anda : ")
    if pilihan == "1":
        for i in range(0,nilai_akhir+1):
            if(i%2==1):
                print(i)
    elif pilihan == "2":
        for j in range(0,nilai_akhir+1):
            if(j%2==0):
                print(j)

    lanjut = input("lanjut or tidak : ")   
    if lanjut =="lanjut":
        print("silakahkan masukan kembali")
    elif lanjut == "tidak":
        print("program berhenti")
        break
    else:
        print("kode yang anda masukan salah")
        break