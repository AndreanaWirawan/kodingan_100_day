nama = str(input("masukan nama lengkap anda : "))
umur = int(input("masukan tahun lahir anda : "))

if umur >= 1965 and umur <=1976:
    print("anda termasuk generasi X")
elif umur >= 1980 and umur<=1944:
    print("anda termasuk generasi Y")
elif umur >= 1995 and umur<=2022:
    print("anda termasuk generasi Z")
else:
    print("maaf anda masih di pikirkan mau masuk di generasi apa")
