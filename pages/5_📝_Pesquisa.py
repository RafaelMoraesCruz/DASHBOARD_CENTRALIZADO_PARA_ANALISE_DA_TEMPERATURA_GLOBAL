import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import plotly.express as px
from pandas import DataFrame
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import OLSInfluence
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

df_geral = pd.read_excel("./data/visao_geral_atributos_juntos.xlsx")
df_geral.rename(columns={"cobertura_vegetal": "perda_cobertura_vegetal"}, inplace=True)

df_cobertura_vegetal = pd.read_excel("./data/deforestation/gfw_2023_statistics_summary_clean_melted.xlsx")
df_cobertura_vegetal.rename(columns={"desmatamento": "perda_cobertura_vegetal"}, inplace=True)

df_degelo = pd.read_excel("./data/sea-ice-coverage/seaice-treated.xlsx")
df_degelo.rename(columns={"Year": "ano", "ice-extent": "extensao_gelo", "hemisphere": "hemisferio"}, inplace=True)

def grafico_heatmap(df : DataFrame):
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

def grafico_paises(df: DataFrame):
    ax =sns.lineplot(data=df, x="ano", y="perda_cobertura_vegetal", hue="country",legend = 'full')
    plt.title("Perda de cobertura vegetal ao longo dos anos")
    plt.ylabel("Perda de cobertura vegetal km²")
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    return plt.show()

def grafico_perda_cobertura(df: DataFrame):
    sns.lineplot(data=df, x="ano", y="perda_cobertura_vegetal", color="green")
    sns.lineplot(data=df[df["ano"].isin([2015,2016])], x="ano", y="perda_cobertura_vegetal",color="red")
    plt.title("Perda de cobertura vegetal ao longo dos anos, cenário global")
    plt.ylabel("Perda de cobertura vegetal km²")
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    return plt.show()

def grafico_co2_paises(df: DataFrame):
    sns.lineplot(data=df, x="ano", y="total_emissao_co2", hue="pais")
    plt.title("Emissão de CO2 ao longo dos anos dos 5 países que mais emitem")
    plt.ylabel("Emissão CO2 (bilhões de toneladas)")
    return plt.show()



dados_section = st.container()
col1, col2 = st.columns(2)
eda_section = st.container()
cobertura_vegetal_analise = st.container()
emissao_co2_analise = st.container()
degelo = st.container()
teste_de_hipotese = st.container()
conclusao = st.container()

with dados_section:

    with st.container():
        st.title("Pesquisa")
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

    green_colors = ['#00FF00', '#00CC00', '#006600']
    df_paises = df_cobertura_vegetal_paises[df_cobertura_vegetal_paises["country"].isin(["Democratic Republic of the Congo", "Brazil", "Indonesia"])]
    df_impacto_cobertura_vegetal_paises = df_paises.merge(df_geral, how="inner", on="ano")[["country", "ano", "perda_cobertura_vegetal_x", "perda_cobertura_vegetal_y"]]
    df_impacto_cobertura_vegetal_paises["%_contribuicao_pais"] = df_impacto_cobertura_vegetal_paises["perda_cobertura_vegetal_x"] / df_impacto_cobertura_vegetal_paises["perda_cobertura_vegetal_y"]
    df_impacto_cobertura_vegetal_paises["%_contribuicao_pais"] = df_impacto_cobertura_vegetal_paises["%_contribuicao_pais"].round(3) * 100
    stacked_bar_plot = px.bar(data_frame=df_impacto_cobertura_vegetal_paises,
                               x="ano", y="%_contribuicao_pais",
                                 color="country", 
                                 title="% que cada país representa no cenário global de perda de cobertura vegetal.",
                                   text_auto=True, color_discrete_sequence=green_colors)
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

