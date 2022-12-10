print("toko andre")
def barang():
    list = ['1.apel','2.mangga','3.nanas','4.jeruk']
    for i in list:
        print(i)
barang()

while True:
    pilihan1 = input("masukan nama buah anda : ")
    if pilihan1 =="apel":
        pilih = input("mau belanja lagi : ")
        if pilih == "y":
            print("pilih kembali belanjaan")
            barang()
        elif pilih == "n":
            print("belanja yang anda beli")
            print(pilihan1) 
            break 
            
    pilihan2 = input("masukan nama buah anda : ")
    if pilihan2 =="mangga":
        pilih = input("mau belanja lagi : ")
        if pilih == "y":
            print("pilih kembali belanjaan")
            barang()
        elif pilih == "n":
            print("belanja yang anda beli")
            print(pilihan1)
            print(pilihan2)  
            break
        
    pilihan3 = input("masukan nama buah anda : ")
    if pilihan3 =="nanas":
        pilih = input("mau belanja lagi : ")
        if pilih == "y":
            print("pilih kembali belanjaan")
            barang()
        elif pilih == "n":
            print("belanja yang anda beli")
            print(pilihan1)
            print(pilihan2)
            print(pilihan3)
            break   

    pilihan4 = input("masukan nama buah anda : ")
    if pilihan4 =="jeruk":
        pilih = input("mau belanja lagi : ")
        if pilih == "y":
            print("pilih kembali belanjaan")
            barang()
        elif pilih == "n":
            print("belanja yang anda beli")
            print(pilihan1)
            print(pilihan2) 
            print(pilihan3)
            print(pilihan4) 
            break     