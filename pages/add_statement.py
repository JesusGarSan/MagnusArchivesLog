import streamlit as st
from utils.read_statements import *
from utils.write_statements import *
from utils.statement_checks import *
from widgets.forms import *

# Page config
import config.init
config.init.init("Add statements", "🪶")


if True: # Authentication verification (to be implemented)
    tab_labels = ["Add a new statement to the log", "Edit existing statement"]
    tabs = st.tabs(tab_labels)
    with tabs[0]:
        st.subheader(tab_labels[0])
        form_data = statement_log_form("add");

        submitted = st.button("Submit")
        if submitted:
            valid, text = write_statement(form_data)
            if valid:
                st.success(text)
            else:
                st.error(text)

    with tabs[1]:
        st.subheader(tab_labels[1])
        options = get_identificators()
        choice = st.selectbox("Choose the statement you want to edit", options)
        id = choice[-9:-1]
        df = read_log()
        df = df[df["Statement ID"] == id];
        form_data = df.to_dict()
        
        ep  = form_data["Episode"][0]
        tit = form_data["Title"][0]
        id  = form_data["Statement ID"][0]
        aut = form_data["Statement given by"][0]
        date = form_data["Statement given on"][0]
        start = form_data["Start of events"][0]
        end = form_data["End of events"][0]
        loc = form_data["Main Location"][0]
        sum = form_data["Short Summary"][0]
        eye = form_data["Eyes Mentioned"][0]
        if eye == 'Yes': eye = 0;
        if eye == 'No': eye = 1;

        with st.expander("Statement log"):
            lod_data = statement_log_form("edit",ep,tit,aut,date,start,end,loc,eye,id,sum) 
            lod_data["Episode_old"] = ep
            lod_data["Title_old"] = tit
            lod_data["Statement ID_old"] = id
            save_log = st.button("Save changes", key="edit_log_button")
            if save_log:
                valid, text = edit_statement(lod_data)
                if valid:
                    st.success(text)
                else:
                    st.error(text)

        st.subheader("Statement summary")
        summary_data = statement_summary_form("summary")
        summary_data["Episode"] = ep
        summary_data["Title"] = tit
        summary_data["Statement ID"] = id

        save_summary = st.button("Save changes", key="edit_summary_button")
        if save_summary:
            valid, text = edit_summary(summary_data)
            if valid:
                st.success(text)
            else:
                st.error(text)
