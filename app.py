import plotly.express as px
import streamlit as st
import pandas as pd

# Encabezado de la aplicación
st.header('Análisis de anuncios de vehículos usados')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón


if hist_button:
    # escribir un mensaje
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")  # crear un histograma
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