with emissao_co2_analise:
    st.header("4. Emissão de co2")
    st.write("Seguindo a fórmula da cobertura vegetal, torna-se necessário a compreensão desse aspecto no cenário micro(países) para ver o impacto real dessa variável e o que pode estar causando números tão altos.")
    df_emissao_co2 = pd.read_csv("./data/CO2/co2-fossil-plus-land-use.csv")
    df_emissao_co2 = df_emissao_co2[~df_emissao_co2["Entity"].isin(["North America (excl. USA)", "Low-income countries","World", "Asia", "Upper-middle-income countries", "High-income countries", "Asia (excl. China and India)", "Europe", "Lower-middle-income countries", "North America", "European Union (28)", "Europe (excl. EU-27)", "South America", "European Union (27)", "Europe (excl. EU-28)", "Africa"])]
    df_emissao_co2.rename(columns={"Entity": "pais", "Code" : "codigo", "Year": "ano", "total_co2_emissions": "total_emissao_co2", "co2_from_land_use" : "emissao_co2_uso_terra", "co2_from_other_sources": "emissao_co2_outras_fontes"}, inplace=True)
    st.dataframe(df_emissao_co2.sort_values(by="total_emissao_co2", ascending=False), hide_index=True)
    st.write("Com a visão inicial é possível afirmar que os países que mais emitem CO2 são China, Estados Unidos e Brasil. Mas é necessário um estudo mais afundo para dizer com certeza os países que mais emitem, por isso, o próximo passo é analisar a média e a mediana de cada país. Para esse estudo os anos vão ser limitados de 2000 até 2022")
    df_emissao_co2 = df_emissao_co2[df_emissao_co2["ano"] >= 2000]
    st.write("<strong>Média:</strong>", unsafe_allow_html=True)
    st.dataframe(df_emissao_co2[["pais", "total_emissao_co2"]].groupby("pais").mean().sort_values(by="total_emissao_co2", ascending=False).head(6))
    st.write("A média das emissões totais de CO2 revela uma visão geral das contribuições ao longo dos anos. A China lidera com uma média de aproximadamente 8,657 bilhões de toneladas, seguida pelos Estados Unidos com cerca de 5,631 bilhões de toneladas. Estes números refletem o rápido crescimento industrial e econômico da China durante o período, bem como o papel dos Estados Unidos como uma economia desenvolvida com altos níveis de consumo energético.")
    st.write("A Índia, Brasil, Rússia e Indonésia também aparecem na lista, mas com médias significativamente menores.")
    st.write("<strong>Mediana:</strong>", unsafe_allow_html=True)
    st.dataframe(df_emissao_co2[["pais", "total_emissao_co2"]].groupby("pais").median().sort_values(by="total_emissao_co2", ascending=False).head(6))
    st.write("Os dados de mediana oferecem uma perspectiva diferente, mostrando o valor central das emissões ao longo do período, o que pode diminuir o impacto de outliers. A China ainda lidera com uma mediana de 9,593 bilhões de toneladas, superior à média, indicando que suas emissões têm sido consistentemente altas ao longo dos anos.")
    df_emissao_co2_paises = df_emissao_co2[df_emissao_co2["pais"].isin(["China", "United States", "India", "Russia", "Brazil"])]
    st.pyplot(grafico_co2_paises(df_emissao_co2_paises))
    st.write("O gráfico apresenta a grande transformação industrial no mundo, China cresceu muito o número de fábricas em seu território o que explica ter um aumento de emissões ao longo dos anos. EUA mudou um pouco a sua estratégia, fazendo com que as indústrias de suas empresas se concentrassem em países emergentes, como: China, India... o que é possível ver no gráfico, pois a emissão desses países foram as que mais subiram de 2000 para 2022.")
    df_emissao_co2_porcentagem_global = df_emissao_co2.groupby("ano", as_index=False).sum()[["ano", "total_emissao_co2"]]
    df_emissao_co2_porcentagem_global = df_emissao_co2_paises.merge(df_emissao_co2_porcentagem_global, how="inner", on="ano")
    df_emissao_co2_porcentagem_global["%_contribuicao_pais"] = df_emissao_co2_porcentagem_global["total_emissao_co2_x"] / df_emissao_co2_porcentagem_global["total_emissao_co2_y"]
    df_emissao_co2_porcentagem_global["%_contribuicao_pais"] = df_emissao_co2_porcentagem_global["%_contribuicao_pais"].round(2) * 100
    co2_color_palete = ["#B5C18E","#481E14", "#F7DCB9", "#DEAC80", "#B99470"]
    stacked_bar_plot = px.bar(data_frame=df_emissao_co2_porcentagem_global,
                               x="ano", y="%_contribuicao_pais",
                                 color="pais", 
                                 title="% que cada país representa no cenário global de emissão de CO2.",
                                   text_auto=True, color_discrete_sequence=co2_color_palete)
    stacked_bar_plot.update_yaxes(range=[0,100] , ticksuffix="%")
    stacked_bar_plot.add_hline(y=50, line_dash="dash", line_color="black")
    stacked_bar_plot.add_annotation(x=2000, y=55, text="50%", showarrow=False, font=dict(color="black", size=14))
    stacked_bar_plot.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
    st.plotly_chart(stacked_bar_plot)
    st.write("É notório que depois de 2004 os 5 países que mais emitem passam a ser responsáveis por mais de 50% da emissão de todo o planeta. Juntando os últimos dois gráficos percebe-se que embora haja reuniões e acordos para a redução da emissão desse gás, quase nenhuma entidade as respeita. A única entidade que parece respeitar esses acordos é o Brasil.")

