print("SELEKSI TES SIM")
def biodata():
    nama = input("masukan nama anda : ")
    umur = input("masukan umur anda : ")
    nilai = int(input("masukan hasil nilai : "))
    print(nama)
    print(umur)
    print(nilai)

    if umur >= "17" and nilai >= 80 and nilai <= 100:
        print("anda berhak daftar sim")
    elif umur <= "17":
        print("Maaf anda belum cukup umur")

biodata()
