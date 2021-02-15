# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:05:39 2021

@author: J H Nando L Z
"""

# Realice un programa que resuelva lo siguiente: Si n Empleados  realizan
# una actividad en k horas, ¿cuántos empleados se necesitarán para realizar 
#la misma 5?

#Entrada
cantidad_emple = int(input("ingrese la cantidad de trabajadores que estan realizando la actividad: "))
h=int(input ("ingresa la catidad de horas que llevan realizando la actividad: "))

#proceso
necesita = cantidad_emple*h
necesi=necesita-cantidad_emple

if necesi >= 1:
    print("se necesita: ", necesi)
    print("para realizar la actividad en una hora")
else:
    print("no es necesario mas personal")



#print(" Realice un programa que resuelva lo siguiente: Si n Empleados  realizan una actividad en k horas, ¿cuántos empleados se necesitarán para realizar la misma actividad en k1 horas? ")