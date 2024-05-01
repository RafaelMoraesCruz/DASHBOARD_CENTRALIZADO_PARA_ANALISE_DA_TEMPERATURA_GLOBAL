import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

def grafico_heatmap(df):
    cmap = sns.diverging_palette(
    h_neg=240,
    h_pos=10,
    s=100,
    as_cmap=True)
    
    heatmap = sns.heatmap(df.corr(), fmt=".2f", cmap=cmap, 
        center=0,
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.01,
        cbar_kws={'label': 'Coeficiente de Correlação'})

    return plt.show()

with st.container():
    df_geral = pd.read_excel("./data/visao_geral_atributos_juntos.xlsx")
    df_geral.rename(columns={"cobertura_vegetal": "perda_cobertura_vegetal"})

    st.title("About")
    st.header("1. Entendimento dos dados")

    st.write("Antes do estudo ser realizado é necessário o entendimento dos dados, nas próximas linhas serão apresentadas as fontes,\
              as entidades que produziram os dados e a importância daqueles dados para o estudo.")
    
    st.write("<strong>1.1-Extensão de Gelo nos Oceanos - NSIDC (National Snow and Ice Data Center) </strong>", unsafe_allow_html=True)
    st.write("  <strong>Dados</strong>: A base de dados fornece informações sobre a extensão do gelo marinho nos oceanos, a unidade encontra-se em milhões de quilômetros quadrados.\
              Estes dados são essenciais para estudar as mudanças climáticas e o aquecimento global,\
              já que a redução do gelo marinho tem profundas implicações para o clima global.",unsafe_allow_html=True)
    st.write("  <strong>Organização</strong>: O NSIDC é parte da Universidade do Colorado e afiliado com a NOAA (National Oceanic and Atmospheric Administration).\
          Eles focam no estudo das partes congeladas da Terra e seu impacto no sistema climático global.",unsafe_allow_html=True)
    
    st.write("<strong> 1.2-Emissão de CO2 - Our World in Data </strong>", unsafe_allow_html=True)
    st.write("<strong>Dados</strong>: Esta base de dados fornece informações detalhadas sobre emissões de dióxido de carbono (CO2) em toneladas,\
              um dos principais gases do efeito estufa responsáveis pelo aquecimento global.\
              Os dados ajudam a monitorar e analisar o impacto das atividades humanas no aumento dos níveis de CO2.", unsafe_allow_html=True)
    st.write("<strong> Organização</strong>: Our World in Data é um projeto online que apresenta pesquisas empíricas e dados estatísticos sobre as mudanças nas condições de vida ao redor do mundo.\
              É publicado pela Global Change Data Lab, uma organização sem fins lucrativos do Reino Unido.", unsafe_allow_html=True)
    
    st.write("<strong> 1.3-Perda de Cobertura Vegetal - Global Forest Watch</strong>", unsafe_allow_html=True)
    st.write("<strong>Dados</strong>: A plataforma oferece dados sobre perda de cobertura vegetal, expressa em quilômetros quadrados,\
              permitindo aos usuários monitorar a desflorestação e outras formas de degradação florestal em tempo real.\
              Estes dados são cruciais para esforços de conservação e políticas de uso da terra.", unsafe_allow_html=True)
    st.write("<strong> Organização</strong>: Global Forest Watch é uma iniciativa do World Resources Institute,\
              uma organização global de pesquisa que fornece informações e ferramentas para proteger os recursos naturais e garantir que o desenvolvimento econômico seja sustentável.", unsafe_allow_html=True)
    
    st.write("<strong>1.4-Temperatura - Copernicus Climate Change Service</strong>", unsafe_allow_html=True)
    st.write("<strong>Dados</strong>: Esta base de dados registra as temperaturas médias globais e é uma ferramenta valiosa para cientistas e pesquisadores monitorarem as mudanças climáticas.\
              O aquecimento global é uma das maiores preocupações de nosso tempo, e entender as tendências de temperatura é fundamental para combater suas consequências.", unsafe_allow_html=True)
    st.write("<strong> Organização</strong>: Copernicus Climate Change Service é parte do Programa Copernicus da União Europeia,\
              dedicado a fornecer informações climáticas precisas e atualizadas para apoiar a política ambiental e de mudanças climáticas na Europa e no mundo.", unsafe_allow_html=True)
    
    st.header("2. Exploração dos dados")

    st.write("Começamos com a exploração dos dados usando a bibloteca ydata_profiling que antigamente se chamava pandas-profiling.\
              A ferramenta é muito útil, pois automatiza o processo incial de Exploração dos dados gerando um relatório inicial sobre o conjunto de dados, \
             oferecendo uma visão detalhada incialmente. Com o ydata_profiling é possível ter uma visão abrangente dos dados, identificação rápida da qualidade\
             dos dados, facilita o processo de limpeza...")
    
    st.write("<strong>Correlação dos atributos</strong>", unsafe_allow_html=True)
    st.dataframe(df_geral.corr())
    st.write("<strong>Grafico Heatmap da correlação entre os atributos.</strong>", unsafe_allow_html=True)
    st.pyplot(grafico_heatmap(df_geral))
    