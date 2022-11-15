angka = int(input("masukan angka akhir : "))
list_tampungan = []
for i in range(1,angka+1):
        if(i%2==1):
            list_tampungan.append(i)
for j in range(1,angka+1):
        if(j%2==0):
            list_tampungan.append(j)
print("ini adalah bilangan ganjil")
print(list_tampungan,i)
print()
print("ini adalah bilangan genap")
print(list_tampungan,j)