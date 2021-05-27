# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:31:25 2021

@author: Jisus
"""

"""Punto 3: Se desea obtener la nómina semanal —salario neto— de los N 
(Leídos por teclado) empleados   de una empresa, cuyo trabajo se paga por
horas y del modo siguiente:

• las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa 
  determinada que se debe introducir por teclado al igual que el número de
  horas trabajadas, el nombre del trabajador, género  y 1,2 o 3 de acuerdo
  a la sección donde trabaje
• las horas superiores a 35 se pagarán como extras a un promedio de 1,5 
horas normales,
• los impuestos a deducir a los trabajadores varían en función de su 
sueldo mensual:
  Salud 12,5% del salario
  ICBF 4% del salario
  Retención en la fuente según la tabla anexa:
       de 2’000.000 a 3´000.000 5%
       de 3’000.001 a 4’000.000 7%
       de 4’000.001 a 5’000.000 9%
       de 5’000.000 en adelante 11%
Imprima el desprendible de pago detallado para cada empleado
Imprima la planilla de totales de pago de la empresa (Total Empleados, 
Total Horas, Total extras, pago horas, pago extras, etc)
Imprimir la planilla de totales los acumulados por sección.
Imprimir la planilla de totales los acumulados por género."""

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")
#Prototipo 
def nombre():
    nom=input("ingrese su nombre ")
    genero=input("ingrese su genero H/M ",)
    return (nom,codigo_empleado)
       
def horas():
    h=int(input("ingrse el total de horas "))
    t=int(input("ingrese el precio por cada hora"))
    if h<=35:
        sbruto=h*t
        print ("has ganado un total:",sbruto)
    else:
        promedio=t*1.5/100+t
        h_promedio=h*promedio
        print ("has ganado un total: ",h_promedio)
    return (h,t)

"""def tarifa():
    t=int(input("ingrese el precio por cada hora"))
    return (t)"""

#salida
mostrar_mensaje(""" (smmlv) Colombia 2021 
                hora normal $4229	Jornada ordinaria 6:00 a.m.–9:00 p.m.""")
nombre()
horas()
genero 
    
