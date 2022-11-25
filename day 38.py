import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Biodata Diri")
window.geometry("300x400")


label1 = Label(window, text="Nama").place(x=130, y=50)
label1 = Label(window, text="Password").place(x=120, y=115)

entry1 = Entry(window, width=30).place(x=60, y=75)
entry1 = Entry(window, width=30).place(x=60, y=140)

kelamin = Checkbutton(window, text="Laki-laki").place(x=55, y=190)
kelamin = Checkbutton(window, text="Perempuan").place(x=160, y=190)

Label = tkinter.Label(window, text="Login", font=40,fg="black", bg="green").place(x=125, y=10)

Tombol3 = tkinter.Button(window, text="Kirim").place(x=130, y=250)

window.mainloop()