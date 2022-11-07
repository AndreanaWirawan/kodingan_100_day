def pertambahan ():
    input1 = int(input("masukan angka1 :"))
    input2 = int(input("masukan angka2 :"))
    operator = input1 + input2
    print("hasil :",operator)
    
def perkalian ():
    input3 = int(input("masukan angka1 :"))
    input4 = int(input("masukan angka2 :"))
    operator1 = input3 * input4
    print("hasil :",operator1)
        
def pengurangan ():
    input5 = int(input("masukan angka1 :"))
    input6 = int(input("masukan angka2 :"))
    operator2 = input5 - input6
    print("hasil :",operator2)
        
def pembagian ():
    input7 = int(input("masukan angka1 :"))
    input8 = int(input("masukan angka2 :"))
    operator3 = input7 / input8
    print("hasil :",operator3)

def modulus ():
    input9 = int(input("masukan angka1 :"))
    input10 = int(input("masukan angka2 :"))
    operator4 = input9 % input10
    print("hasil :",operator4)

print("KALKULATOR SEDERHANA")
while True:
    print("operator yang ada di dalam")
    list = ['1.pertambahan','2.perkalian','3.pengurangan','4.pembagian','5.modulus']
    for i in list:
        print(i)
    nama = input("silahkan masukan salah satu kode diatas : ")
    if nama == "pertambahan" or nama =="1":
        pertambahan()      
    elif nama == "perkalian" or nama =="2": 
        perkalian()
    elif nama == "pengurangan" or nama =="3": 
        pengurangan()
    elif nama == "pembagian" or nama =="4": 
        pembagian()
    elif nama == "modulus" or nama =="5": 
        modulus()
    else:
        print("maaf coba kode anda salah")

        
    lanjut = input("lanjut or tidak :")
    if lanjut == "lanjut":
        print("silahkan masukan pilihan anda kembali")
    elif lanjut == "tidak":
        print("program selesai")
        break
    




    

    
        



