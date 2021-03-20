# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:21:48 2021

@author: Jisus
"""
#Escribir un programa que calcule la suma de los cuadrados de los 100
# primeros números enteros.
cuadrado = 1
conRepCiclo = 0
multiplicador = 1
suma=0

while conRepCiclo<=100:
    print(conRepCiclo, "al cuadrado es :",cuadrado)
    conRepCiclo = conRepCiclo + 1 * multiplicador
    cuadrado =  conRepCiclo ** 2 
    suma=suma + cuadrado
print ("suma",suma)