total = 0
harga = []
barang = []
while True:   
    print("SELAMAT DATANG DITOKO ANDRE")
    list=["""daftar barang\n
    1.roti \t 2000
    2.es crime \t 5000
    3.buku \t 20000
    4.penghapus \t 3000
    5.penggaris \t 5000
    6.pulpen \t 2000
    7.pensil \t 3000
    8.sapu \t 30000
    9.oli \t 50000
    10.rantai \t 140000
    """]
    for i in list:
        print(i)
    break 

kasir = int(input("silahkan masukan nama pesanan anda : "))
if kasir == 1 :
    barang.append("roti")
    harga.append(2000)
    total += 2000
elif kasir == 2:
    barang.append("es crime")
    harga.append(5000)
    total += 5000
elif kasir == 3:
    barang.append("buku")
    harga.append(20000)
    total += 20000
elif kasir == 4:
    barang.append("penghapus")
    harga.append(3000)
    total += 3000
elif kasir == 5:
    barang.append("penggaris")
    harga.append(5000)
    total += 5000
elif kasir == 6:
    barang.append("pulpen")
    harga.append(2000)
    total += 2000
elif kasir == 7:
    barang.append("pensil")
    harga.append(3000)
    total += 3000
elif kasir == 8:
    barang.append("sapu")
    harga.append(30000)
    total += 30000
elif kasir == 9:
    barang.append("oli")
    harga.append(50000)
    total += 50000
elif kasir == 10:
    barang.append("rantai")
    harga.append(140000)
    total += 140000
else:
    print("kode yang anda masukan salah")  
    
print("barang yang di beli :",barang)
print("harga barang :",harga)
print("total yang harus dibayar :",total)

uang = int(input("masukan uang pembayaran :"))
if uang > total:
    print("uang kembalian :",uang-total)
elif uang == total:
    print("uang pass")
else:
    print("uang anda kurang",uang-total)

lanjut = input("mau lanjut berbelanja? (y/t) :")
if lanjut == "y":
    print("silahkan masukan pesan anda lagi")
     
elif lanjut == "t":
    print("program selesai")

    



           
         
