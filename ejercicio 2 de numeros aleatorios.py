# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:38:50 2021

@author: Jisus
"""
import random
# leer N , generar aleatorios y calcular suma y promedio 

#Area de definicion de variables 

cantidadNumeros=0
contadorRepeticionesWhile=0
acumuladorSuma=0
promedioNumerosAleatorios=0.0
numero=0

#variables segunda parte del ejercicio
acumuladorPositivos=0
acumuladorNegativos=0
promedioPositivos=0.0
promedioNegativos=0.0
contadorPositivos=0
contadorNegativos=0

#varaible tercera parte del ejercicio
mayorpositivos=0
mayornegativos=0
menorpositivos=100
menornegativos=0

#Entradas 
cantidadNumeros=int(input("cantidad de numeros: "))

#procesos
#ciclo whie

while contadorRepeticionesWhile<cantidadNumeros:
    numero = random.randint(0,100)
    acumuladorSuma=acumuladorSuma+numero
    #segunda parte del ejerciico
    if numero>0:
        print("numero positivos: ",numero)
        acumuladorPositivos=acumuladorPositivos+numero
        contadorPositivos=contadorPositivos+1
        # Identificar el mayor de los positivos
        if numero>mayorpositivos:
            mayorpositivos=numero
        #identificar el menor de los positivos
        if numero<menorpositivos:
            menorpositivos=numero
        #fin tercera parte del ejercicio
    else:
        print ("numero negativos: ",numero)
        acumuladorNegativos=acumuladorNegativos+numero
        contadorNegativos=contadorNegativos+1
        #Identificar el mayor de lo negativos
        if numero>mayornegativos:
            mayornegativos=numero
        #Identificar el menor de los negativos
        if numero<menornegativos:
            menornegativos=numero  
    #Fin de la segunda parte del ejercicio
    contadorRepeticionesWhile=contadorRepeticionesWhile+1
#fin del ciclo
promedioNegativos=acumuladorNegativos/contadorNegativos
promedioPositivos=acumuladorPositivos/contadorPositivos
promedioNumerosAleatorios=acumuladorSuma/contadorRepeticionesWhile

#Salida de todos los numeros
print ("Suma de Numeros Aleatorios: ",acumuladorSuma)
print("proemdio de Numeros Aleatorios: ",promedioNumerosAleatorios)

#Salidas de todos los numeros positivos
print ("cantidad numeros possitvos: ",contadorPositivos)
print ("suma de numeros positivos: ",acumuladorPositivos)
print ("promedio de nuemros positivos: ",promedioPositivos)

#Salida de todos los numeros negativos
print ("cantidad numero negativos: ",contadorNegativos)
print ("la suma de numeros negativos: ",acumuladorNegativos)
print ("el promedio de los numeros negativos son: ",promedioNegativos)

#imprimir mayor de los positivos y menor de los positivos
print("Mayor de los positivos ",mayorpositivos)
print("menor de los positivos",menorpositivos)

#imprimir mayor de los negativos y menor de los negaticos 
print("Mayor de los positivos ",mayornegativos)
print("menor de los positivos",menornegativos)