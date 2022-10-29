print("GAME QUIZ SOAL\n")

print("1. 200 X 5?")
print("a. 500\nb. 250\nc. 750\nd. 1000\n")
while True:
    jawaban = input("Silahkan pilih jawaban anda :")
    if jawaban == "d":
        print("JAWABAN ANDA BENAR")
        print("program selesai")
        break
    elif jawaban != "d":
        print("JAWABAN ANDA SALAH")