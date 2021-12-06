import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Hello World')

data = pd.read_csv('../Data/export.csv', sep=',', encoding='utf-8')

data.columns
test = data[['brand', 'stockX', 'retailPrice']].groupby(['brand']).agg('mean')
# fig = px.bar(test, x='retailPrice', y='stockX', title="test")
# fig.show()

st.line_chart(test)