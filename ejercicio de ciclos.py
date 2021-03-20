# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:53:42 2021

@author: Jisus
"""

#leer una tabla de multiplicar e imprimir
# dicha desde el 1 hasta el 20 y sumar sus resultados . U
#sar para la solucion.

tabla = 0
multplicador= 1
resultado = 0
sumaResultado = 0
conRepCiclo = 1

#leer el numero de la tabla para la cual vamos a realizar las operaciones.

tabla = int(input("tabla: "))

multiplicador = int (input("Multiplicador : "))

#Inicio del ciclo repetitivo WHILE

while(conRepCiclo <= 20):
    resultado = tabla * conRepCiclo
    sumaResultado = sumaResultado + resultado
    print (tabla, "*" , conRepCiclo, "=" ,resultado)
    #incrementar la variable que control el ciclo 
    conRepCiclo = conRepCiclo + 1
print ("la suma de los resultados es: ", sumaResultado)

