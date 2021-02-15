# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:36:13 2021

@author: J H Nando L Z
"""

#Calcular la velocidad a la que debe ir un vehículo
# para recorrer una distancia d en un tiempo t.

#entrada

distancia = float(input("ingresa la distancia que a recorrido: "  "hh:mm:  ")) 
tiempo= float(input ("ingresa el tiempo que ha viajado en horas : "))
#proceso
velocidad = distancia//tiempo 

#salida
print ("la velocidad es : ",velocidad,"Kilometros por hora")










#Las fórmulas de la velocidad, la distancia y el tiempo:
#V = S / T;   S = V * T;   T = S / V;
#donde V es la velocidad, S es la distancia, T es el tiempo




#Resuelve un problema usando la siguiente fórmula. Por ejemplo,
# si un coche viaja a 60 millas (96 km/h) y el viaje tarda 2 horas,
# puedes calcular fácilmente la distancia 
#recorrida: Distancia = 60 mph x 2 horas (o 96 km/h x 2 horas) 
#Distancia = 120 millas (192 km)