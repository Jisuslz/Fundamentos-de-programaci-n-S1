# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:19:06 2021

@author: J H Nando L Z
"""
resultado = "si"
while resultado != "no":
    print ("""Bienvenido
    Menu
    1 Suma  
    2 Resta  
    3 Multiplicacion  
    4 Division  
    5 Ponteciacion 
    6 Salir """)
    opcion=int(input("oprima una de las opciones: "))
    #m = [1, 2, 3, 4, 5, 6]
    if opcion == 6:
        print("hasta la proxima")
        resultado= "no"
    else:
        a=int(input("Ingrese el primer numero para calcular: "))
        b=int(input("Ingrese el segundo numero para calcular: "))
    if opcion == 1:
        print("la suma es: ", a+b)
    if opcion==2:
        print("la resta es: ", a-b)
    if opcion==3:
        print("la multiplicacion es ", a*b)
    if opcion==4:
        print("la division es ",a/b)
    if opcion==5:
        print("la pontenciacio es: ",pow(a,b))
    resultado =input("ingrese 'si' o 'no' para realizar un nuevo calculo: ")
