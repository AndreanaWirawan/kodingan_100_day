print("MENENTUKAN DOSIS OBAT SESUAI UMUR")
def biodata():
    nama = input("masukan nama anda : ")
    umur = input("masukan umur anda : ")
    keluhan = input("masukan keluhan anda : ")
    print()
    print(nama)
    print(umur)
    print(keluhan)

    if umur >= "5" and umur <= "10":
        print("Dosis obat yang harus diberikan adalah")
        print("250 mg.")
        print("TIDAK DI ANJURKAN UNTUK IBU HAMIL")
    elif umur >= "10" and umur <= "15":
        print("Dosis obat yang harus diberikan adalah")
        print("500 mg.")
        print("TIDAK DI ANJURKAN UNTUK IBU HAMIL")
    elif umur >= "15" and umur <= "30":
        print("Dosis obat yang harus diberikan adalah")
        print("5.000 mg")
        print("TIDAK DI ANJURKAN UNTUK IBU HAMIL")
    elif umur >= "30" and umur <= "50":
        print("Dosis obat yang harus diberikan adalah")
        print("1.000 mg")
        print("TIDAK DI ANJURKAN UNTUK IBU HAMIL")
    elif umur >= "50" and umur <= "100":
        print("Dosis obat yang harus diberikan adalah")
        print("1.000 - 1.500 mg")
        print("TIDAK DI ANJURKAN UNTUK IBU HAMIL")
    else:
        print("Semoga lekas sembuh")
biodata()