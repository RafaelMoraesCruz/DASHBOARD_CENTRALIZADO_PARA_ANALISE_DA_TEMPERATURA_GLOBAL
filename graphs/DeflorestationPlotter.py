import streamlit as st
import pandas as pd
import plotly.express as px

class Deforestation_plotter:

    @staticmethod
    def cobertura_perdida_atraves_dos_anos_paises(df):
        fig = px.line(df, x="ano", y="desmatamento", color="pais",
                    title="Cobertura de floresta perdida comparativo países", 
                    labels={"desmatamento" : "Cobertura de floresta perdida km²", "ano": "Ano", "pais" : "País"}, markers=True)
        return fig

    @staticmethod
    def desmatamento_atraves_dos_anos_mundo(df):
        fig = px.line(df, x='ano', y="desmatamento", 
                    title="Cobertura vegetal perdida mundial ao passar dos anos", labels={"desmatamento" : "Cobertura vegetal perdida"}, markers=True)
        return fig

    @staticmethod
    def box_deforestation_mundo(df):
        fig = px.box(data_frame=df, y="desmatamento",title="Distribuição da Cobertura vegetal perdida global",labels={"desmatamento" : "Cobertura vegetal perdida"})
        return fig

    @staticmethod
    def box_cobertura_perdida_paises(df):
        fig = px.box(data_frame=df, y="desmatamento", color="pais", title="Grafico comparativo da perda da cobertura vegetal entre os países", labels={"desmatamento" : "Cobertura vegetal km²", "pais": "País"})
        return fig