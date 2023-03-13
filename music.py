import streamlit as st
import pandas as pd
import codecs
import plotly.express as px

st.title('Generos de musica')
DATA_URL = ('top10s.csv')

@st.cache
def load_data(nrows):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
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

#::::::::::Dataset::::::::::::::::::::
st.header("Dataset:")
sidebar.title("Opciones:")
agree = sidebar.checkbox("Selecciona para mostrar el dataset")
if agree:
  st.dataframe(data)

sidebar.markdown("_")

#:::::::::::nombre canciones:::::::::::
st.header("Titulo de canciones:")
sidebar.write("\n")
@st.cache
def load_data_film(names):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered_name = data[data['title'].str.contains(names, case=False)]
    return filtered_name

selected_title = sidebar.text_input("Buscar por nombre de una cancion:")
button_name = sidebar.button("Buscar titulo")

if(button_name):
    filtroname = load_data_film(selected_title)
    count_row = filtroname.shape[0]
    st.write(f"Total encontrados: {count_row}")
    st.dataframe(filtroname)

#:::::::::genero musica:::::::::::
st.header("Filtro de canciones por genero:")
sidebar.write("\n")
@st.cache
def load_data_bygenre(g):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered_data = data[data['top genre'] == g]
    return filtered_data

selected_g = sidebar.selectbox("Buscar por genero de musica:", data['top genre'].unique())
btnFilterbyG = sidebar.button('Filtrar')

if (btnFilterbyG):
    filtro = load_data_bygenre(selected_g)
    count_row = filtro.shape[0] 
    st.write(f"Total items : {count_row}")
    st.dataframe(filtro)

#::::::::::: Multiselect ::::::::::::
st.header("Multiselect:")
sidebar.write("\n")
year = sidebar.multiselect("Selecciona año(s):",
                                options=data['year'].unique())

df_selection=data.query("year == @year")
st.write("Años seleccionados", df_selection)
sidebar.markdown("__")

#::::::::::: histograma :::::::::::
sidebar.title("Graficas:")
st.header("Histograma")
agree = sidebar.checkbox("Clic para ver histograma")
if agree:
  fig_genre=px.bar(data,
                    x=data['top genre'],
                    y=data.index,
                    orientation="v",
                    title="Cantidad de canciones que hay por genero",
                    labels=dict(y="index", x="top genre"),
                    color_discrete_sequence=["#7ECBB4"],
                    template="plotly_white")
  st.plotly_chart(fig_genre)

#::::::::::: grafica de barras :::::::::::
st.header("Grafica de barras")
agree = sidebar.checkbox("Clic para ver grafica de barras")
if agree:
   title=data['title']
   year=data['year']
   fig_barra=px.bar(data,
                    x=year,
                    y=title,
                    orientation="v",
                    title="Nombre de las canciones y el año en que salieron",
                    labels=dict(year="Year", title="Title"),
                    template="plotly_white")
   st.plotly_chart(fig_barra)

#::::::::::: grafica scatter :::::::::::
st.header("Grafica Scatter")
agree = sidebar.checkbox("Clic para ver grafica scatter")
if agree:
    year=data['year']
    artist=data['artist']
    dnce=data['dnce']
    fig_age=px.scatter(data,
                   x=year,
                   y=dnce,
                   color=artist,
                   title="¿Que tan bailable son las canciones dependiendo del artista? Nivel (0-100)",
                   labels=dict(year="Year", artist="Artist", dnce="Danceability"),
                   template="plotly_white")
    st.plotly_chart(fig_age)

sidebar.markdown("___")
