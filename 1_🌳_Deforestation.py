import pandas as pd
import streamlit as st
import os
from graphs.DeflorestationPlotter import Deforestation_plotter

# Streamlit config
st.set_page_config(layout="wide")
data_folder = f"{os.getcwd()}/data/deforestation/"
# Dataframe
df = pd.read_excel(f"{data_folder}gfw_2023_statistics_summary_clean_melted.xlsx")
paises = list(df["country"].unique())

st.subheader("Desmatamento Mundial")

with st.container():
    st.write("Selecione os países: ")
    col1, col2, col3, col4 = st.columns(4)


    with col1:
        checkbox_mundo = st.checkbox("selecione para mostrar o agregado mundial", value=True)
    if not checkbox_mundo:
        with col2:
            pais1 = st.selectbox("Selecione o país 1", options=paises)
            pais2 = st.selectbox("Selecione o país 2", options=paises, index=5)
            selecionados = [pais1,pais2]
    with col4:
        min_year = df["ano"].min()
        max_year = df["ano"].max()
        years_range = st.slider(
        'Select the range of years:',
        min_year, max_year, (min_year, max_year))
        years = [year for year in range(years_range[0], years_range[1]+1)]

        df_for_metric = df[(df["ano"].isin(years) & (df["country"].isin(selecionados)))]

        # Parei AQUI 15/04/2024
        sum_metric_desmatamento = df_for_metric.groupby("country").sum().sort_values(by="desmatamento", ascending=False)["desmatamento"].sum()
        metric_visibility="hidden"
        if sum_metric_desmatamento!= 0:
            metric_visibility="visible"
            st.metric(label=f"Total deforestation between {years[0]} - {years[-1]}",
                       value=f"{sum_metric_desmatamento}km²",
                         label_visibility=metric_visibility)
        pass

with st.container():

    col1, col2 = st.columns(2)

    if selecteds:
        df_for_graph = df[(df["ano"].isin(years) & (df["estado"].isin(selecteds)))]
        temporal = Deforestation_plotter.desmatamento_atraves_dos_anos_estados(df_for_graph)
        box_plot = Deforestation_plotter.box_deforestation_brazil_states(df_for_graph)
    else:
        df_for_graph = df[df["ano"].isin(years)]
        df_for_graph = df_for_graph.groupby("ano").sum().sort_values(by="ano")
        temporal = Deforestation_plotter.desmatamento_atraves_dos_anos_pais(df_for_graph)
        box_plot = Deforestation_plotter.box_deforestation_brazil(df_for_graph)

    with col1:
        st.plotly_chart(temporal)
    with col2:
        st.plotly_chart(box_plot)
