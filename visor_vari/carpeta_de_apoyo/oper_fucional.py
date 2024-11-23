
""" Metodos creados para dar apoyo al modulo principal de
    la libreria """
    

"========================================================"

from mas_bajo_nivel.variables_valores import ini
from mas_bajo_nivel.variables_valores import ini, base
from mas_bajo_nivel.variables_valores import pulso
from mas_bajo_nivel.clases_asistem import termi_2

from carpeta_de_apoyo.revisar import ver_registro

from mas_bajo_nivel.variables_valores import tk

"========================================================"

class Asiste:

    def boton_muestra(self):
        
        self.panel_control= tk.LabelFrame(self.primer_marco)
        self.panel_control.pack(anchor= "w")

        boton_para_crear_nuevo_carapter= tk.Button (self.panel_control, text= "mostrar carapteres", command= self.mirar_las_varis)
        boton_para_crear_nuevo_carapter.config(padx= 24)
        boton_para_crear_nuevo_carapter.pack ()

    def boton_mues(self, marco):
        print("aqui_1")
        
        self.panel_control= tk.LabelFrame(marco)
        self.panel_control.pack(anchor= "w")

        boton_para_crear_nuevo_carapter= tk.Button (self.panel_control, text= "mostrar carapteres", command= self.mirar_las_varis)
        boton_para_crear_nuevo_carapter.config(padx= 24)
        boton_para_crear_nuevo_carapter.pack ()

    def mirar_las_varis(self):
        ver_registro(tk)

    def destruye_ventanas(self):
        
        self.panel_control= tk.LabelFrame(ini.objeto_tk)
        self.panel_control.pack(anchor= "w")

        boton_para_crear_nuevo_carapter= tk.Button (self.panel_control, text= "Destruir ventanas", command= self.destruye)
        boton_para_crear_nuevo_carapter.config(padx= 24)
        boton_para_crear_nuevo_carapter.pack ()
        
    def destruye(self):
        ini.objeto_tk.destroy()

burbuja= Asiste()

"- - - - - - - - - - -"

def enumer_sub():
    
    if True: # Detecto...
        
        if base.argment_1 != pulso.escalon:
            pulso.cambio_de_fase= False
        
        else: # si son iguales "disloco" para demostrar
            pulso.escalon += 1
            pulso.cambio_de_fase= True
            base.activo_para_2= True
            
    if True: # Si hay un cambio, cuento
        
        if pulso.cambio_de_fase == False:
            pulso.sub_cuenta += 1
            termi_2.enau_ment += 1
        else:
            pulso.sub_cuenta= 1
            termi_2.enau_ment += 1
        
    if pulso.cambio_de_fase == True: # igualando, para poder entrar.
        pulso.entrada += 1

"- - - - - - - - - - -"

def numero_de_ola():
    
    ""