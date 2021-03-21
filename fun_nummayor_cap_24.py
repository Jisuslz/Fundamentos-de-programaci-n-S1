# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:45:21 2021

@author: Jisus
"""

#Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. 
#La carga de los valores hacerlo por teclado.

def tres_enteros():
    num1=int(input("ingresa el primer entero: "))
    num2=int(input("ingresa el segndo entero: "))
    num3=int(input("ingresa el tercer entero: "))
    print("numero mayor es" )
    if num1>num2 and num1>num3:
        print(num1)
    else:
        if num2>num1 and num2>num3:
            print(num2)
        else:
            if num3>num1 and num3>num2:
                print(num3)
for i in range (5):
    tres_enteros() 
    
"""def mostrar_mayor(x1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if x1>v2 and x1>v3:
        print(x1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)


# programa principal

cargar()"""