print("latihan soal")
nilai = 0
def soal1():
    global nilai
    print("1.ada berapa jumblah kaki ayam?....")
    list = ['a.2','b.3','c.4','d.5']
    for i in list:
        print(i)
    jawaban = input("masukan jawaban anda : ")
    if jawaban == "a" and "A":
        print("selamat jawaban anda benar")
        nilai += 10
        print()
        
def soal2():
    global nilai
    print("2.berapa kaki ular?....")
    list = ['a.3','b.6','c.2','d.semua jawaban salah']
    for i in list:
        print(i)
    jawaban = input("masukan jawaban anda : ")
    if jawaban == "d" and "D":
        nilai += 10
        print("selamat jawaban anda benar")
    else:
        print("jawaban anda salah")
    lanjut = input("lanjut or tidak (y/n) :")
    if lanjut == "y" and "Y":
        print("silahkan masukan kembali jawaban anda")
    elif lanjut == "n" and "N":
        print("program selesai")
    else:
        print('kode yang anda masukan salah')  
soal1()
soal2()  
print("nilai yang anda peroleh adalah : ",nilai)



    
        