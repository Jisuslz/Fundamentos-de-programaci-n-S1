# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:07:05 2021

@author: Jisus
"""

## ejercicio que almacena en listas - procesa en funcioes
## Declar las librerias a usar para la soluciones

import matplotlib.pyplot as plt

#generar los datos inicializados
nombreProducto= ['Ron','Aguardiente','Vino','cerveza']
existenciaProducto=[75,50,100,150]
#Funciones que resuelven el prob

def f_calc_tot_existencias():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    print("total existencias", sumaExistencias)
    
def f_calc_tot_existencias_2():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    return(sumaExistencias)

#
def f_calc_prom_existencias():
    promExistencias = f_calc_tot_existencias_2()/len(existenciaProducto)
    return(promExistencias)

#llamdo a las funciones que realizan los calculos 
f_calc_tot_existencias()
print("total exsitencias 2:",f_calc_tot_existencias_2())
print ("promedio existencias",f_calc_prom_existencias())
#graficar la info
fig, ax = plt.subplots()
#Definiri el titulo del grafico
ax.set_title('GRAFICO DE EXISTENCIA DE PRODUCTO')
ax.set_xlabel('productos')
ax.set_ylabel('existencias')

#crear el
plt.bar(nombreProducto,existenciaProducto)

#publico el grafico
plt.show()

