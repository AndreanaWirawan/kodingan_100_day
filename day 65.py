print('=' * 20, "KODINGAN 5", '=' * 20)

class operator:
    def rumus():
        angka1 = int(input("masukan angka anda : "))
        operator = input("operator +,-,*,/ : ")
        angka2 = int(input("masukan angka anda : "))

        if operator == "+":
            print(angka1 + angka2)
        elif operator == "-":
            print(angka1 - angka2)
        elif operator == "x":
            print(angka1 * angka2)
        elif operator == "/":
            print(angka1 / angka2)
            
        else:
            print("maaf kode yang anda masukan salah")
            

        
operator.rumus()

