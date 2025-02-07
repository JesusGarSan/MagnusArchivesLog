import streamlit as st
from utils.read_statements import *
from utils.write_statements import *
from utils.statement_checks import *

# Page config
import config.init
config.init.init("Add statements", "🪶")


if True: # Authentication verification (to be implemented)
    # with st.form("New statement", enter_to_submit=False):
        st.subheader("Add a new statement to the log")
        col = st.columns(4)
        episode = col[0].number_input("Episode",min_value=0,max_value=1000)
        title   = col[1].text_input("Title",max_chars=100,placeholder="The Puppeteer")
        author  = col[2].text_input("Statement given by:",max_chars=100,placeholder="Mathew Smith")
        statement_date    = col[3].date_input("Statement given on:")

        start_date = col[0].date_input("Start date of the events:")
        end_date   = col[1].date_input("End date of the events:")
        location   = col[2].text_input("Main Location:",placeholder="Doncaster, UK", max_chars=50)
        eyes       = col[3].selectbox('Were "eyes" mentioned?',["Yes", "No"], 1)

        id = '#'+str(statement_date).replace('-', '')[1:]
        ID = col[0].text_input("Statement ID", id)

        short_summary = st.text_input("Short summary:", placeholder="Max. 200 charaxters", max_chars=200)

        form_data = {
            "Episode": episode,
            "Title": title,
            "Statement ID": ID,
            "Satatement given by": author,
            "Statement given on": statement_date,

            "Start of events": start_date,
            "End of events": end_date,
            "Main Location": location,
            "Short Summary": short_summary,
            "Eyes Mentioned": eyes,
        }

        # submitted = st.form_submit_button()
        submitted = st.button("Submit")
        if submitted:
            valid, text = write_statement(form_data)
            if valid:
                st.success(text)
            else:
                st.error(text)