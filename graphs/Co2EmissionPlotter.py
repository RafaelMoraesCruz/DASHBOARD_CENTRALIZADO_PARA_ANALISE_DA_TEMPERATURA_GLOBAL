import streamlit as st
import pandas as pd
import plotly.express as px

class co2_emission_plotter:
    
  @staticmethod
  def co2_over_the_years_worldwide(df, co2_option):
      fig = px.line(data_frame=df, x="Year", y=co2_option, 
                    title=f"{co2_option} ao longo dos anos em todo o mundo.", labels={co2_option : f"{co2_option} (tons)", "Year": "Ano"}, color_discrete_sequence=["#7F7F7F", "#BAB0AC"])
      return st.plotly_chart(fig)

  @staticmethod
  def co2_over_the_years_comparative(df, co2_option):
      fig = px.line(data_frame=df,
                    x="Year",
                      y=co2_option,
                        color="Entity",
                          title=f"{co2_option} ao longo dos anos em {df['Entity'].unique()}",
                            labels={co2_option : f"{co2_option} (tons)", "Year": "Ano", "Entity": "Entidade"},
                              color_discrete_sequence=["#7F7F7F", "#BAB0AC"])

      return st.plotly_chart(fig)