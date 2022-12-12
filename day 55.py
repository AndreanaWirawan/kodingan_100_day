import mysql.connector

conn=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'kelompok2'
)

cursor=conn.cursor()
# cursor.execute('create database kelompok2')
# cursor.execute(
#     '''
#     CREATE TABLE anggota_kelompok(
#     nama varchar (20) not null,
#     nim char (10) not null,
#     alamat varchar (20) not null
#     )
#     '''
# )
# cursor.execute('''insert into anggota_kelompok(nama,nim,alamat)
#                values
#                ('putu','D0221068','topoyo')
#                '''
#                )
# conn.commit()

# update = "update anggota_kelompok set nama='andre', nim='D0221069', alamat='majene' where nama='putu'"
# cursor.execute(update)
# conn.commit()

# cursor.execute('select*from anggota_kelompok')
# hasil = cursor.fetchall()
# for i in hasil:
#     print(i)

# cursor.execute('drop database kelompok2')  
# cursor.execute('drop table anggota_kelompok') 
 
print('Program Berhasil')
