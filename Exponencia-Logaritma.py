# -*- coding: utf-8 -*-
"""
Created on Tue May 25 01:13:49 2021

@author: Jisus
"""


print("Funcion Exponencial y Logaritmica")

import numpy as np
from numpy.core.records import array

print("funcion ax^2")
print(5*10**2)

print("funcion exponencial e^x")
print(np.exp(5))
np.exp(5)

print("funcion exponente")
print(120**2)

print("funcion loge x o ln x")
print(np.log(5))
np.log(5)

print("funcion log10x o log x")
print(np.log10(8))
np.log10(8)

print("funcion log2x ")
print(np.log2(20))
np.log2(20)

print("Graficas Funcion exponencial y Logaritmica")
import math 
import numpy as np
from matplotlib import pyplot as plt

h=lambda x: np.exp(x)

x=np.arange(0,10,0.1)

plt.subplot(2,2,2)
plt.plot(x,h(x),label="Funcion exponencial")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funcion exponencial')
plt.show()

f=lambda x: np.log(x)

x=np.arange(0,10,0.1)

plt.subplot(2,2,1)
plt.plot(x,f(x), label="Funcion logaritmica")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funcion logaritmica')
plt.show()

plt.savefig("graficas")