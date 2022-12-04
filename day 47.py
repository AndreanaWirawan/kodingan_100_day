import mysql.connector

conn=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'tugas3_D0221068_andreana'
)

cursor=conn.cursor()
cursor.execute('create database tugas3_D0221068_andreana')
cursor.execute('use putu')
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
