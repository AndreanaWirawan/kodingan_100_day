import time

while True:
    print("program hitung mundur")
    list = ['1.masak nasi','2.goreng telur','3.masak mie']
    for i in list:
        print(i)
    pilihan = input("masukan pilihan anda : ")
    if pilihan == "1":
        for i in range(1,20+1):
            print("menit ke : ",i)
            time.sleep(60)
        if i == i:
            print("nasi sudah masak")
        lanjut = input("lanjut or tidak (y/n) :")
        if lanjut == "y" and "Y":
            print("silahkan masukan kembali pilihan")
        elif lanjut == "n" and "N":
            print("program selesai")
            break
        else:
            print('kode yang anda masukan salah')  
            
    elif pilihan == "2":
        for i in range(1, 5+1):
            print("menit ke : ",i)
            time.sleep(60)
        if i == i:
            print("telur telah masak")
        lanjut = input("lanjut or tidak (y/n) :")
        if lanjut == "y" and "Y":
            print("silahkan masukan kembali pilihan")
        elif lanjut == "n" and "N":
            print("program selesai")
        else:
            print('kode yang anda masukan salah') 
            break  
            
    elif pilihan == "3":
        for i in range(1, 3+1):
            print("menit ke : ",i)
            time.sleep(60)
        if i == i:
            print("mie telah masak")
        lanjut = input("lanjut or tidak (y/n) :")
        if lanjut == "y" and "Y":
            print("silahkan masukan kembali pilihan")
        elif lanjut == "n" and "N":
            print("program selesai")
        else:
            print('kode yang anda masukan salah') 
            break 
    else:
        print("kode yang anda masukan salah")
        break
   
    
    
