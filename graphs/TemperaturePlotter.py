import streamlit as st
import pandas as pd
import plotly.express as px

class Temperature_plotter:

    @staticmethod
    def top3_years(df, ano1, ano2):
            fig = px.bar(data_frame=df, x="year", y="celsius", color="celsius", 
            title=f"Anos mais quentes dentre os anos: {ano1} - {ano2}",
            range_y = [df["celsius"].min() - 0.1 , df["celsius"].max() + 0.1], labels={"year": "Ano", "celsius": "Celsius"})
            
            fig.update_xaxes(
                            tickmode = 'array',
                            tickvals = df["year"])
            return st.plotly_chart(fig)

    
    @staticmethod
    def temperature_over_the_years(df, ano1, ano2):
        fig = px.line(data_frame=df, x="year", y="celsius", 
        title=f"Temperatura ao longo dos anos entre os anos: {ano1} - {ano2}",
        labels={"year": "Ano", "celsius": "Celsius"},
          markers=True)
        return st.plotly_chart(fig)