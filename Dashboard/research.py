# app2.py
import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    st.title('APP2')
    st.write('Welcome to app2')

    data = pd.read_csv('../Data/export.csv', sep=',', encoding='utf-8')
    data["profit"] = data["stockX"] - data["retailPrice"]

    options = st.multiselect('What are your favorite colors',data["brand"].unique())
    xxuix = data.loc[data['brand'].isin(options)]

    if options :
        options2 = st.multiselect('What are your favorite colors',xxuix["silhoutte"].unique())
        xxuix2 = xxuix.loc[data['silhoutte'].isin(options2)]
    else :
        options2 = st.multiselect('What are your favorite colors',data["silhoutte"].unique())
        xxuix2 = data.loc[data['silhoutte'].isin(options2)]
    
    
    if options :
        if options2 :
            option = st.selectbox('How would you like to be contacted?', xxuix2["shoeName"])
            st.write('You selected:', option)
        else :
            option = st.selectbox('How would you like to be contacted?', xxuix["shoeName"])
            st.write('You selected:', option)
    else :
        if options2 :
            option = st.selectbox('How would you like to be contacted?', xxuix2["shoeName"])
            st.write('You selected:', option)
        else :
            option = st.selectbox('test', data["shoeName"])
            st.write('You selected:', option)

    if st.button('Rechercher'):
        st.write(option)
        knonvc = data.loc[data['shoeName'] == option]
        pd.set_option("display.max_colwidth", 10000)
        imgtet = knonvc["thumbnail"].to_string(header = False, index = False)
        st.image(imgtet)


        test234679 = knonvc["profit"].to_string(header = False, index = False)
        test234679sdfe = knonvc["retailPrice"].to_string(header = False, index = False)
        test23467dd9sdfe = knonvc["stockX"].to_string(header = False, index = False)
        calcul = (int(knonvc["stockX"]) - int(knonvc["retailPrice"])) / int(knonvc["retailPrice"]) 
        calculFinal = str(round(calcul*100,2)) + "%"
        col10, col20, col30 = st.columns(3)
        col10.metric(label="Profit", value=test234679, delta = calculFinal)
        col20.metric(label="retail", value=test234679sdfe)
        col30.metric(label="ressell", value=test23467dd9sdfe)
        
        description = knonvc["description"].to_string(header = False, index = False)
        st.write(description)
    else:
        st.write('Goodbye')