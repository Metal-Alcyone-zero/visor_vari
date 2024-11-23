
""" instalaciones que componen la configuracion principal """


"=========================================="

import tkinter as tk

"- - - - - - - - - - - "

class Principio:

    def __init__(self):
                
        self.objeto_tk= None
        self.seg_tkven= None
        
        self.caso= 1
        self.fase= 0
        
        self.obj_paracaso_2= None

ini= Principio()

"=========================================="

class Paso:
    
    def __init__(self):
                
        self.escalon= 1
        self.cambio_de_fase= False
        self.sub_cuenta= 0
        
        self.entrada= 0
        self.fase= 0

        self.conteo_de_las_entradas= 0

pulso= Paso()


class Linea_viva:
    
    def __init__(self):
        
        self.de_ventana= 0
        self.sub_numero= 1
        self.enau_ment= 0
        
        self.contador_3= 0

linea= Linea_viva()


class Almacenaje:
    
    def __init__(self):
        
        self.nada= None
        
        self.argment_1= None
        self.argment_3= None

        self.tipo_visor= 0
        
        self.unapasada_para_2= True
        self.sumador_de_2= 0
        self.activo_para_2= False
        
        self.posi_driel= None
        self.posi_atada= None
        self.enumer_geltil= 0

base= Almacenaje()


class Flujo:
    
    def __init__(self):
        
        self.limit= 0
        self.other_ola= 1
    
todo= Flujo()


class Primer:
    
    def __init__(self):
        
        self.dato_a= None
        self.llave= True
        
        self.dale_puntual= False
        self.entry_modifor_4= False

primer_gent= Primer()