with degelo:
    st.header("5. Cobertura de gelo")
    st.write('A coluna "ano" mostra o ano em que os dados foram coletados, ajudando a ver como a quantidade de gelo mudou ao longo do tempo. A coluna "hemisferio" o hemisfério norte ou sul, o que é importante porque os padrões de gelo podem ser diferentes em cada região. A última coluna diz o tamanho da área coberta por gelo, o que nos ajudar a entender a extensão do gelo em cada ano e hemisfério. Essas informações são importantes para estudar as mudanças no gelo ao longo do tempo e entender melhor as consequências das mudanças climáticas.')
    st.dataframe(df_degelo, hide_index=True)
    st.write("O gráfico abaixo mostra a % de cobertura de gelo em cada hemisfério em relação com o cenário mundial")
    tradutor_hemisferio = {"north": "hemisferio_norte", "south": "hemisferio_sul"}
    df_degelo["hemisferio"] = df_degelo["hemisferio"].apply(lambda x: tradutor_hemisferio[x])
    df_degelo_completo = df_degelo.copy()
    df_degelo = df_degelo[df_degelo["ano"] > 2000]
    df_por_ano = df_degelo.groupby("ano").agg({"extensao_gelo": "sum"})
    df_degelo = df_por_ano.merge(right=df_degelo, on="ano", how="left")
    df_degelo["representacao_total"] = df_degelo["extensao_gelo_y"] / df_degelo["extensao_gelo_x"]
    df_degelo["representacao_total"] = df_degelo["representacao_total"].round(2) * 100
    stacked_bar_plot = px.bar(data_frame=df_degelo,
                               x="ano", y="representacao_total",
                                 color="hemisferio", 
                                 title="% que cada hemisfério representa no cenário global de cobertura de gelo",
                                   text_auto=True)
    stacked_bar_plot.update_yaxes(range=[0,100] , ticksuffix="%")
    stacked_bar_plot.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
    st.plotly_chart(stacked_bar_plot)
    st.write("Existe um balanço entre os hemisférios de cobertura de gelo, sendo 8% a máxima diferença que os hemisférios tiveram de representação. O ano de 2024 está tem uma grande diferença pois esse trabalho foi feito no primeiro semestre de 2024, logo o hemisfério sul ainda não teve o perído de inverno e o norte não teve o período de verão. Isso justifica a presença de uma área maior de gelo no hemisfério norte.")
    st.write("Para compreensão de números, o Gráfico de linhas fica de melhor visualização, esse gráfico pode ser encontrado abaixo: ")
    palette = sns.color_palette("mako_r", 6)
    sns.lineplot(df_degelo_completo, x="ano", y="extensao_gelo", hue="hemisferio", style="hemisferio", palette=palette, markers=True, dashes=False)
    st.pyplot(plt.show())
    st.write("Pelo gráfico é possível observar alguns insights importantes. O mais importânte proposto aqui é a divergência da cobertura de gelo entre os hemisférios depois do ano de 2002. O hemisfério sul começa a apresentar uma área bastante superior ao hemisfério norte, coisa que não vinha ocorrendo e que se prolonga de 2002 até o ano de 2023.")
    diff_2015 = df_degelo_completo[(df_degelo_completo["ano"] == 2015) & (df_degelo_completo["hemisferio"] == "hemisferio_sul")]["extensao_gelo"].values[0] - df_degelo_completo[(df_degelo_completo["ano"] == 2015) & (df_degelo_completo["hemisferio"] == "hemisferio_norte")]["extensao_gelo"].values[0]
    st.write(f"A maior diferença é atingida no ano de 2015. Nesse ano os hemisférios apresentam {round(diff_2015,3)} milhões de km² de diferença, sendo hemisfério sul apresenta maior cobertura de gelo.")

