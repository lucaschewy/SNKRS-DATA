# Import des librairies
import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

def app():
    # Contexte et titre du dashboard
    st.title('General Data')
    st.write('Welcome to this dashboard that will allow you to analyze and understand the sneaker resale market.')

    # Import de données et création du DataFrame
    data = pd.read_csv('../Data/export.csv', sep=',', encoding='utf-8')
    
    # Ajout de la colonne calculé pour obtenir le profit pour chaque paire
    data["profit"] = data["stockX"] - data["retailPrice"]

    # Affichage et calculs des principaux KPI
    profitMoyen = str(round(data["profit"].mean(), 2)) + "$"
    retailMoyen = str(round(data["retailPrice"].mean(), 2)) + "$"
    resellMoyen = str(round(data["stockX"].mean(), 2)) + "$"
    profitPercentage = str(round(((data["stockX"].mean() - data["retailPrice"].mean()) / data["retailPrice"].mean()), 2) * 100) + "%"

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Average Profit", value=profitMoyen, delta = profitPercentage)
    col2.metric(label="Average Retail Price", value=retailMoyen)
    col3.metric(label="Average Resell Price", value=resellMoyen)

    # DataFrame pour analysser l'évolution du marché
    prixEvo = data[['profit', 'stockX', 'retailPrice', 'releaseDate']].groupby(['releaseDate']).agg('sum').sort_values(by='releaseDate', ascending=True)
    prixEvo.reset_index(inplace=True)

    # Slider pour pouvoir sélectioner la plage de date souhaitée
    tailleDF = len(prixEvo) - 1
    prixEvo["releaseDate"] = pd.to_datetime(prixEvo["releaseDate"])
    startRange = prixEvo["releaseDate"][0].to_pydatetime()
    endRange = prixEvo["releaseDate"][tailleDF].to_pydatetime()
    dateRange = st.slider('Select a range of date', min_value = startRange, value = (startRange, endRange),max_value = endRange, format = "YYYY-MM-DD")
    startDate, endDate = dateRange
    startDate = str(startDate.date())
    endDate = str(endDate.date())

    # Query en fonction de la date et affichage de l'histogramme
    prixRangeEvo = prixEvo.query('releaseDate >= "' + startDate + '" and releaseDate <= "' + endDate + '"')
    fig = px.histogram(prixRangeEvo, x="releaseDate", y=["profit", 'retailPrice', 'stockX'], title = 'Evolution of the Sneakers market', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig)

    # DataFrame pour analyser la performance par marque
    brandProfit = data[['profit', 'brand', 'releaseDate']].groupby(['brand']).agg('mean').sort_values(by='profit', ascending=False).dropna()
    brandProfit.reset_index(inplace=True)

    # Affichage de l'histogramme
    fig2 = px.bar(brandProfit, x="profit", y="brand", color="brand", orientation='h', title = 'Brand Profit', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig2)

    # Vision des meilleurs silhouettes
    bestSilhoutte = data[['profit', 'silhoutte']].groupby(['silhoutte']).agg('mean').sort_values(by='profit', ascending=False)
    bestSilhoutte.reset_index(inplace=True)

    # Affichage de l'histogramme, filtré sur le top 50
    fig3 = px.histogram(bestSilhoutte[:50], x="silhoutte", y="profit", color="silhoutte", title = 'Best Silhoutte', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig3)