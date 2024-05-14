import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import plotly.express as px
st.set_option('deprecation.showPyplotGlobalUse', False)

df_geral = pd.read_excel("./data/visao_geral_atributos_juntos.xlsx")
df_geral.rename(columns={"cobertura_vegetal": "perda_cobertura_vegetal"}, inplace=True)

df_cobertura_vegetal = pd.read_excel("./data/deforestation/gfw_2023_statistics_summary_clean_melted.xlsx")
df_cobertura_vegetal.rename(columns={"desmatamento": "perda_cobertura_vegetal"}, inplace=True)

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
        annot=True,
        linewidths=0.01,
        cbar_kws={'label': 'Coeficiente de Correlação'})

    return plt.show()

def grafico_paises(df):
    ax =sns.lineplot(data=df, x="ano", y="perda_cobertura_vegetal", hue="country",legend = 'full')
    plt.title("Perda de cobertura vegetal ao longo dos anos")
    plt.ylabel("Perda de cobertura vegetal km²")
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    return plt.show()

def grafico_perda_cobertura(df):
    sns.lineplot(data=df, x="ano", y="perda_cobertura_vegetal")
    sns.lineplot(data=df[df["ano"].isin([2015,2016])], x="ano", y="perda_cobertura_vegetal",color="red")
    plt.title("Perda de cobertura vegetal ao longo dos anos, cenário global")
    plt.ylabel("Perda de cobertura vegetal km²")
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.vlines(x=2015, ymin=0, ymax=65000, colors="red")
    # plt.vlines(x=2016, ymin=0, ymax=65000, colors="red")
    return plt.show()



dados_section = st.container()
col1, col2 = st.columns(2)
eda_section = st.container()
cobertura_vegetal_analise = st.container()
conclusao = st.container()

with dados_section:

    with st.container():
        st.title("About")
        st.header("1. Entendimento dos dados")
        st.write("Antes do estudo ser realizado é necessário o entendimento dos dados, nas próximas linhas serão apresentadas as fontes,\
        as entidades que produziram os dados e a importância daqueles dados para o estudo.")

    with col1:
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
    with col2:
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
with eda_section:

    st.header("2. Exploração dos dados")
    st.write("Começamos com a exploração dos dados usando a bibloteca ydata_profiling que antigamente se chamava pandas-profiling.\
              A ferramenta é muito útil, pois automatiza o processo incial de Exploração dos dados gerando um relatório inicial sobre o conjunto de dados, \
             oferecendo incialmente uma visão detalhada. Com o ydata_profiling é possível ter uma visão abrangente dos dados, identificação rápida da qualidade\
             dos dados, facilita o processo de limpeza...")
    
    st.write("<strong>Correlação dos atributos</strong>", unsafe_allow_html=True)
    st.dataframe(df_geral.corr(), hide_index=True)
    st.write("<strong>Grafico Heatmap da correlação entre os atributos.</strong>", unsafe_allow_html=True)
    st.pyplot(grafico_heatmap(df_geral))

    st.write("Analisando as figuras acima, é possível perceber que o fator mais bem correlacionado com a temperatura é a perda de cobertura vegetal, por isso, é importante avaliar essa variável com mais cuidado na próxima secção.")
    
