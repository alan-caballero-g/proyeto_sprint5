import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Información de vehículos en venta")
df_vehicles = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(df_vehicles, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Mostrar gráfico de dispersión')
if scatter_button:
    fig = px.scatter(df_vehicles, x="odometer", y="price",
                     title="Gráfico de Dispersión")
    st.plotly_chart(fig)
