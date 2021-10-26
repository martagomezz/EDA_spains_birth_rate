# importar librerías
from http.client import ImproperConnectionState
import streamlit as st
import functions as ft
import pandas as pd
import os 
# configurar la página
ft.config_page()

# cargar los datos

path1 = 'data/output/factores_natalidad.csv'
df1 = ft.cargar_datos(path1)

path2 = 'data/output/factores_natalidad_salarios.csv'
df2 = ft.cargar_datos(path2)

st.title('Natalidad en España') 

# menú
menu = st.sidebar.selectbox('Selecciona menú',['Home','Datos','Filtros','Conclusiones']) 
if menu == 'Home':
    ft.home()
elif menu == 'Datos':
    ft.datos(df1)
elif menu == 'Filtros':
    ft.filtros(df2)
else:
    ft.conclusiones()