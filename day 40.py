print("latihan soal")
while True:
    def soal1():
        print("1.ada berapa jumblah kaki ayam?....")
        list = ['a.2','b.3','c.4','d.5']
        for i in list:
            print(i)
    soal1()
    jawaban = input("masukan jawaban anda : ")
    if jawaban == "a":
        print("selamat jawaban anda benar")
    else:
        print("jawaban anda salah")
    lanjut = input("lanjut or no(y/n)")
    if lanjut == "y":
        print()
        print("silahkan masukan kembali jawaban anda")
    elif lanjut == "n":
        print("program selesai")
        break
    else:
        print('kode yang anda masukan salah')
        
    def soal2():
        print("2.berapa kaki ular?....")
        list = ['a.3','b.6','c.2','d.semua jawaban salah']
        for i in list:
            print(i)
    soal2()
    jawaban = input("masukan jawaban anda : ")
    if jawaban == "D":
        print("selamat jawaban anda benar")
    else:
        print("jawaban anda salah")
    lanjut = input("lanjut or tidak (y/n)")
    if lanjut == "y":
        print("silahkan masukan kembali jawaban anda")
    elif lanjut == "n":
        print("program selesai")
        break
    else:
        print('kode yang anda masukan salah')
        