import tkinter
from tkinter import *
from tkinter import ttk

window = tkinter.Tk()
window.title("Biodata Diri")
window.geometry("600x700")

tabel = Label(window, text="Setting").place(x=130, y=50)
judul = Label(window, text="sending of massage from", font=20).place(x=215, y=10)
setting = Label(window, bg="white", height=5, width=50).place(x=125, y=80)
mode = Label(window, text="Mode :", bg="silver").place(x=130, y=90)
kode = ttk.Combobox(window, width=7).place(x=180, y=90)
subject = Label(window, text="Subject :", bg="silver").place(x=130, y=125)
kode = ttk.Combobox(window, width=5).place(x=190, y=125)
koneksi = Label(window, text="Connection :", bg="silver").place(x=285, y=90)
kode = ttk.Combobox(window, width=5).place(x=370, y=90)
remote = Label(window, text="Remote Ip :", bg="silver").place(x=285, y=125)
kode = ttk.Combobox(window, width=6).place(x=365, y=125)
kirim = Label(window, text="kirim").place(x=435, y=125)
setting = Label(window, bg="silver", height=15, width=20).place(x=120, y=200)
setting = Label(window, bg="gray", height=15, width=20).place(x=335, y=200)

window.mainloop()