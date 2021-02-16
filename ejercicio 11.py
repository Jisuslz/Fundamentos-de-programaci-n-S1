# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:44:19 2021

@author: J H Nando L Z
"""

#Calcular las raíces de una ecuación cuadrática.  Suponga que los datos ingresados no generan raíces imaginarias.


# formula  x = (-b + (b*b - 4*a*c)ˆ(1/2))/(2*a)
#Entrada

a = int(input("Ingrese un primer valor a: "))
b = int(input("Ingrese un segundo valor b: "))
c = int(input("Ingrese un tercer valor c: "))

#Proceso

x1 = (-b + (b*b - 4*a*c) ** (1/2)) / (2*a)
x2 = (-b - (b*b - 4*a*c) ** (1/2)) / (2*a)

#Salida

print("la primera Raiz es: ", x1)
print("la segunda Raiz es: ", x2)






