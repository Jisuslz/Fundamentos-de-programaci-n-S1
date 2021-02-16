# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:15:32 2021

@author: J H Nando L Z
"""

#Calcular el sueldo total a recibir de un empleado.  El usuario deberá ingresar el número de horas trabajadas
# y el valor por cada hora. Considere en los cálculos el descuento de seguridad social y una bonificación del 2%
# para aquellos cuyo sueldo no supere los 300 dólares.

#entrada
resultado = "si"
while resultado != "no":
    print ("""Bienvenido""")
    horas=float(input("ingresa las horas trabajadas: "))
    valor=float(input("ingresa el valor por cada hora: "))
    suelto_total= horas*valor
    salud=suelto_total* 4/100
    bonificación=suelto_total*2/100
    sueldo_bonificacion= bonificación+suelto_total
    if suelto_total < 1048950 :
        print("Descuento por salud: ",salud )
        print ("Salud: 12,5%= el empleador paga el 8,5% y el trabajador el 4%")
        print ("sueldo + bonificacion ",sueldo_bonificacion)
        print ("bonificacion :",bonificación)
    else:
        print("sueldo",suelto_total)
        resultado= "no"
    
    
    #a=int(input("Ingrese el primer numero para calcular: "))
       # b=int(input("Ingrese el segundo numero para calcular: "))
    #if opcion == 1:
        #print("la suma es: ", a+b)
    