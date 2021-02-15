# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:21:48 2021

@author: J H Nando L Z
"""



# EJERCICIO 4
#* Realice un programa que obtenga la calificación 
# que debe obtenerse en un examen supletorio, 
# si se conoce que el promedio incluido el supletorio
# para aprobar debe ser mínimo de 3.5 . 
# El usuario debe ingresar las calificaciones 
# en números enteros del primer y segundo bimestre. 

bi1 = int(input("Ingrese sus calificaciones para el Bimestre 1 "))
bi2 = int(input("Ingrese sus calificaciones para el Bimestre 2 "))

prom = (bi1 + bi2) / 2

if prom < 3.5:
    print("Su promedio en las notas es de:", prom)
    print("Debe repetir la carrera")
else:
    print("Felicidades!!!, Pasaste con: ", prom)
    
    #OTRA FORMA 
    
    # Realice un programa que obtenga la calificación que debe 
#obtenerse en un examen supletorio, si se conoce que el promedio
# incluido el supletorio para aprobar debe ser mínimo de 3.5 . 
#El usuario debe ingresar las calificaciones en números enteros 
#del primer y segundo bimestre.


#entrada
nota_s1 = float(input ("ingresa su nota del primer semestre: "))
nota_s2 = float (input("ingresa nota del segundo semestre: "))

#proceso
aprobado = nota_s1+nota_s2 >= 3.5
no_aprobado = nota_s1+nota_s2 <3.5
nota_pganar = no_aprobado-3.5


#Salida
print ("aprobado no es necesario sacar mayor nota: ",aprobado)
print ("nota deficiente para ganar la materia: ",no_aprobado)
print ("nota que debe obtener en el examen como minimo: ",nota_pganar)
