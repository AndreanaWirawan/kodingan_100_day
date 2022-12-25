print("perintah menggunakkan perulangan for")

angka1 = int(input("Masukan angka awal : "))
angka2 = int(input('Masukan angka akhir : '))
angka3 = int(input('masukan angka lompatan : '))
print()
print("angka awal : ",angka1)
print("angka akhir : ",angka2)
print("batas lompatan : ",angka3)

print()
print("hasil")
for i in range(angka1 ,angka2+1 , angka3):
    print(i)