import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
df_cars = pd.read_csv('dataset/Automobile.csv')

min_hp = df_cars['horsepower'].min()
max_hp = df_cars['horsepower'].max()

hp_select = st.sidebar.slider("HP Range", min_hp, max_hp, max_hp)

cars_filtered = df_cars[df_cars['horsepower'] <= hp_select]

st.title("Car Insights (Home)")
cars_filtered

### CHARTs
cars_by_year = px.pie(
    cars_filtered, 
    names="model_year",
    title="Number os models per year"
)


col1, col2 = st.columns(2);
cars_by_cilinders = px.bar(cars_filtered['cylinders'].value_counts(), title="Number of models per Cylinders")
cars_by_origin = px.pie(cars_filtered, names="origin", title="Cars by origin")

col1.plotly_chart(cars_by_year)
col2.plotly_chart(cars_by_cilinders)

st.plotly_chart(cars_by_origin)
### MEAN

mean_horsepower = cars_filtered['horsepower'].mean()
mean_acceleration = cars_filtered['acceleration'].mean()
mean_mpg = cars_filtered['mpg'].mean()

st.title("Mean")
mean_col1, mean_col2, mean_col3 = st.columns(3)

mean_col1.metric('HP', round(mean_horsepower))
mean_col2.metric('Acceleration',f'{mean_acceleration:.2f}')
mean_col3.metric('MPG (Miles Per Kilometer)', f'{mean_mpg:.2f}')

st.divider()

### MODE

mode_hp = cars_filtered['horsepower'].mode()
mode_acceleration = cars_filtered['acceleration'].mode()
mode_mpg = cars_filtered['mpg'].mode()


st.title('Mode')

mode_col1, mode_col2, mode_col3 = st.columns(3)

mode_col1.metric('HP', mode_hp)
mode_col2.metric('Acceleration', mode_acceleration)
mode_col3.metric('MPG (Miles Per Kilometer)', mode_mpg)

st.divider()

### Median (Mediana)

median_hp = cars_filtered['horsepower'].median()
median_acceleration = cars_filtered['acceleration'].median()
median_mpg = cars_filtered['mpg'].median()

st.title('Median')

median_col1, median_col2, median_col3 = st.columns(3)

median_col1.metric('HP', median_hp)
median_col2.metric('Acceleration', median_acceleration)
median_col3.metric('MPG (Miles Per Kilometer)', median_mpg)

