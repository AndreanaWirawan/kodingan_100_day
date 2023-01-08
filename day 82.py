import tkinter as tk
form = tk.Tk()
form.title("Form Login")
form.geometry("300x200")


label1 = tk.Label(form, text="Username")
label1.pack()

entry1 = tk.Entry(form)
entry1.pack()

label2 = tk.Label(form, text="Password")
label2.pack()

entry2 = tk.Entry(form, show="*")
entry2.pack()

btn = tk.Button(form, text="Login", command='Login')
btn.pack()

form.mainloop()




