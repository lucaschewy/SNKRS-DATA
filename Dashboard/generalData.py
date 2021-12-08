# app1.py
import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    st.title('General Data')
    st.write('Welcome to this dashboard that will allow you to analyze and understand the sneaker resale market.')


    st.image("https://cdn.dribbble.com/users/2502549/screenshots/15513115/media/d91789a62ee7d71b15f990342410143f.png?compress=1&resize=1600x1200")


    data = pd.read_csv('../Data/export.csv', sep=',', encoding='utf-8')
    data["profit"] = data["stockX"] - data["retailPrice"]

    test0 = data["profit"].mean()
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Profit moyen", value=test0)
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    ##################################
    # Global
    ##################################

    # évolution du marché du resell
    # vérifier l'évolution du resell, il y a t il une saisonalité
    # prix retail & prix resell en fonction de la date (moyenne)

    test = data[['profit', 'stockX', 'retailPrice', 'releaseDate']].groupby(['releaseDate']).agg('sum').sort_values(by='releaseDate', ascending=True)
    test.reset_index(inplace=True)
    test123 = test.query('releaseDate >= "2016/01/01"')
    fig = px.histogram(test123, x="releaseDate", y=["profit", 'retailPrice', 'stockX'])
    st.plotly_chart(fig)

    # vision par marque
    # quelle marque fonctionne le mieux, est-ce qu'il y a des périodes
    # prix retail & prix resell en fonction de la date et de la marque (moyenne)

    test2 = data[['profit', 'brand', 'releaseDate']].groupby(['brand']).agg('mean').sort_values(by='profit', ascending=False).dropna()
    test2.reset_index(inplace=True)
    fig2 = px.bar(test2, x="profit", y="brand", color="brand", orientation='h')
    st.plotly_chart(fig2)

    # vision des meilleurs silhouette
    # prix retail & prix resell en fonction de la silhouette

    test3 = data[['profit', 'silhoutte']].groupby(['silhoutte']).agg('mean').sort_values(by='profit', ascending=False)
    test3.reset_index(inplace=True)
    fig3 = px.histogram(test3[:50], x="silhoutte", y="profit", color="silhoutte")
    st.plotly_chart(fig3)

    st.image(data["thumbnail"][0])
    st.image(data["thumbnail"][1])
    st.image(data["thumbnail"][2])

    ##################################
    # Détaillé
    ##################################

    # vision centrée sur une marque
    # Est-ce qu'il y a une saisonalité pour une marque précise + top 3 silhouette de la marque
    # prix retail & prix resell en fonction de la date et de la marque filtré (moyenne)


    ##################################
    # Supplément demande un autre export
    ##################################

    # vision centrée sur une silhouette / paire
    # Vérifier le prix retail et resell de la paire dans le temps
    # prix retail & prix resell en fonction de la date et de la paire filtrée (moyenne)