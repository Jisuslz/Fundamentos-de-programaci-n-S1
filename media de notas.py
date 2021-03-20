# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:02:01 2021

@author: Jisus
"""

"""progrma que lee el nombre y la nota 
definitiva de tres materias
(basic,fortran y pascal) de N
estudiantes .Condicion de salida
nombre = ***"""

#Area de claracion de de variables 

var_e_nom = "***"
var_e_bas = 0.0
var_e_for = 0.0
var_e_pas = 0.0

var_p_s_medEst = 0.0
var_p_s_conEst = 0

#leer nombre

var_e_nom = input("digite nombre del estudiante:")

#ingreso o inicio el ciclo while
while (var_e_nom != "***"):
    var_e_bas = float(input("ingresa la nota de Basic: "))
    var_e_for = float(input("ingresa la nota de Fortran: "))
    var_e_pas = float(input("ingresa la nota de Pascal: "))

#proceso
    var_p_s_medEst = (var_e_bas+var_e_for+var_e_pas/3)
    print("la media del estudiante  ",var_e_nom, "es",var_p_s_medEst)
    var_e_nom = input ("digite nombre del estudiante: ")
    var_p_s_conEst += 1
#fin del ciclo
    
print("la cantidada de estudiante es: ",var_p_s_conEst)
print("ADIOS")