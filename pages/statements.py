import streamlit as st
from utils.read_statements import *

# Page config
import config.init
config.init.init("Statements", "📼")


# Page starts
tab_labels = ["Statement log", "Statements summary"]
tabs = st.tabs(tab_labels)
with tabs[0]:
    st.header(tab_labels[0])
    log = read_log()
    st.dataframe(log, hide_index=True)
with tabs[1]:
    st.header(tab_labels[1])
    summaries = read_summaries()
    st.dataframe(summaries, hide_index=True)    




# st.data_editor(
#     data_df,
#     column_config={
#         "apps": st.column_config.LinkColumn(
#             "Trending apps",
#             help="The top trending Streamlit apps",
#             validate=r"^https://[a-z]+\.streamlit\.app$",
#             max_chars=100,
#             display_text=r"https://(.*?)\.streamlit\.app"
#         ),
#         "creator": st.column_config.LinkColumn(
#             "App Creator", display_text="Open profile"
#         ),
#     },
#     hide_index=True,
# )