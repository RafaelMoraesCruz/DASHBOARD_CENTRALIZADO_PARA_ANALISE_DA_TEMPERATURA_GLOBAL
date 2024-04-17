import plotly.express as px
import streamlit as st

class sea_ice_plotter:

    @staticmethod
    def seaice_per_hemisphere(df):
        fig = px.line(data_frame=df, 
                      x="Year", 
                      y="ice-extent", 
                      color="hemisphere",
                      title="Sea ice coverage by hemisphere",
                      labels={"ice-extent" : "Extent * 10^6 sq km"})
        return st.plotly_chart(fig)
    
    @staticmethod
    def seaice_global(df):
        fig = px.line(data_frame=df, 
                      x="Year", 
                      y="ice-extent", 
                      title="Sea ice layer worldwide",
                      labels={"ice-extent" : "Extent * 10^6 sq km"},
                      markers=True)
                      
        return st.plotly_chart(fig)