print("SELAMAT DATANG DI APOTIK KITA")
while True:
    keluhan = str(input("masukan keluhan anda :"))
    
    if keluhan == "flu":
        print("obat yang cocok untuk flu adalah")
        list_obat1 =['1.ultraflu','2.intunal-f','3.procold','4.termorex']
        for i in list_obat1:
            print(i)
        print('jadi mau beli obat yang mana?')
        obat = input("masukan pilihan obat anda :")
        print(obat)        
           
    elif keluhan == "batuk":
        print("obat yang cocok untuk batuk adalah")
        list_obat2=['1.obat batuk siladex','2.obat batuk OBH','3.obat batuk takabb','4.obat batuk konidin','5.obat batuk komix','6.obat batuk laserin']
        for i in list_obat2:
            print(i)
        print('jadi mau beli obat yang mana?')
        obat = input("masukan pilihan obat anda :")
        print(obat)
        
    elif keluhan == "demam":
        print("obat yang cocok untuk demam adalah")
        list_obat3 =['1.sanmol tablet','2.panadol','3.bodrex','4.sumagesic']
        for i in list_obat3:
            print(i)
        print('jadi mau beli obat yang mana?')
        obat = input("masukan pilihan obat anda :")
        print(obat)
        
    elif keluhan =="meriang":
        print("obat yang cocok untuk meriang adalah")
        list_obat4=['1.paracetamol','2.bodrex','3.ibuprofen']
        for i in list_obat4:
            print(i)
        print('jadi mau beli obat yang mana?')
        obat = input("masukan pilihan obat anda :")
        print(obat) 
        
    elif keluhan == "sakit kepala":
        print("obat yang cocok untuk sakit kepala adalah")
        list_obat5 = ['1.bodrek','2.oskadon']
        for i in list_obat5:
            print(i)
        print('jadi mau beli obat yang mana?')
        obat = input("masukan pilihan obat anda :")
        print(obat)
        
    lanjut = input("lanjut or tidak :")
    if lanjut == "tidak":
        print("TerimaKasih")
        print("Moga Lekas Sembuh")
        break
    
    
