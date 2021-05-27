# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 02:35:28 2021

@author: Jisus
"""

# c. Leer un rango (límite inferior y límite superior) e imprimir y sumar los valores del rango incluyendo los extremos.
# Ejemplo: Lee 3 y 6:  Imprime 2,3,5,8  Suma 18

#Prototipo y desarrollo
def rango_101202114852_102202114638_82202114279(): # se crea la funcion rango sin parametros
    a = 2 #Se crean las variables de la sucesión de fibonacci
    b = 3
    c = 5
    d = 8
    sumando = a + b + c + d #Se suman las variables anteriores para obtener un valor
    agrego = 18  # se crea la varible anexo para cargar el numero 18 en memoria para poder sumarlo
    rangos = int(input("Digite el rango limite superior o inferior: "))
    suma_total = sumando + rangos + agrego  # se crea la varible para sumar los rangos el agrego
    print(a, "+", b, "+", c, "+", d, "+", rangos, "=", suma_total) # se imprime el resultado de la suma de el ejercicio

#Llamado
rango_101202114852_102202114638_82202114279() #Se  imprime el resultado en pantalla