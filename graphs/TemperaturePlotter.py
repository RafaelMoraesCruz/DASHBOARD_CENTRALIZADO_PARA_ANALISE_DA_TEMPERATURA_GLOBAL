import streamlit as st
import pandas as pd
import plotly.express as px

class Temperature_plotter:

    @staticmethod
    def top3_years(df, ano1, ano2):
            fig = px.bar(data_frame=df, x="year", y="celsius", color="celsius", 
            title=f"3 hotter years between years {ano1} - {ano2}",
            range_y = [df["celsius"].min() - 0.1 , df["celsius"].max() + 0.1])
            
            fig.update_xaxes(
                            tickmode = 'array',
                            tickvals = df["year"])
            return st.plotly_chart(fig)

    
    @staticmethod
    def temperature_over_the_years(df, ano1, ano2):
        fig = px.line(data_frame=df, x="year", y="celsius", 
        title=f"Temperature over the years world wide between years {ano1} - {ano2}")
        return st.plotly_chart(fig)