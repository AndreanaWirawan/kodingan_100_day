print("program hitung mundur")

import time
waktu = int(input("masukan waktu : "))
for i in range(1, waktu+1):
    print("detik ke : ",i)
    time.sleep(1)
if i == waktu:
    print("program selesai")