tampungan = {}

while True:
    nama = input("Masukan nama pegawai or cek (y) : ")
    if nama == 'y':
        break
    if nama in tampungan:
        print(nama, "Nama pegawai.")
    else:
        tampungan[nama] = True
        print(nama, "Yang hadir.")

print("Pegawai yang isi absen".center(40, ' '))
for i in tampungan:
    print(i)
    