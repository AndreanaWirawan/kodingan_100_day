Tampungan = 1000
login = {}
run = True
while True:
    print("Selamat datang di ATM!".center(40, ' '))
    list = ['1. Login','2. Cek saldo','3. Tarik tunai','4. Isi saldo','5. Ganti sandi','6. Exit']
    for i in list:
        print(i)

    pilihan = int(input("Masukan pilihan anda: "))
    if pilihan == 1:
        print("Login")
        user = "user"
        password = "admin"
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == user and password == password:
            print("Selamat datang, admin!")
            print('saldo anda saat ini : ', Tampungan)

        elif username in login and login[username] == password:
            print("Login berhasil!")
        
        else:
            print("Username atau password salah.")
            
    elif pilihan == 2:
        print("Isi Saldo anda :", Tampungan)
        
    elif pilihan == 3:
        tarik = int(input("Masukan jumblah yang ingin anda tarik : "))
        if tarik > Tampungan:
            print("Saldo anda tidak cukup")
        else:
            Tampungan -= tarik
            print("Penarikan Berhasil.")
            print("Sisa saldo anda :", Tampungan)
            
    elif pilihan == 4:
        saldo = int(input("Masukan jumlah yang ingin anda Stor : "))
        Tampungan += saldo
        print("Isi saldo berhasil.")
        print("Isi saldo saat ini :", Tampungan)
    
    elif pilihan == 5:
        print("Ganti sandi")
        username = str(input("Masukkan username: "))
        password = input("Masukkan dulu:  ")
        password1 = input("Masukan password yang baru : ")
        ganti = password.replace,(password1)
    
        print(ganti)
        
        
    elif pilihan == 6 :
        print("Terima kasih telah mengunakan ATM.".center(40, ' '))
        run = False
        break
    else:
        print("kode yang anda masukan salah")