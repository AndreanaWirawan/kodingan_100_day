import mysql.connector

conn=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'putu'
)

cursor=conn.cursor()
cursor.execute('create database putu')
cursor.execute('use putu')
cursor.execute(
    '''
    CREATE TABLE mahasiswa(
    nim CHAR (10) NOT NULL PRIMARY KEY,
    nama VARCHAR (25) NOT NULL,
    email VARCHAR (30) NOT NULL,
    alamat VARCHAR (30) NOT NULL
    )
    '''
)
cursor.execute('''insert into mahasiswa(nim,nama,email,alamat) 
values
("D0221068","ANDRE","wirawanandre","Topoyo")''')
conn.commit()
              
print('database berhasil')
