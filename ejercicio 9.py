# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:15:49 2021

@author: J H Nando L Z
"""


resultado="si"
while resultado !="no":
    print("""Bienvenido
          Menu
          1 conversion de Celsius a grados Kelvin
          2 conversion de Celsius a Farenheit
          3 conversion de Kelvin a Farenheint
          4 Para salir """)
    opcion=int (input("oprima de una de las opciones: "))
    if opcion == 5:
        print("hasta la proxima")
        resultado= "no"
    else:         
        C=int(input("Ingresa el dato a convertir   "))
    if opcion==1:
        print ("la conversion de C a grados Kelvin es:  ",C-273.15,"K")
    if opcion==2:
        print("la conversion de C a grados Farenheit es: ",C*9/5+32,"°F")
    if opcion==3:
        print ("la conversion de K a grados °F es: ",C*9/5-459.67,"°F")
    resultado =input("ingrese 'si' o 'no' para realizar un nuevo calculo: ")
        
        
#Leer la temperatura en grados Celsius y convertirla a grados Kelvin y a grados Farenheit