
""" Aqui alojare una clase que controle con poliformismo
    los diversos procesos """
    
    
"========================================="

from dominio.del_segundo_proceso.swicheo_entre_poliforma import otra_ventana as otv_2

"========================================="

class Control:
    
    def del_proceso_dos(self, dato):
        otv_2(dato)
        
    def del_proceso_tres(self):
        ""
        
acto_01= Control()

