import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Hai Broo!!!")
window.geometry("600x300")


label1 = Label(window, text="Nim").place(x=225, y=40)
label2 = Label(window, text="Nama").place(x=225, y=60)
label3 = Label(window, text="kelompok").place(x=225, y=80)

entry1 = Entry(window, width=20).place(x=300, y=40)
entry2 = Entry(window, width=20).place(x=300, y=60)
entry3 = Entry(window, width=20).place(x=300, y=80)

Label = tkinter.Label(window, text="Biodata Diri", font=20,fg="black").place(x=300, y=0)
Label = tkinter.Label(window, text="Jurusan", font=20,fg="black").place(x=325, y=110)

sipil = Radiobutton(window,text ="Teknik Sipil", value = 1).place(x= 200, y =140)
inf = Radiobutton(window,text ="Informatika", value = 2).place(x= 310, y =140)
pwk = Radiobutton(window,text ="PWK", value = 3).place(x= 440, y =140)

Tombol1 = tkinter.Button(window, text="Kirim").place(x=335, y=180)
window.mainloop()