import streamlit as st
from config.interface import header

def init(title = None, icon=None, layout="centered", sidebar="collapsed"):
    st.set_page_config(title, icon, layout, sidebar)
    header()
    return
