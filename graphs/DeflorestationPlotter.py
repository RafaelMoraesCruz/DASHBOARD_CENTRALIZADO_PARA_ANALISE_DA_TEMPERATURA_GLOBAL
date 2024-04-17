import streamlit as st
import pandas as pd
import plotly.express as px

class Deforestation_plotter:

    @staticmethod
    def desmatamento_atraves_dos_anos_estados(df):
        fig = px.line(df, x="ano", y="desmatamento", color="estado",
                    title="Amazon deforestation in each state among the years", 
                    labels={"desmatamento" : "Deforestation km²", "ano": "Year", "estado" : "State"})
        return fig

    @staticmethod
    def desmatamento_atraves_dos_anos_pais(df):
        fig = px.line(df, x=df.index, y="desmatamento", 
                    title="Amazon deforestation in Brazil among the years", 
                    labels={"desmatamento" : "Deforestation km²", "ano": "Year"})
        return fig

    @staticmethod
    def desmatamento_estado_acumulado(df, ano1, ano2):
        fig = px.bar(data_frame=df, x=df.index, y="desmatamento", 
                    title=f"Deforestation acumulated between the selected states among the years : {ano1}-{ano2}", 
                    labels={"desmatamento" : "Deforestation km²", "estado": "State"})
        return st.plotly_chart(fig)
    
    @staticmethod
    def box_deforestation_brazil(df):
        fig = px.box(data_frame=df, y="desmatamento",title="Useful statistics using about deforestation in Brazil using box plot", labels={"desmatamento" : "Deforestation km²", "ano": "Year"})
        return fig

    @staticmethod
    def box_deforestation_brazil_states(df):
        fig = px.box(data_frame=df, y="desmatamento", color="estado", title="Useful statistics using about deforestation in Brazil states using box plot", labels={"desmatamento" : "Deforestation km²", "estado": "States"})
        return fig