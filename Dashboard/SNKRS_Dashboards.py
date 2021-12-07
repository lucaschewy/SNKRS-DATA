import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Hello World')

data = pd.read_csv('../Data/export.csv', sep=',', encoding='utf-8')
data["profit"] = data["stockX"] - data["retailPrice"]

data.columns

##################################
# Global
##################################

# évolution du marché du resell
# vérifier l'évolution du resell, il y a t il une saisonalité
# prix retail & prix resell en fonction de la date (moyenne)

test = data[['profit', 'stockX', 'retailPrice', 'releaseDate']].groupby(['releaseDate']).agg('mean').sort_values(by='releaseDate', ascending=True)
test.reset_index(inplace=True)
st.write(test)
fig = px.histogram(test, x="releaseDate", y=["profit", 'stockX', 'retailPrice'])
st.plotly_chart(fig)

# vision par marque
# quelle marque fonctionne le mieux, est-ce qu'il y a des périodes
# prix retail & prix resell en fonction de la date et de la marque (moyenne)

test2 = data[['profit', 'brand', 'releaseDate']].groupby(['brand']).agg('mean')
st.write(test2)
fig2 = px.bar(test2)
st.plotly_chart(fig2)

# vision des meilleurs silhouette
# prix retail & prix resell en fonction de la silhouette

test3 = data[['profit', 'silhoutte']].groupby(['silhoutte']).agg('mean').sort_values(by='profit', ascending=False)
st.write(test3)
fig3 = px.bar(test3[:50])
st.plotly_chart(fig3)

st.image(data["thumbnail"][1])

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