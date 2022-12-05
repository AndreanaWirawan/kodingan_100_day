import mysql.connector

conn=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'wirawan'
)

cursor=conn.cursor()
#perintah untuk menbuat database
db = input("masukan nama database: ")
cursor.execute(f'create database {db}')

#perintah untuk mengaktifkan database
db1 = input("masukan database yang ingin di aktifkan : ")
cursor.execute('use {db1}')

#perintah untuk menghapus database
db2 = input("masukan database yang ingin di hapus : ")
cursor.execute('drop database {db2}')

#perintah untuk membuat tabel
cursor.execute(
    '''
    CREATE TABLE andre_tbtransaksi(
    no_faktur char (10) not null,
    tanggal date not null,
    kode_pelanggan char (10) not null,
    kode_barang char (10) not null,
    jumlah_barang int (5) not null
    )
    '''
)

#perintah untuk mengisi tabel
cursor.execute('''insert into andre_tbtransaksi(no_faktur,tanggal,kode_pelanggan,kode_barang,jumlah_barang) 
values
('FA0001','2021/12/12','PL0001','B0001','4'),
('FA0001','2021/12/12','PL0001','B0002','3'),

('FA0002','2022/01/01','PL0002','B0001','2'),
('FA0002','2022/01/01','PL0002','B0003','5'),

('FA0003','2022/01/01','PL0003','B0004','2'),
('FA0003','2022/01/01','PL0003','B0003','5'),
('FA0003','2022/01/01','PL0003','B0005','1')
''')
conn.commit()                 
                   
print('database berhasil')
