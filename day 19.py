print("PROGRAM MENGITUNG LUAS")
while True:
    print('1.persegi')
    print('2.persegi panjang')
    menu = input("masukan angka yang anda ingin hitung :")


    if menu == "1":
        sisi_persegi = float(input("masukan panjang sisi :"))
        luas = sisi_persegi * sisi_persegi
        print('luas persegi adalah :',luas)
        print()


    elif menu == "2":
        panjang = float(input("masukan panjang persegi :"))
        lebar = float(input("masukan lebar persegi :"))
        keliling = panjang * lebar
        hasil = 2*(panjang+lebar)
        print('luas persegi panjang adalah',hasil)
        print()
    else:
        print('kode yang anda masukan salah')

    lanjut = input("lanjut or tidak :")
    if lanjut == "tidak":
        print("program selesai")
        break
    elif lanjut == "lanjut":
        print()
    else:
        print('Maaf kode yang anda masukan salah')
        
        
       
        
