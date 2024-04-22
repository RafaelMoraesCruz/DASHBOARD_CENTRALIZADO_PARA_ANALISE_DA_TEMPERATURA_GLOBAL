import streamlit as st
import os
import pandas as pd
from graphs.TemperaturePlotter import Temperature_plotter

# Streamlit config
st.set_page_config(layout="wide")

st.title("Temperatura através dos anos")
print(os.getcwd())
df = pd.read_excel(f"./data/temperature/word-wide-temperature.xlsx")

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col3:
        min_year = df["year"].min()
        max_year = df["year"].max()
        years_range = st.slider(
        'Selecione o alcance dos anos:',
        min_year, max_year, (min_year, max_year))
        years = [year for year in range(years_range[0], years_range[1]+1)]
        lower_year, top_year = years[0], years[-1]

        df_year = df[df["year"].isin(years)]

    with col5:
        st.metric("Número de anos no alcance: ", value=top_year - lower_year)

    with col1:
        top_year_temperature = df_year[df_year["year"] == top_year]["celsius"].values[0]
        lower_year_temperature = df_year[df_year["year"] == lower_year]["celsius"].values[0]
        st.metric("Diferença de temperatura ", value=f"{lower_year} -> {top_year}", delta=f"{round(top_year_temperature-lower_year_temperature,2)} °C")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        top3 = df_year.sort_values(by="celsius", ascending=False).head(3)
        Temperature_plotter.top3_years(top3, lower_year,top_year)

    with col2:
        Temperature_plotter.temperature_over_the_years(df_year,lower_year, top_year)
        pass