with teste_de_hipotese:
    st.header("6. Teste de Hipótese")
    st.write("Para ressaltar os resultados obtidos com esse estudo, se torna necessário a implementação de um teste de hipótese para envolver uma análise mais estatísta dos dados. O método estatístico escolhido foi o de regressão linear múltipla.")
    st.write("<strong>Hipóteses a serem testadas:</strong>", unsafe_allow_html=True)
    st.write("1-H0 As variáveis dependentes possuem valores significativos na temperatura global")
    st.write("2-H1 As variáveis dependentes não possuem valores significativos na temperatura global")
    st.write("Esse tipo de teste foi escolhido pois avalia o impacto combinado das variáveis independentes (emissão de CO2, perda de cobertura vegetal e cobertura de gelo) na variável target/dependente (temperatura global)")
    # Regressão linear múltipla
    df_geral_processed = df_geral.copy()
    scaler = StandardScaler()

    X = scaler.fit_transform(df_geral_processed[['emissoes_totais_co2', 'perda_cobertura_vegetal', 'cobertura_gelo', 'ano']])
    print(X)
    X = pd.DataFrame(X)
    print(X)
    X.rename(columns={0: 'emissoes_totais_co2', 1: "perda_cobertura_vegetal", 2: "cobertura_gelo", 3: "ano"}, inplace=True)
    y = df_geral_processed['celsius']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    influence = OLSInfluence(model)
    standard_resid = influence.resid_studentized_internal

    st.write('Como o foco do trabalho não é aprendizado de máquina, foi escolhido um modelo simples, o <a href="https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html">Ordinary Least Squares </a>, para que tivesse maior eficiência, antes do modelo ser executado foi feito um pré-processamento, pois os dados eram muito distantes com relação a variação de cada variável. Os resultados estatísticos obtidos foram:', unsafe_allow_html=True)
    st.write('R-squared (R²): 0.382')
    st.write('F-statistic: 2.477')
    st.write('Prob (F-statistic): 0.0859')
    st.write("<strong>P>|t|</strong>", unsafe_allow_html=True)
    st.write("   Emissões Totais de CO2: 0.787")
    st.write("   Perda de Cobertura Vegetal: 0.251")
    st.write("   Cobertura de Gelo: 0.985")
    st.write("   Ano: 0.440")
    st.write("   <strong>Nenhum dos p-valor é significativo</strong>", unsafe_allow_html=True)

with conclusao:
    st.header("7. Conclusao")
    st.write("Com base nos resultados, conclui-se que as variáveis emissões totais de CO2, perda de cobertura vegetal, cobertura de gelo e ano não têm um impacto estatisticamente significativo na temperatura global dentro do contexto deste modelo específico. A análise do p-valor da estatística F e dos coeficientes individuais indica que não podemos rejeitar a hipótese nula (H0), sugerindo que as variáveis independentes analisadas não são atributos significativos da temperatura global.")
    st.write("Esses resultados indicam que outras variáveis, além das analisadas neste estudo, podem ter um impacto mais significativo na temperatura global. ")