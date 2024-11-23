
""" Ventana principal del visor de variables """


"========================================================"

# Depura: visor_vari.
from mas_bajo_nivel.variables_valores import base
from mas_bajo_nivel.clases_asistem import de_tres
from mas_bajo_nivel.variables_valores import todo

from mana.interfases_option.tipo_visor_1 import Tipo_uno
from mana.interfases_option.tipo_visor_2 import Tipo_dos
from mana.interfases_option.tipo_visor_3 import Tipo_tres
from mana.interfases_option.tipo_visor_4 import Tipo_cuatro

#from numero_para_ola.core_001 import Eninpulso

"- - - - - - - - - - - -"

#en_simple= Eninpulso()

def acop_nucleo(conment):
    
    def rebolu():
        
        conment
    
        def conmutacion_por_olas(numero): # por aqui pasan los dos ultimos.
            
            filtrado= "en_simple.exaltada(numero)"

            if filtrado != None:
                al_bloque_principal_visor_vari(filtrado)
                
        if base.argment_1 == 1:
            conmutacion_por_olas(0)
            conmutacion_por_olas(1)
        else:
            conmutacion_por_olas(base.argment_1)
            
    return rebolu
        
"========================================================"

class E_lenguaje_quipus:

    "......... Inicializando .........."

    def __init__(self, situacion):
        
        de_tres.situacion= situacion
                        
        self.iniciotekinte()

    def iniciotekinte(self):
        
        # abriendo modulos
        if base.tipo_visor == 1: # uno a uno
            print("caso _1...")
            Tipo_uno()
        
        elif base.tipo_visor == 2: # serie todos
            print("caso _2...")
            Tipo_dos()

        elif base.tipo_visor == 3: # serie puntual
            print("caso _3...")
            Tipo_tres(de_tres.situacion)
        
        elif base.tipo_visor == 4: # paralelo
            print("caso _4...")
            Tipo_cuatro()
        
        elif base.tipo_visor == 5: # paralelo, compacto
            print("caso _5...")
            #Tipo_cinco()

def al_bloque_principal_visor_vari(arg_1_transformado):
    E_lenguaje_quipus(arg_1_transformado)

"------------------------------------"

@acop_nucleo
def call_01():
    ""
        
class Entradas:
        
    def uno_de_cinco(self):
        al_bloque_principal_visor_vari(base.nada)
    
    def dos_de_cinco(self):
        al_bloque_principal_visor_vari(base.nada)
    
    def tres_de_cinco(self):
        al_bloque_principal_visor_vari(base.posi_driel)
        
    def cuatro_de_cinco(self):
        al_bloque_principal_visor_vari(base.nada)

    "- - - - - - - -"

    def cinco_de_cinco(self):
        ""

tipo= Entradas()

"------------------------------------"

def riel(posicion, atado= None):
    
    base.posi_driel= posicion
    base.posi_atada= atado

def ultimo_numero(act_num):
    
    if base.tipo_visor == 1:
        pass
    if base.tipo_visor == 2:
        pass
    if base.tipo_visor == 3:
        pass
    else:                   # Solo 4 emplean 'todo.limit'
        if act_num > todo.limit:
            todo.limit= act_num
        else:
            pass

def gentil(numero= None, extension= None, objet_supre= None):
    
    # depositando valores
    base.argment_1= numero          # Tiene dos maneras de ingresar al bloque P.
    base.argment_3= objet_supre     # Solo para la cuarta forma del visualizacion.

    # opciones
    
    if (numero == None) and (extension == None) and (objet_supre == None):
        
        base.tipo_visor= 1
        tipo.uno_de_cinco()
        
        base.argment_1= 1
    
    if (numero != None) and (extension == "serie") and (objet_supre == None):
        
        if base.posi_driel != None:
            
            base.tipo_visor= 3
            tipo.tres_de_cinco()
        else:
            base.tipo_visor= 2
            tipo.dos_de_cinco()

    if (numero != None) and (extension == "paralelo") and (objet_supre == None):
        
        base.tipo_visor= 4
        tipo.cuatro_de_cinco()

    "- - - - - - - -"

    if (numero != None) and (extension == "serie") and (objet_supre != None):
        
        if base.posi_driel != None:
            
            base.tipo_visor= 5
            tipo.tres_de_cinco()
        else:
            base.tipo_visor= 6
            tipo.dos_de_cinco()

    if (numero != None) and (extension == "paralelo") and (objet_supre != None):
        base.tipo_visor= 7

    # ultimo_numero(base.argment_1)

def ultimate():
    
    if base.tipo_visor == 4:
        
        todo.other_ola += 1
        base.enumer_geltil= 0

