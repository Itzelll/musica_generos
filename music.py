import streamlit as st
import numpy as np
import pandas as pd
import codecs

st.title('Generos de musica')
DATA_URL = ('music_genre.csv')

@st.cache
def load_data(nrows):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    #data.rename({'start_lat':'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) #la fecha lo vuelve string
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done!")

sidebar = st.sidebar
sidebar.image('genremusic.png')
sidebar.title("Itzel Mendez Martinez")
sidebar.write("Matricula: S20006761")
sidebar.write("zs20006761@estudiantes.uv.mx")
sidebar.markdown("___")

#Dataset
st.header("Dataset")
agree = sidebar.checkbox("Selecciona para mostrar el dataset")
if agree:
  st.dataframe(data)
