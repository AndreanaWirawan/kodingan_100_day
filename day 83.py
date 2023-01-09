print('login facebook'.center(40 , ' '))
tampungan = {}

def buat_akun():
    print("Buat Akun Baru".center(40, ' '))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    tampungan[username] = password
    print("Akun Anda telah dibuat!")
    print("Hallo ",username)

def login():
    print("Login")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in tampungan and tampungan[username] == password:
        print("Login berhasil!")
        print("Selamat datang kembali ",username)
    else:
        print("Username atau password salah.")

# nisialisasi variabel
# teks_awal = "Hello World"

# #mengubah teks menjadi "Hello Python"
# teks_awal = teks_awal.replace("World", "Python")

# #mencetak hasil perubahan
# print(teks_awal)

def ganti_sandi():
    print("Ganti sandi")
    username = str(input("Masukkan username: "))
    password = input("Masukkan dulu:  ")
    password1 = input("Masukan password yang baru : ")
    ganti = password.replace,(password1)
    
    print(ganti)
    
    
    
        
while True:
    print("Menu login:\n")
    print("1. Buat Akun Baru")
    print("2. Login")
    print("3. Cek akun")
    print('4. Ganti sandi')
    print('5. Exit\n')
    pilihan = input("Masukkan pilihan : ")
    
    if pilihan == '1':
        buat_akun()
    elif pilihan == '2':
        login()
    elif pilihan == '3':
        for i in tampungan:
            print(i)
    elif pilihan == "4":
        ganti_sandi()
    elif pilihan == '5':
        print('Program selesai')
        break
    else:
        print("Kode yang anda masukan salah!!")


