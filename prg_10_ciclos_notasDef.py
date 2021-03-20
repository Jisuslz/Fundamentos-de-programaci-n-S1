# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:36:40 2021

@author: Jisus
"""

#programa que calcula las notas de un estudiante 
#Entradas
#Pedir el nombre del estudiante y sus parcialesinput()

canEst=int(input("cantidad de estudiante : "))
#Inicializar la variable que controla el ciclo
conRep=0
sumDefGru=0.0

proDefGru=0.0
while(conRep < canEst):
    #Instruciones a repetir
    nomEst=input("nombre estudiante:  ")
    notUnoEst= float(input("parcial Uno: "))
    notDosEst= float(input("parcial Dos: "))
    notTresEst= float(input("parcial Tres: "))

    #Calculos
    notDefEst = (notUnoEst+notDosEst+notTresEst)/3
    
    sumDefGru=sumDefGru+notDefEst

    #Imprimir los resultados - Salidas

    print (f"1. la nota definitiva es: {notDefEst:.2f} ")
    
    #Incrementar la variable que controla el ciclo 
    conRep = conRep+1

#calcular el promedio del grupo
notProDefGru = sumDefGru/canEst

#imprimir la nota promedio del grupo
print (f"2. la nota promedio del grupo es: {notProDefGru:.2f}")