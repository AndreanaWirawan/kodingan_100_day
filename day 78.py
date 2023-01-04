print('UNTUK MENEMUKAN BILANGAN GANJIL YANG HABIS DI BAGI 3')
end = int(input("masukan angka anda : "))
list_kosong =[]
for i in range(0, end+1):
    for j in range(1, end+1):
        if (i%3==0 and j%2==1):
            list_kosong.append(i)
            print(list_kosong)