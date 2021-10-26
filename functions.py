# importar librerias
from os import write
import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import texto as tx
import matplotlib.pyplot as plt

# configuración de la página
def config_page():
    st.set_page_config(
        page_title = 'Natalidad en España',
        page_icon = ':baby_symbol:',
        layout = 'wide'
    )
# cache
st.cache(suppress_st_warning=True)

# cargar los datos
def cargar_datos(path):
    df = pd.read_csv(path)
    return df

# HOME
def home():
    filehtml = open('utils/output/natalidad.html','r')
    sc = filehtml.read()
    components.html(sc, height = 450)
    with st.expander(tx.titulo_natalidad):
        st.write(tx.texto_natalidad)
    with st.expander(tx.titulo_tendencia):
        st.write(tx.texto_tendencia)
    with st.expander(tx.titulo_poblacion):
        st.write(tx.texto_poblacion)
    with st.expander(tx.titulo_factores):
        st.write(tx.texto_factores)
        st.write(tx.texto_nota)
    with st.expander(tx.titulo_fertilidad):
        st.write(tx.texto_fertilidad)
    pass

# DATOS
def datos(df):

    st.write('Condicionantes de la natalidad española')
    st.table(df)

    filehtml1 = open('utils/output/comparativa_natalidad_fertilidad.html','r')
    sc = filehtml1.read()
    components.html(sc, height = 450)
  
    filehtml2 = open('utils/output/comparativa_natalidad_desempleo.html','r')
    sc = filehtml2.read()
    components.html(sc, height = 450)

    st.write('Comparativa evolutiva tasas natalidad y abortos voluntarios')
    img = Image.open('utils/output/Correlacion_IVE.jpg')
    st.image(img, use_column_width='auto')

# FILTROS

def filtros(df):
    
    filehtml = open('utils/output/salarios_sectores.html','r')
    sc = filehtml.read()
    components.html(sc, height = 450)

    check_year = st.sidebar.radio('¿Quieres filtrar por año?',('no','si'))
    if check_year == 'si': 
        lista_year = list(df['Periodo'].unique())
        filtro_year = st.sidebar.selectbox('Selecciona un año',lista_year)
        df = df[df['Periodo'] == filtro_year]
    else:
         pass
    
    check_sector = st.sidebar.radio('¿Quieres filtrar por sector?',('no','si'))
    if check_sector == 'si':
        lista_sector = list(df['Sector'].unique())
        filtro_sector = st.sidebar.selectbox('Selecciona un sector',lista_sector)
        df = df[df['Sector'] == filtro_sector]
    else:
         pass

    st.write('Sectores y Salarios en España')
    st.table(df)

    df_poblacion = round(df.groupby('Sector')['% Población'].mean(),2).to_frame().reset_index()

    labels = df_poblacion['Sector']
    values = df_poblacion['% Población']
    colours = {'Construcción': '#b97c26',
           'Servicios': '#26b97c',
           'Industria': '#4126b9'
            }
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=[colours[key] for key in labels], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  

    

    col1,col2 = st.columns(2)

    with col1:
        st.pyplot(fig)

    with col2:
        st.write(df_poblacion)

# CONCLUSIONES
def conclusiones():
    img = Image.open('utils/balanza.jpg')
    st.image(img, use_column_width='auto')
    st.write('Conclusiones')
    st.write(tx.conclusiones)