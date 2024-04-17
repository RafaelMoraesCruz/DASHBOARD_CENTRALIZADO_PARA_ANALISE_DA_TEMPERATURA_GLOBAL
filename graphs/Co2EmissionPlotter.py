import streamlit as st
import pandas as pd
import plotly.express as px

class co2_emission_plotter:
    
  @staticmethod
  def co2_over_the_years_worldwide(df, co2_option):
      fig = px.line(data_frame=df, x="Year", y=co2_option, 
                    title=f"{co2_option} over the years worldwide", labels={co2_option : f"{co2_option} (tons)"})
      return st.plotly_chart(fig)

  @staticmethod
  def co2_over_the_years_comparative(df, co2_option):
      fig = px.line(data_frame=df,
                    x="Year",
                      y=co2_option,
                        color="Entity",
                          title=f"{co2_option} over the years in {df['Entity'].unique()}",
                            labels={co2_option : f"{co2_option} (tons)"})

      return st.plotly_chart(fig)