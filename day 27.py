print('UNTUK MENEMUKAN BILANGAN GANJIL YANG HABIS DI BAGI 3')
end = int(input("masukan angka anda : "))
list_kosong =[]
for i in range(0, end+1):
    if (i%3==0 and i%2==1):
        list_kosong.append(i)
print(list_kosong)
print("hasil keseluruhan :",sum(list_kosong))
print('program selesai')   


        
