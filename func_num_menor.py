# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:28:34 2021

@author: Jisus
"""

#Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
def tres_reales ():
    num1=int(input("ingresa el primeror numero: "))
    num2=int(input("ingresa el segundo numero:  "))
    num3=int(input("ingresa el tercer numero: "))
    print("Menor de los tres")
    if num1<num2 and num1<num3:
        print(num1)
    else:
        if num2<num1 and num2<num3:
            print(num2)
        else:
            if num3<num1 and num3<num2:
                print(num3)
                
            
for i in range (2):
    tres_reales ()