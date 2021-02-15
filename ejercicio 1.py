# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:30:02 2021

@author: J H Nando L Z
"""
#entrada
compra_neto = int(input("ingresar el monto neto: "))


#proceso 
IVA = compra_neto *19 /100
total = IVA+compra_neto
Descuento = total *5/100
total_Des = Descuento - total


#Salida 
print ("el total con IVA es : ",total)
print ("con el descuento es: ",total_Des)