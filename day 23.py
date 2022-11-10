print("ISI PULSA")
list_pulsa = [
        ['1.pulsa 5',6000],
        ['2.pulsa 10',10000],
        ['3.pulsa 15',16000],
        ['4.pulsa 20',21000],
        ['5.pulsa 25',26000],
        ['6.pulsa 30',31000],
        ['7.pulsa 40',41000],
        ['8.pulsa 50',51000],
        ['9.pulsa 100',101000],
        ['10.pulsa 500',501000]]

for i in list_pulsa:
    for j in range(len(i)):
        print(i[j])
print()

pelangan = int(input("masukan nomer anda :"))
nominal = int(input("masukan kode pulsa :"))


if nominal == 1:
    print("pulsa :",list_pulsa[0][0])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[0][1]) 
elif nominal == 2:
    print("pulsa :",list_pulsa[1][1])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[1][1])
elif nominal == 3:
    print("pulsa :",list_pulsa[2][2])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[2][1])
elif nominal == 4:
    print("pulsa :",list_pulsa[3][3])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[3][1])
elif nominal == 5:
    print("pulsa :",list_pulsa[4][4])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[4][1])
elif nominal == 6:
    print("pulsa :",list_pulsa[5][5])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[5][1])
elif nominal == 7:
    print("pulsa :",list_pulsa[6][6])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[6][1])
elif nominal == 8:
    print("pulsa :",list_pulsa[7][7])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[7][1])
elif nominal == 9:
    print("pulsa :",list_pulsa[8][8])
    print("Nomer :",pelangan)
    print("harga :",list_pulsa[8][1])
else:
    print("kode pulsa yang anda masukan kosong")
  
  