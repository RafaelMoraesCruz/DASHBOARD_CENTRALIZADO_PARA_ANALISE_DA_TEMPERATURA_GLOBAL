import streamlit as st
import pandas as pd
from graphs.Co2EmissionPlotter import co2_emission_plotter

st.set_page_config(layout="wide")

df = pd.read_csv("./data/CO2/co2-fossil-plus-land-use.csv")

with st.container():
    st.title("Emissões de CO²")

    col1, col2 = st.columns([2, 4])
    with col1:
        checkbox = st.checkbox("Mundo", value=True)
        co2_option = st.selectbox(
            '',
            df.columns[3:])
        df_world = df.groupby("Year").sum()[co2_option].reset_index()
        if not checkbox:
            st.subheader("Selecione duas entidades para comparar.")
            option1 = st.selectbox(
            'Selecione a primeira entidade.',
            df["Entity"].unique())

            option2 = st.selectbox(
            'Selecione a segunda entidade.',
            df["Entity"].unique())
            df_world = df[df["Entity"].isin([option1,option2])].reset_index()
    with col2:
        if not checkbox:
            co2_emission_plotter.co2_over_the_years_comparative(df_world, co2_option)
        else:
            co2_emission_plotter.co2_over_the_years_worldwide(df_world, co2_option)
