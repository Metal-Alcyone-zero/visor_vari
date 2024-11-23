
""" visor_vari opcion primera (unica) """


if True: # Descripcion
    """
    Este modulo trabaja sin sacar una ventana.
    muestra el dato por consola.
    """

"====================================================="

from mana.elementos_de_conducto.conducto_uno import *

"====================================================="

class Tipo_uno:
    
    def __init__(self):
        
        objeto= tk.Tk()
        ini.objeto_tk= objeto
        
        linea.de_ventana= 1
        
        objeto.geometry("200x25")
        objeto.title ("diseñemos programas")

        self.primer_marco= tk.LabelFrame(objeto, bd= 0)
        self.primer_marco.pack(expand= True, fill= tk.BOTH)
        
        burbuja.boton_mues(self.primer_marco)
        
        objeto.mainloop()

        
