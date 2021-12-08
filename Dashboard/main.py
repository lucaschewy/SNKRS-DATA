import streamlit as st

import generalData
import research
import home
PAGES = {
    "Home": home,
    "General Data": generalData,
    "Sneakers Research": research
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()