with cobertura_vegetal_analise:
    st.header("3. Análise Perda de Cobertura Vegetal")
    st.write("A ideia aqui é coletar alguns países que apresentam uma grande perda de cobertura vegetal e fazer um comparativo com o cenário geral, para isso foi-se atrás de um dataset e suas perdas vegetais ao longo dos anos")
    st.subheader("3.1   visão inicial dos dados")
    st.dataframe(df_cobertura_vegetal.sort_values(by="perda_cobertura_vegetal", ascending=False), hide_index=True)
    st.write("Pela visão inicial dos dados é possível perceber que três paises ocupam o ranking com maior perda de cobertura vegetal: Brasil, Indonesia e República democrática do Congo.")
    st.write("Para isso ficar mais claro, é necessário da análise de média e mediana dos países.")
    st.write("Média")
    st.dataframe(df_cobertura_vegetal.groupby("country", as_index=False).agg({"perda_cobertura_vegetal" : "mean"}).sort_values("perda_cobertura_vegetal", ascending=False).rename(columns={"perda_cobertura_vegetal": "perda_cobertura_vegetal_media", "country": "paises"}), hide_index=True)
    st.write("Mediana")
    st.dataframe(df_cobertura_vegetal.groupby("country", as_index=False).agg({"perda_cobertura_vegetal" : "median"}).sort_values("perda_cobertura_vegetal", ascending=False).rename(columns={"perda_cobertura_vegetal": "perda_cobertura_vegetal_mediana", "country": "paises"}), hide_index=True)
    st.write("Aqui fica confirmado que os países com as maiores perdas de cobertura vegetal são Brasil, Indonésia e República Democrática do Congo.")
    st.write("Antes de realizar a comparação é fundamental o entendimento desses dados ao longo do tempo, para isso é necessário a realização de um gráfico temporal, como mostrado na figura abaixo:")
    df_cobertura_vegetal_paises = df_cobertura_vegetal[df_cobertura_vegetal["country"].isin(["Brazil", "Indonesia", "Democratic Republic of the Congo"])]
    st.pyplot(grafico_paises(df_cobertura_vegetal_paises))

    st.subheader("Comparativo local-global")
    st.write("O gráfico apresenta alguns pontos interessantes, por exemplo, o Brasil é o pais com maior perda vegetal durante os anos, não existe nenhumum ano que algum dos outros 2 países supera o Brasil.")
    st.write("Outro ponto que será estudado é o crescimento em um nível bastante elevado entre os anos de 2015 e 2016 em todos os três países. E logo em seguida a perda de cobertura entra em um declínio também acentuado.")
    st.write("O gráfico a seguir mostra o cenário mundial da perda de cobertura vegetal.")

    st.pyplot(grafico_perda_cobertura(df_geral))
    perda_cobertura_2016 = df_geral[df_geral["ano"]== 2016]["perda_cobertura_vegetal"].values[0]
    perda_cobertura_2016_congo = df_cobertura_vegetal_paises[(df_cobertura_vegetal_paises["ano"]== 2016) & (df_cobertura_vegetal_paises["country"] == "Democratic Republic of the Congo")]["perda_cobertura_vegetal"].values[0]
    perda_cobertura_2016_brasil = df_cobertura_vegetal_paises[(df_cobertura_vegetal_paises["ano"]== 2016) & (df_cobertura_vegetal_paises["country"] == "Brazil")]["perda_cobertura_vegetal"].values[0]
    perda_cobertura_2016_indonesia = df_cobertura_vegetal_paises[(df_cobertura_vegetal_paises["ano"]== 2016) & (df_cobertura_vegetal_paises["country"] == "Indonesia")]["perda_cobertura_vegetal"].values[0]

    st.write(f"No ano de 2016 o mundo perdeu {perda_cobertura_2016}km² de vegetação natural, No ano de 2016 o Brasil perdeu {perda_cobertura_2016_brasil}km² de vegetação natural, No ano de 2016 a Indonésia perdeu {perda_cobertura_2016_indonesia}km² de vegetação natural, No ano de 2016 Congo perdeu {perda_cobertura_2016_congo}km² de vegetação natural.")

    representacao_2016 = (perda_cobertura_2016_brasil+perda_cobertura_2016_indonesia+perda_cobertura_2016_congo)/perda_cobertura_2016
    representacao_2016_brasil = perda_cobertura_2016_brasil/perda_cobertura_2016
    st.write(f"Juntos esses países representaram {round(representacao_2016,3)}% da perda global no ano de 2016. O Brasil, o país que mais perdeu naquele ano, apresenta {round(representacao_2016_brasil,3)}% de impacto global.")

    st.write("Sabendo que o Brasil, Congo e a Indonesia exercem um grande impacto no cenário global no ano de 2016, torna-se vital o entendimento desses países ao longo dos anos. A visualização disso fica mais claro no próximo gráfico")

    df_paises = df_cobertura_vegetal_paises[df_cobertura_vegetal_paises["country"].isin(["Democratic Republic of the Congo", "Brazil", "Indonesia"])]
    df_impacto_cobertura_vegetal_paises = df_paises.merge(df_geral, how="inner", on="ano")[["country", "ano", "perda_cobertura_vegetal_x", "perda_cobertura_vegetal_y"]]
    df_impacto_cobertura_vegetal_paises["%_contribuicao_pais"] = df_impacto_cobertura_vegetal_paises["perda_cobertura_vegetal_x"] / df_impacto_cobertura_vegetal_paises["perda_cobertura_vegetal_y"]
    df_impacto_cobertura_vegetal_paises["%_contribuicao_pais"] = df_impacto_cobertura_vegetal_paises["%_contribuicao_pais"].round(3) * 100
    stacked_bar_plot = px.bar(data_frame=df_impacto_cobertura_vegetal_paises, x="ano", y="%_contribuicao_pais", color="country",title="% que cada país representa no cenário global de perda de cobertura vegetal.", text_auto=True)
    stacked_bar_plot.update_yaxes(range=[0, 100], ticksuffix="%")
    stacked_bar_plot.add_hline(y=50, line_dash="dash", line_color="black")
    stacked_bar_plot.add_annotation(x=2002, y=45, text="50%", showarrow=False, font=dict(color="black", size=14))
    stacked_bar_plot.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
    st.plotly_chart(stacked_bar_plot)

    st.write("Em todos os anos do estudo (2002 até 2022) os três países representam mais de 50% da perda de cobertura vegetal, em alguns anos O brasil passa disso sozinho.")
    st.write("O entendimento desses valores e da representação de influência desses páises é de extrema importância para a concepção de medidas mais eficientes para a preservação do ambiente.")
    st.write("Estudando o Brasil por exemplo, o país teve uma perda de 28309km² no ano de 2016, desse número, 7893km² foram só de desmatamento de áreas na amazônia, o que corresponde a 28% da cobertura vegetal perdida no país naquele ano.")
    st.write("É sempre bom lembrar que o desmatamento é diferente da perda de cobertura vegetal. Desmatamento é a remoção ou destruição de florestas e outras formas de vegetação natural pela ação humana. Perda de cobertura vegetal refere-se a perda de vegetação com mais de 5m de altura por ação do homem ou não, alguns dos fatores considerados são: colheita mecânica, incêndios, doenças, danos causados por tempestades, desmatamento... A imagem embaixo deixa isso mais claro.")
    st.image("./assets/desmatamento_perda.png")

with conclusao:
    st.header("Conclusão")