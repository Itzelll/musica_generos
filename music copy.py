import streamlit as st
import numpy as np
import pandas as pd
import codecs
import plotly.express as px
import matplotlib.pyplot as plt

st.title('Generos de musica')
DATA_URL = ('top10s.csv')
#DATA_URL = ('music_genre.csv')
#DATE_COLUMN = 'top genre'

@st.cache
def load_data(nrows):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    #lowercase = lambda x: str(x).lower()
    #data.rename({'start_lat':'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) #la fecha lo vuelve string
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done!")

sidebar = st.sidebar
sidebar.image('genrem.png')
sidebar.title("Itzel Mendez Martinez")
sidebar.write("Matricula: S20006761")
sidebar.write("zs20006761@estudiantes.uv.mx")
sidebar.markdown("___")

#Dataset
st.header("Dataset")
sidebar.title("Opciones:")
agree = sidebar.checkbox("Selecciona para mostrar el dataset")
if agree:
  st.dataframe(data)

#nombre canciones
st.header("Titulo de canciones")
sidebar.write("\n")
@st.cache
def load_data_film(names):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered_name = data[data['title'].str.contains(names)]

    return filtered_name

selected_title = sidebar.text_input("Busca nombre de una cancion:")
button_name = sidebar.button("Buscar titulo")

if(button_name):
    filtroname = load_data_film(selected_title)
    st.dataframe(filtroname)

#genero musica
st.header("Filtro por genero")
sidebar.write("\n")
@st.cache
def load_data_bygenre(g):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered_data = data[data['top genre'] == g]

    return filtered_data

selected_g = sidebar.selectbox("Busca genero de musica:", data['top genre'].unique())
btnFilterbyG = sidebar.button('Filtrar')

if (btnFilterbyG):
    filtro = load_data_bygenre(selected_g)
    count_row = filtro.shape[0] 
    st.write(f"Total items : {count_row}")

    st.dataframe(filtro)

#histograma 
st.header("Histograma")
sidebar.write("\n")
agree = sidebar.checkbox("Clic para ver histograma")
if agree:
  fig_genre=px.bar(data,
                          x="top genre",
                          y=data.index,
                          orientation="v",
                          title="Cantidad de canciones que hay por genero",
                          labels=dict(average_genre="Total Generos", genre="top genre"),
                          color_discrete_sequence=["#7ECBB4"],
                          template="plotly_white")

  st.plotly_chart(fig_genre)

#grafica de barras de 2 columnas
st.header("Grafica de barras")
sidebar.write("\n")
agree = sidebar.checkbox("Clic para ver grafica de barras")
if agree:
   fig_barra=px.bar(data,
                    x="top genre",
                    y=data.index,
                    orientation="v",
                    title="Cantidad de canciones que hay por genero",
                    labels=dict(average_genre="Total Generos", genre="top genre"),
                    color_discrete_sequence=["#7ECBB4"],
                    template="plotly_white")
   st.plotly_chart(fig_barra)

#grafica scatter

