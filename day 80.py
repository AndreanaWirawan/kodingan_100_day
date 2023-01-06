print('login facebook'.center(40 , ' '))
tampungan = {}

def buat_akun():
    print("Buat Akun Baru")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    tampungan[username] = password
    print("Akun Anda telah dibuat!")

def login():
    print("Login")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    
    if username in tampungan and tampungan[username] == password:
        print("Login berhasil!")
    else:
        print("Username atau password salah.")
        
while True:
    print("Pilih opsi:")
    print("1. Buat Akun Baru")
    print("2. Login")
    print("3. Exit")
    pilihan = input("Masukkan pilihan : ")
    
    if pilihan == '1':
        buat_akun()
    elif pilihan == '2':
        login()
    elif pilihan == '3':
        print('Program selesai')
        break

    else:
        print("Kode yang anda masukan salah!!")

