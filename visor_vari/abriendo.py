
"""" Entrada para probar la ejecucion del programa """


"==========================================="

# sin ventana
from ejecutopcion.sin_ventana import ejecutando

"==========================================="

if __name__ == "__main__":
    
    opcion= 0
        
    def entra():
    
        if opcion == 1:
            
            holas= 1
            ejecutando(1, holas)
            
        elif opcion == 2:
            
            holas= 1
            ejecutando(2, holas)
            
        elif opcion == 3:
            
            holas= 1
            ejecutando(3, holas)
            
        elif opcion == 4:   # esta es la funcion que se da en paralelo
            
            holas= 2
            ejecutando(4, holas)

    #opcion= 1; print("ent_1")
    #entra()
    #opcion= 2; print("ent_2")
    #entra()
    #opcion= 3; print("ent_3")
    #entra()
    #opcion= 4; print("ent_4")
    #entra()

    import ejecutopcion.mi_trabajo.vent_adm 
    
