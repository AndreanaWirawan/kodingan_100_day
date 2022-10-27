print('=' * 20, "KODINGAN 9", '=' * 20)
umur1 = int(input("masukan umur anda :"))

if umur1 >= 5 and umur1 <=12:
    print("anda tergolong anak-anak")

elif umur1 >= 13 and umur1 <=18:
    print("anda tergolong remaja")

elif umur1 >=19 and umur1 <=29:
    print("anda tergolong dewasa")

elif umur1 >= 30 and umur1 <=75:
    print("anda tergolong tua ")

elif umur1 >= 76 and umur1 <=85:
    print("anda tergolong lansia")
    
else:
    print("umur tidak terdeteksi")