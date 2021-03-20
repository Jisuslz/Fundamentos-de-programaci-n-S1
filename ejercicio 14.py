# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:01:24 2021

@author: Jisus
"""

base = 10
exponente = 30
potencia = 1
conRepCiclo = 0
suma=0

while conRepCiclo <= exponente: 
         potencia = potencia*base
         exponente=exponente
         print("Potencia de 10 a la", conRepCiclo," * ",potencia) 
         conRepCiclo=conRepCiclo+1
         suma=potencia + potencia

print ('Se calcula la potencia de 10^^30, cuyo resultado es :',suma)