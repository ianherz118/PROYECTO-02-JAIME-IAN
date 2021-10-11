# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 23:35:46 2021

@author: ianja
"""
# import statsmodels.api as sm
import pandas as pd 
 
df = pd.read_csv("synergy_logistics_database.csv") 
# Se carga el archivo como un dataframe
df[['register_id','year']] = df[['register_id','year']].astype(str)
# Se conviertieron esta variable a las variables que nos permite realizar nuestras funciones
def ruta(a):
    # Se genero la funcion para agrupar por las variables que se requerian 
    top_rutas = df.groupby(a).size().reset_index(name='count')
    top_rutas_sum= df.groupby(a).sum().reset_index()
    # Sirve para obtener el porcentaje de aportacion historico 
    top_rutas['percent']=(top_rutas['count']/top_rutas['count'].sum())*100
    top_rutas_sum['percent']=(top_rutas_sum['total_value']/top_rutas_sum['total_value'].sum())*100
    # Sirve para ordenar acorde a lo que se necesite 
    top_rutas = top_rutas.sort_values('count',ascending=False)
    top_rutas_sum = top_rutas_sum.sort_values('total_value',ascending=False)
    return top_rutas,top_rutas_sum

def porcentaje(b,c):
    porciento=0
    i=0
    list_demanda = b.values.tolist()
    # convertir a lista y poder mostrar la aproximacion del 40 por ciento 
    while porciento<c:
        porciento=list_demanda[i][2]+porciento
        i+=1
    return list_demanda[0:i]
# Se llaman a los funciones necesarias para las agupaciones necesarias 
top_Importacion_Exportacion_conteo,top_Importacion_Exportacion_totalValor=ruta(['origin', 'destination'])
top_transport_mode_conteo,top_transport_mode_totalValor=ruta(['transport_mode'])
top_origen_conteo,top_origen_totalValor=ruta(['origin'])

# Se llama a la funcion para calcular el 80% del historico 
list_demanda_80_top_origen=porcentaje(top_origen_conteo,80)

# Se llaman a los funciones necesarias para las agupaciones necesarias  con año 
top_origen_year,top_year_totalValor=ruta(['origin','year'])
top_transporte_year,top_year_transporte_totalValor=ruta(['transport_mode','year'])
top_Importacion_year_Exportacion_conteo,top_Importacion_year_Exportacion_totalValor=ruta(['origin', 'destination','year'])
top_producto_year_Exportacion_conteo,top_producto_year_Exportacion_totalValor=ruta(['product','year'])
year,year_totalValor=ruta(['year'])

#Imprime los datos solicitados 
print(" \n Rutas mas demandadas: \n")
print(top_Importacion_Exportacion_conteo.head(10))

print(" \n Rutas que mas valor generan: \n")
print(top_Importacion_Exportacion_totalValor.head(10))

print(" \n Rutas transporte con mas uso:\n")
print(top_transport_mode_conteo.head(3))

print(" \n Rutas transporte con mas valor generado:\n")
print(top_transport_mode_totalValor.head(3))

print(" \n Paises que representan 80% demanda:\n")
for i in range (len(list_demanda_80_top_origen)):
    print("\n Pais:",list_demanda_80_top_origen[i][0], "Demanda:",round(list_demanda_80_top_origen[i][-1], 2),"%")

#  Esta parte se relizo el modelo ARIMA para ver como se comportara en un futuro
# Se seleciono de esta forma para que no fuera necesario instalar la libreria para correr el programa
# year_predict=year[['year','count']]
# mod = sm.tsa.arima.ARIMA(year_predict['count'], order=(1, 0, 0))
# res = mod.fit()
# year_predict['pronostico'] = res.fittedvalues 

# year_predict_valor=year_totalValor[['year','total_value']]
# mod2 = sm.tsa.arima.ARIMA(year_predict_valor['total_value'], order=(1, 0, 0))
# res2 = mod2.fit()
# year_predict_valor['pronostico'] = res2.fittedvalues   
