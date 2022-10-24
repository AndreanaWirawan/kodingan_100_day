# program mengecek nilai
tugas = int(input("masukkan nilai tugas : "))
uts = int(input("masukkan nilai uts : "))
final = int(input("masukkan nilai final : "))
hasil = (tugas + uts + final) / 3
if hasil >= 91 and hasil <= 100 :
    print("nilai anda adalah A")
elif hasil >= 81 and hasil <= 90 :
    print("nilai anda adalah B")
elif hasil >= 71 and hasil <= 80 :
    print("nilai anda adalah C")
elif hasil >= 61 and hasil <= 70 :
    print("nilai anda adalah D")
elif hasil <= 60 and hasil >= 0 :
    print("nilai anda adalah E")
else : 
    print("terjadi kesalahan")