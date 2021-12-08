# Import des librairies
import streamlit as st
import plotly.express as px
import pandas as pd
import time

def app():
    # Contexte et titre du dashboard
    st.title('Sneakers Research')
    st.write('This module allows you to search and analyze the details of a pair and especially the price evolution ')

    # Import de données et création du DataFrame
    data = pd.read_csv('../Data/export.csv', sep=',', encoding='utf-8')

    # Ajout de la colonne calculé pour obtenir le profit pour chaque paire
    data["profit"] = data["stockX"] - data["retailPrice"]

    # Module de sélection des marques et stockage du ou des choix
    options = st.multiselect('Brand',data["brand"].unique())
    brandChoice = data.loc[data['brand'].isin(options)]

    # Vérification si une marque a été selectionnée
    if options :

        # Si oui, affichage des silhouettes liées à cette marque
        options2 = st.multiselect('Shape',brandChoice["silhoutte"].unique())
        shapeChoice = brandChoice.loc[data['silhoutte'].isin(options2)]
    else :

        # Si non, affichage des silhouettes globales
        options2 = st.multiselect('Shape',data["silhoutte"].unique())
        shapeChoice = data.loc[data['silhoutte'].isin(options2)]
    
    # Vérification de la marque
    if options :

        # Et si shape choisie, alors sélection des paires liées
        if options2 :
            option = st.selectbox('Shoes', shapeChoice["shoeName"])

        # Et si pas de shape, alors sélection des paires liées
        else :
            option = st.selectbox('Shoes', brandChoice["shoeName"])

    # Si pas de marque
    else :

        # Et si shape, alors sélection des paires liées
        if options2 :
            option = st.selectbox('Shoes', shapeChoice["shoeName"])

        # Et si pas de shape, alors sélection des paires globales
        else :
            option = st.selectbox('Shoes', data["shoeName"])

    # Bouton pour lancer la recherche avec temps d'attente
    if st.button('Research'):
        with st.empty():
            for seconds in range(5):
                st.write(f"⏳ Please Wait")
                time.sleep(1)
            st.write("Executed")
        
        # Affichage du nom et d'un visuel de la paire
        st.title(option)
        shoe = data.loc[data['shoeName'] == option]
        pd.set_option("display.max_colwidth", 10000)
        shoeImg = shoe["thumbnail"].to_string(header = False, index = False)
        st.image(shoeImg)

        # Affichage et calculs des principaux KPI de la paire
        shoeProfit = shoe["profit"].to_string(header = False, index = False)
        shoeRetail = shoe["retailPrice"].to_string(header = False, index = False)
        shoeResell = shoe["stockX"].to_string(header = False, index = False)
        shoePercentage = str(round((int(shoe["stockX"]) - int(shoe["retailPrice"])) / int(shoe["retailPrice"]), 2)) + "%"
        col10, col20, col30 = st.columns(3)
        col10.metric(label="Profit", value=shoeProfit, delta = shoePercentage)
        col20.metric(label="retail", value=shoeRetail)
        col30.metric(label="ressell", value=shoeResell)
        
        # Affichage de la description
        description = shoe["description"].to_string(header = False, index = False)
        st.write(description)