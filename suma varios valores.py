# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Escribir un programa que solicite ingresar 10 notas de alumnos y 
#nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
altas=0
bajas=0
x=1
while x<=10:
    nota=float(input("ingrese las notas:  "))
    if nota>=7:
        altas=altas+1
        x=x+1
    else:
        bajas=bajas+1
        x=x+1
print ("total de notas altas")
print (altas)
print ("total de notas bajas")
print (bajas)

    
