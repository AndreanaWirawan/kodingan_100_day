Tampungan = 1000
run = True
while True:
    print("Selamat datang di ATM!".center(40, ' '))
    print("1. Check Saldo")
    print("2. Tarik Tunai")
    print("3. Isi Saldo")
    print("4. Exit")

    pilihan = int(input("Masukan pilihan anda: "))
    if pilihan == 1:
        print("Isi Saldo anda :", Tampungan)
        
    elif pilihan == 2:
        tarik = int(input("Masukan jumlah yang ingin anda tarik : "))
        if tarik > Tampungan:
            print("Saldo anda tidak cukup")
        else:
            Tampungan -= tarik
            print("Penarikan Berhasil.")
            print("Sisa saldo anda :", Tampungan)
            
    elif pilihan == 3:
        saldo = int(input("Masukan jumblah yang ingin anda Stor : "))
        Tampungan += saldo
        print("Isi saldo berhasil.")
        print("Isi saldo saat ini :", Tampungan)
        
    elif pilihan == 4:
        print("Terima kasih telah mengunakan ATM.".center(40, ' '))
        run = False
        break
    else:
        print("kode yang anda masukan salah")