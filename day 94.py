print('jadwal matakuliah'.center(40, ' '))
def menu():
    jadwal = input('Masukan hari yang ingin anda cek : ')
    if jadwal == 'senin':
        senin()
        pass
    elif jadwal == 'rabu':
        selasa()
        pass
    elif jadwal == 'rabu':
        rabu()
        pass
    elif jadwal == 'Kamis':
        kamis()
        pass
    elif jadwal == 'jukmat':
        jukmat()
        pass
    elif jadwal == 'sabtu':
        sabtu()
        pass
    elif jadwal == 'minggu':
        minggu()
        print('kode yang anda masukan kurang akurat!!')
        pass
def senin():
    list = ['Pbo','Basis data','Baisi data 1']
    for i in list:
        print(i)
    dosen = input('apakah anda ingin melihat dosen yang mengajar?..')
    if dosen == 'y':
        nama_dosen = ['Arul.S,kom.M,kom','Haswar.S,kom.M,kom']
        pass
        for j in nama_dosen:
            print(j)
    elif dosen == 'n':
        pass

def selasa():
    mk = ['Java','Pengembangan multi media']
    for i in mk:
        print(i)
    dosen = input('apakah anda ingin melihat dosen yang mengajar?..')
    if dosen == 'y':
        nama_dosen = ['deni.S,kom.M,kom','joni.S,kom.M,kom']
        pass
        for j in nama_dosen:
            print(j)
    elif dosen == 'n':
        pass
    
def rabu():
    mk = ['Python','Pemrograman web']
    for i in mk:
        print(i)
    dosen = input('apakah anda ingin melihat dosen yang mengajar?..')
    if dosen == 'y':
        nama_dosen = ['Putu.S,kom.M,kom','Fyan.S,kom.M,kom']
        pass
        for j in nama_dosen:
            print(j)
    elif dosen == 'n':
        pass
    
def kamis():
    mk = ['Multi media','Dasar dasar pemrograman']
    for i in mk:
        print(i)
        pass
    dosen = input('apakah anda ingin melihat dosen yang mengajar?..')
    if dosen == 'y':
        nama_dosen = ['Aco,kom.M,kom','Tono.S,kom.M,kom']
        for j in nama_dosen:
            print(j)
    elif dosen == 'n':
        pass
    
def jukmat():
    mk = ['Aljabar']
    for i in mk:
        print(i)
        pass
    dosen = input('apakah anda ingin melihat dosen yang mengajar?..')
    if dosen == 'y':
        nama_dosen = ['Artini.S,kom.M,kom']
        for j in nama_dosen:
            print(j)
    elif dosen == 'n':
        pass
    
def sabtu():
    mk = ['Matematika dasar','C++']
    for i in mk:
        print(i)
        pass
    dosen = input('apakah anda ingin melihat dosen yang mengajar?..')
    if dosen == 'y':
        nama_dosen = ['Rini,kom.M,kom','Akmal.S,kom.M,kom']
        for j in nama_dosen:
            print(j)
    elif dosen == 'n':
        pass
        
def minggu():
    print('libur')
    

menu()

            