import pandas as pd
import streamlit as st
import plotly as pt

st.set_page_config(layout="wide")

df_cars = pd.read_csv('dataset/Automobile.csv')

cars = df_cars['name'].unique()
car = st.sidebar.selectbox('Car', cars)

df_car = df_cars[df_cars['name'] == car]
year = f'19{df_car['model_year'].iloc[0]}'
mpg = df_car['mpg'].iloc[0]
horsepower = df_car['horsepower'].iloc[0]
acceleration = df_car['acceleration'].iloc[0]
origin = df_car['origin'].iloc[0].title()
weight = df_car['weight'].iloc[0]
cylinders = df_car['cylinders'].iloc[0]


st.title(car.title())

col1, col2 = st.columns(2)

col1.subheader(f"Model Year: {year}")
col2.subheader(f"Origin: {origin}")

st.divider()

col1, col2 = st.columns(2)
col1.metric('MPG', mpg)
col2.metric('Weight', weight)

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric('HP', horsepower)
col2.metric('Cylinders', cylinders)
col3.metric('Acceleration', acceleration)