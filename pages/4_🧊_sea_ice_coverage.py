import pandas as pd
import streamlit as st
import plotly.express as ex

from graphs.SeaIcePlotter import sea_ice_plotter

st.set_page_config(layout="wide")
header = st.container()
col1, col2 = st.columns(2)
graphics = st.container()

df = pd.read_csv("./data/sea-ice-coverage/seaice-treated.csv")
df.dropna(inplace=True)

with header:
    st.title("Sea Ice Coverage")

    with col1:
        min_year = int(df["Year"].min())
        max_year = int(df["Year"].max())
        years_range = st.slider(
        'Select the range of years:',
        min_year, max_year, (min_year, max_year))
        years = [year for year in range(int(years_range[0]), int(years_range[1])+1)]
        lower_year, top_year = years[0], years[-1]

        df_year = df[df["Year"].isin(years)]

    with col2:
        by_hemisphere = st.toggle('Split by hemisphere')


with graphics:
    if not by_hemisphere:
        df_global = df_year[["Year", "ice-extent"]].groupby("Year").mean().reset_index().sort_values(by="Year")
        sea_ice_plotter.seaice_global(df_global)
    else:
        sea_ice_plotter.seaice_per_hemisphere(df_year)
            