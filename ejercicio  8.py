# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:41:26 2021

@author: J H Nando L Z
"""

#  Calcular la fuerza que se debe aplicar a un cuerpo para moverlo en una mesa horizontal,
#  sabiendo que tiene una masa m (kg) y un coeficiente de rozamiento estático  Us.
#[ F ] = [ m ] . [ a ]
#[ F ] = kg m s-2
#= N
#La unidad de fuerza es el Newton (N) cuando la masa se mide en kilogramos (kg) y la
#aceleración en metros por segundos al cuadrado (m/s2
#).

#entrada
PNewton = int(input("inresa el peso: " ))
rosamientoestatico = float(input("ingresa el rosamieno estatico :"))
fuerzahorizontal = int(input("cual es la fuerza horizonotal :"))

masa = PNewton
gravedad = 10
peso = masa * gravedad
fuerzaderozamiento = rosamientoestatico * peso 

if fuerzaderozamiento >= fuerzahorizontal:
    print("el peso es de  :", peso , "en newton del articulo")
    print("la fuerza de rozamiento estatico para la fuerza aplicada es de  :", fuerzaderozamiento ,)
    print("felicidades con  :", fuerzahorizontal , "newton vas a poder mover")
    
else:
    print("no se puede mover")