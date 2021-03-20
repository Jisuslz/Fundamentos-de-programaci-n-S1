# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:49:15 2021

@author: Jisus
"""

import numpy as np
Matriz = np.arange (9)
np.random.shuffle (Matriz)
Matriz = Matriz.reshape((3,3))
print(Matriz)

matriz_1= np.trace(Matriz)
print("la matriz 1 es: ",matriz_1 )
Matriz_inv = np.linalg.inv(Matriz)
deterM = np.linalg.det(Matriz)
adjunta = deterM * Matriz_inv
cofactor1 = adjunta
print("Cofactor: ", cofactor1)