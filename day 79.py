print('program tampilan login')
user = "user"
password = "admin"

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == user and password == password:
  print("Selamat datang, admin!")
else:
  print("Username atau password yang Anda masukkan salah.")