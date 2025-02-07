import streamlit as st

@st.cache_data
def header():
    col = st.columns(5)

    with col[2]:
        st.page_link("./pages/statements.py", label = "Statements", icon='📼')
    with col[4]:
        st.page_link("./pages/statements.py", label = "Add statement", icon='🪶')

