from tkinter import *

def selec():
    monitor.config(text="Opcion {}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text='')

window=Tk()
window.config(bd=15)

opcion=IntVar()

Radiobutton(window, text='opcion 1', variable=opcion, value=1, command=selec).pack()
Radiobutton(window, text='opcion 2', variable=opcion, value=2, command=selec).pack()
Radiobutton(window, text='opcion 3', variab1e=opcion, value=3, command=selec).pack()
Button(window, text="Reiniciar", command=reset).pack()

monitor=Label(window)
monitor.pack()
window.mainloop()