# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:16:57 2021

@author: Jisus
"""

#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa 
#que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y
# cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

sueldo_basico=0
sueldo_bruto=0
gastos=0
x=1
n=int(input("ingresa la cantidad de tabajadores: "))
while x<=n:
    sueldo=float(input("ingrese los sueldos: "))
    if sueldo>300:
        sueldo_bruto=sueldo_bruto+1
        x=x+1
    else:
        sueldo_basico=sueldo_basico+1
        x=x+1
    gastos=gastos+sueldo
print("total de trabajadores que ganan entre $100 y $300")
print(sueldo_basico)
print("total de trabajadores que ganan mas de $300")
print(sueldo_bruto)
print("informe de total de nomina: ")
print (gastos)





#while x<=10:
 #   nota=float(input("ingrese las notas:  "))
  #  if nota>=7:
   #     altas=altas+1
    #    x=x+1
    #else:
     #   bajas=bajas+1
      #  x=x+1
#print ("total de notas altas")
#print (altas)
#print ("total de notas bajas")
#print (bajas)