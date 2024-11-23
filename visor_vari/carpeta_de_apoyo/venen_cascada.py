
""" Ventana principal que elimina 
    de una sola vez
    todas las sub-ventanas que tiene a su cargo. """


"=========================================="

from carpeta_de_apoyo.control import ver_registro
from mas_bajo_nivel.variables_valores import ini, linea, tk

"=========================================="

def mini_muestra():
            
    def mirar_las_varis():
        print("presiono boton "); print(end= " ")
        ver_registro(tk)

    def boton_muestra ():
        
        panel_control= tk.LabelFrame(primer_marco)
        panel_control.pack(anchor= "w")

        boton_para_crear_nuevo_carapter= tk.Button (panel_control, text= "mostrar carapteres", command= mirar_las_varis)
        boton_para_crear_nuevo_carapter.config(padx= 24)
        boton_para_crear_nuevo_carapter.pack ()

    print("aqui")
    jeto_tk= tk.Tk()
    ini.objeto_tk= jeto_tk
    
    jeto_tk.geometry("200x25")
    jeto_tk.title (str(ini.caso))

    primer_marco= tk.LabelFrame(jeto_tk, bd= 0)
    primer_marco.pack(expand= True, fill= tk.BOTH)

    boton_muestra()

    jeto_tk.mainloop()

