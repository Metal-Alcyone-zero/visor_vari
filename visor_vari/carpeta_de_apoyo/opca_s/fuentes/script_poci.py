
""" codigo que muebe la operacion de pociciones 
    que se entienden bajo el concepto de rieles """
    

"============================================"

from mas_bajo_nivel.variables_valores import base, todo
from mas_bajo_nivel.variables_valores import primer_gent

"============================================"

class Esenario_de_pociciones:

    def riel_de_serie(self):

        if base.posi_atada != None:
            if base.enumer_geltil == base.posi_atada:
                primer_gent.dale_puntual= True

        if base.enumer_geltil == base.posi_driel:
            primer_gent.dale_puntual= True
        else:
            base.enumer_geltil += 1
        
    def riel_de_paralelo(self):
        
        if base.posi_driel != None:

            "- - - - - - - -"
            
            if isinstance(base.posi_driel, list):
                print("el dato es list"); print()
                
                def saco_elemento_de_dict():
                    
                    print(todo.other_ola, base.posi_driel)
                    posi_riel= base.posi_driel[todo.other_ola]
                    
                    return posi_riel
                    
                por_dict= saco_elemento_de_dict()
                #comparo= por_dict + 1
                
                if base.enumer_geltil == por_dict:
                    primer_gent.entry_modifor_4= True
                else:
                    base.enumer_geltil += 1
                
                # (este angulo actua) empleando una lista
                
            else: # con riel normal
            
                if base.posi_atada != None:
                    if base.enumer_geltil == base.posi_atada:
                        primer_gent.entry_modifor_4= True
                    
                if base.enumer_geltil == base.posi_driel:
                    primer_gent.entry_modifor_4= True
                else:
                    base.enumer_geltil += 1
                    
        else: # sin riel
            primer_gent.entry_modifor_4= True

actor_02= Esenario_de_pociciones()

