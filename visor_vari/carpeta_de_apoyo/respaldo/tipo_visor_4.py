
""" visor_vari opcion tercera (Separacion paralela) """


if True: # Descripcion
    """ 
    Muestra los datos segun el numero
    del comando que tenga "gentil",
    si se corresponde con el numero de la ola.
    """

"====================================================="

from mana.elementos_de_conducto.conducto_cuatro import *

"====================================================="

class Tipo_cuatro:
    
    def __init__(self):
        
        dale_a= 1
        
        if dale_a == 1: # original
        
            def alter_vent():
                
                ini.objeto_tk= tk.Tk()
                
                #desaparece.withdraw()
                
                burbuja.destruye_ventanas()
                
                ini.objeto_tk.mainlook()

            def vent_de_seccion():
                
                colateral= Thread(target= alter_vent)
                colateral.start()
                #primera_sub_ventana()
                
            enumer_sub()
            
            print(pulso.entrada)
            
            if base.argment_1 == pulso.entrada: # Ejecuto ventana
                                            
                if (base.argment_1 == 1) and (termi_2.pared_a == True):
                    termi_2.pared_b= True
                
                if (base.argment_1 == 1) and (termi_2.pared_a == False):
                    termi_2.pared_a= True
                    
                
                if termi_2.pared_b == False:
                    
                    ""
                    termi_2.pared_b= True
                    
                else:
                    if base.activo_para_2 == 1:
                        ""
                
                ini.caso= base.argment_1
                linea.sub_numero= pulso.sub_cuenta
                #linea.de_ventana= int(termi_2.enau_ment)
                linea.de_ventana= 1
                
                print(ini.caso, linea.sub_numero, linea.de_ventana)
                print(pulso.cambio_de_fase)
                
                termi_2.acumula= linea.sub_numero - 1
                
                # Deteta final...
                
                if base.argment_1 == 1:
                
                    if linea.sub_numero == 1:
                        
                        print("saco ventanas")
                        #vent_de_seccion()
                        #self.mirar_las_varis()
                    
                    else:
                        print("another oction")
                        #self.mirar_las_varis()
                
                else:
                    if linea.sub_numero == 1:
                        
                        if via_2 == False:
                            via_1= False
                        
                        if via_1 == False:
                        
                            colateral= Thread(target= alter_vent)
                            colateral.start()
                        
                            self.mirar_las_varis()
                            via_2= True
                            
                        if via_1 == True: # 
                            
                            ""
                            via_2= False
                        
                    else:
                        via_1= False
                        self.mirar_las_varis()
        
        if dale_a == 2: # con la linea beta anterior aparentaba funcionar
        
            def vent_deseccion():
                primera_sub_ventana()
                    
            if (base.activo_para_2 == True) and (base.argment_1 == 1):
                base.unapasada_para_2= False

            if base.unapasada_para_2 == True:
                
                enumer_sub()
                
                if base.argment_1 == pulso.entrada: # Ejecuto ventana
                    
                    
                    print("en un solo pase...")
                                                            
                    ini.caso= base.argment_1
                    linea.sub_numero= pulso.sub_cuenta
                    linea.de_ventana= termi_2.enau_ment
                    
                    print(ini.caso, linea.sub_numero, linea.de_ventana)
                    
                    # Deteta final...
                    
                    if ini.caso == termi_2.anterior_a:
                        print("hola_1")
                    else:
                        # comp
                        
                        # ejecuto
                        print("hola_2")
                        vent_deseccion()
                        termi_2.anterior_b += 1
                        #termi_2.anterior_a += 1
                    
                    # conteniendo elementos"""
                    
            else:
                if termi_2.solo_asi == True:
                    
                    print("hola_3")
                    vent_deseccion()
                    termi_2.solo_asi= False
            
