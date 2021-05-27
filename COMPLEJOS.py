# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:16:22 2021

@author: Jisus
"""

print("operacion con Numeros Complejos")
print("determinacion parte real y parte imaginaria de z y w")
z=-6+8j
w=3-5j
print("z:",z)
print(z.real)
print(z.imag)

print("w:",w)
print(w.real)
print(w.imag)

print("operaciones basicas con z y w")

print("suma:", z+w)
print("resta:", z-w)
print("multiplicacion:", z*w)
print("division:", z/w)

print("conjugado z:",z.conjugate())
print("conjugado w:",w.conjugate())

print("reciproco z:",1/z)
print("reciproco w:",1/w)

print("z al cuadrado:",z**2)
print("z al cubo:",z**3)
print("w al cuadrado:",w**2)
print("w al cubo:",w**3)

print("forma polar del numero complejo")

print("abs(z):",abs(z))
print("abs(w):",abs(w))

print("modulo z:",((z**2))**1/2)
print("modulo w:",((w**2))**1/2)

import cmath

print("Angulo o argumento z:",cmath.phase(z))
print("Angulo o argumento w:",cmath.phase(w))

print("cmath.polar z:", cmath.polar(z))
print("cmath.polar w:", cmath.polar(w))

print("cmath.recta z:", cmath.rect(10,2.214))
print("cmath.recta z:", cmath.rect(5.830,-1.0303))