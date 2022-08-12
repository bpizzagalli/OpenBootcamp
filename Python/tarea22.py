from tkinter import *

window=Tk()

lista=Listbox(window)

for item in ['iPhone', 'Samsung', 'Motorola', 'Lenovo']:
    lista.insert(END, item)
    lista.pack()

label=Label(text="Lista de marcas")
label.pack()
window.mainloop()