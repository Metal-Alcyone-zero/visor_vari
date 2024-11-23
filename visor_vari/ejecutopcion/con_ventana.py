
""" Abro ventana y compruebo la libreria visor-vari """


"============================================="

import tkinter as tk

from visorquipus import gentil
from see import refer

"- - - - - - - - "

nada= None

def milu(etapa):
    
    if etapa == 1:
        refer.selda_0= 15
    
    if etapa == 2:
        refer.selda_0= 28

"============================================="

def minoury():
    
    milu(1)
    gentil(1, minipro)
    print("sacando la exprecion_divisora")
    milu(2)
    gentil(1, minipro)

def minou():
    
    milu(1)
    gentil(2, minipro)
    print("sacando la exprecion_divisora")
    milu(2)
    gentil(2, minipro)

minipro= tk.Tk()

bon_1= tk.Button(minipro, text= "pulso_1", command= minoury)
bon_1.pack()

bon_2= tk.Button(minipro, text= "pulso_2", command= minou)
bon_2.pack()

minipro.mainloop()

