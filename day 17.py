print('=' * 10, "SELAMAT DATANG DI AGEN TOKO KAMI", '=' * 10)
print('=' * 8, "SILAHKAN PILIH TOKO YANG ANDA INGIN MASUKI", '=' * 8)
print("toko naila")
print("toko fila")
print("toko andre")
nama = input("masukan nama toko :")

if nama == "toko naila":
    print("daftar menu yang ada di toko naila adalah")
    print("toko kami hanya menyediakan sayur-sayuran")
    list_benda = ['terong','cabai','tomat','kedelai','jagung']
    for i in list_benda:
        print(i)
elif nama == "toko fila":
    print("daftar menu yang ada di toko toko fila adalah")
    print("toko kami hanya menyediakan buah-buahan")
    list_benda1 = ['kopi','mie','mangga','apel','jeruk']
    for i in list_benda1:
        print(i)
elif nama == "toko andre":
    print("selamat datang di toko smartphon andre")
    print("toko kami hanya meyediakan smartphon yang bermerk")
    list_benda2 = ['vivo','relame','nokia','iphone','samsung','redmi']
    for i in list_benda2:
        print(i)
else:
    print("maaf toko yang anda tujuh tidak ada dalam menu")
    print("program selesai")
