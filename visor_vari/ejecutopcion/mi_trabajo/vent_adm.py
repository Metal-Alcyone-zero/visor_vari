
""" Este es un ejemplo de una ventana que muestra datos """


"============================================"

import tkinter as tk
from ejecutopcion.con_ventana_1 import abriendo

"============================================"

ventana= tk.Tk()

ventana.title("laguna")
ventana.geometry("500x400")

luto= tk.Button(ventana, text= "presiona para ingresar")
luto.pack()

abriendo(tk)

ventana.mainloop()

