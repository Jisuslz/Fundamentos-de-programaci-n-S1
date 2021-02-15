# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:55:13 2021

@author: J H Nando L Z
"""

#Realice un programa que obtenga el índice de masa 
#corporal de una persona, ingresando la estatura en 
#centímetros y el peso en kilos.

#entrada

peso = float(input ("ingresa su peso: "))
Estatura = float(input("ingresa su estatura: "))

#proceso
calculo = peso/Estatura**2

#Salida 
print ("su peso es: ",peso)
print ("su estatura es: ",Estatura)
print ("IMC")
print ("su masa corporal es: ",calculo)

