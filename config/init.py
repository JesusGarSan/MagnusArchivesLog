import streamlit as st
from config.interface import header

def init(title = None, icon=None, layout="wide", sidebar="collapsed"):
    st.set_page_config(title, icon, layout, sidebar)
    # Hide sidebar expander
    st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    header()
    return
