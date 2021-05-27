# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:50:22 2021

@author: Jisus
"""

import pandas as pd

# leer archivo excel
df_archivoExcel = pd.read_excel('ventas_productos_1.xlsx',index_col="Producto")
df_archivoExcel = df_archivoExcel[ :10].copy()
print(df_archivoExcel)

#Grafica Vertocal
df_archivoExcel.plot(kind = 'bar')
df_archivoExcel.plot(kind = 'barh')
df_archivoExcel.plot(kind = 'barh',width=1)