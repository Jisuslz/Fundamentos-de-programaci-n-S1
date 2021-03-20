# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:57:08 2021

@author: Jisus
"""

#Se ingresan un conjunto de n alturas de personas por teclado. 
#Mostrar la altura promedio de las personas.

suma=0
x=1
n=int(input("ingresar el total de personas: "))
while x<=n:
    altura=float(input("ingresa la altura: "))
    suma=suma+altura
    x=x+1
promedio=suma/n
print("la estatura promedio es: ")
print (promedio)