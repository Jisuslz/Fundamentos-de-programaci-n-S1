# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:20:48 2021

@author: Jisus
"""

matrizNumeros=[[7,8,3][1,9,2][4,6,5]]

print(matrizNumeros)

sumEleMat=0
for f in range (3):
    for c in range(3):
        sumEleMat=sumEleMat+matrizNumeros[f][c]
print ("la suma de los elementos es: ",sumEleMat)

#iMPRIMIR L AMATRIZ 
for f in range (3):
    for c in range(3):
        print (matrizNumeros[f][c])
    
    #sumar la diaigonal principal 
sumDiaPri=0
for pos in range (3):
    sumDiaPri=sumDiaPri+matrizNumeros[pos][pos]
print ("Diagonal principal" , sumDiaPri)
    