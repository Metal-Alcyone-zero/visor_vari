
""" programa que busca el promedio """


"==========================================="

from visor_vari.visorquipus import gentil, ultimate, riel
from visor_vari.see import refer

"==========================================="

def variables(limit):
    
    if limit >= 1:
        
        refer.selda_0= num
        refer.selda_1= otro_num
        refer.selda_2= 0
        refer.selda_3= adicional
        refer.selda_4= cuantos
        refer.selda_5= 0
    
    if limit >= 2:
    
        refer.selda_6= mas
        
    if limit >= 3:
        
        #refer.selda_7= otro_mas
        refer.selda_8= 0
        refer.selda_9= divisor
        refer.selda_10= primera_sum
        refer.selda_11= 0
        refer.selda_12= numerador
        
    if limit >= 4:
        
        refer.selda_13= numer
        refer.selda_14= divi


gentil(3, 'serie')

num= int(input("dime el 1° numero: "))

otro_num= int(input("dame otro numero: "))

adicional= 0
cuantos= 0

variables(1)
gentil(1, 'serie')

while True:

    mas= input("otro numero (si o no): ")

    if mas == "no":
        break
    
    if mas == "si":
        otro_mas= int(input("cual: "))

        adicional= adicional + otro_mas
        cuantos += 1

variables(2)
gentil(2, 'serie')

divisor= cuantos + 2

primera_sum= num + otro_num

try:
    numerador= primera_sum + adicional

except TypeError:
    numerador= primera_sum

variables(3)
gentil(3, 'serie')

numer= int(numerador); divi= int(divisor)

salida= numer // divi

print(salida)
variables(4)
gentil(1, 'serie')

x= input("presione enter para salir ")

