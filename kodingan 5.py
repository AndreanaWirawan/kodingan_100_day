print('=' * 20, "KODINGAN 5", '=' * 20)

angka1 = float(input("masukan angka anda :"))
operator = input("operator +,-,*,/ :")
angka2 = float(input("masukan angka anda :"))
 
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
    


