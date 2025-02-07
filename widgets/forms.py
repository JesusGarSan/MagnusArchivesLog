import streamlit as st

def statement_log_form(key,ep=0, tit="",aut="",date=None,start=None,end=None,loc="",eye=1,id=None,sum=""):
    col = st.columns(4)
    if str(date) == "nan": date = None;
    if str(start) == "nan": start = None;
    if str(end) == "nan": end = None;
    if str(loc) == "nan": loc = ""
    if str(sum) == "nan": sum = ""
    episode = col[0].number_input("Episode",min_value=0,max_value=1000,value=ep,key=key+"_ep")
    title   = col[1].text_input("Title",max_chars=100,placeholder="The Puppeteer",value=tit,key=key+"_tit")
    author  = col[2].text_input("Statement given by:",max_chars=100,placeholder="Mathew Smith",value=aut,key=key+"_au")
    statement_date    = col[3].date_input("Statement given on:",value=date,key=key+"_date")

    start_date = col[0].date_input("Start date of the events:",value=start,key=key+"_start")
    end_date   = col[1].date_input("End date of the events:",value=end,key=key+"_end")
    location   = col[2].text_input("Main Location:",placeholder="Doncaster, UK", max_chars=50,value=loc,key=key+"_loc")
    eyes       = col[3].selectbox('Were "eyes" mentioned?',["Yes", "No"], eye,key=key+"_eye")

    if id == None:
        if statement_date == None: id = None
        else: id = '#'+str(statement_date).replace('-', '')[1:]
    ID = col[0].text_input("Statement ID", id)

    short_summary = st.text_input("Short summary:", placeholder="Max. 200 charaxters", max_chars=200,value=sum,key=key+"_sum")

    return {
        "Episode": episode,
        "Title": title,
        "Statement ID": ID,
        "Statement given by": author,
        "Statement given on": statement_date,

        "Start of events": start_date,
        "End of events": end_date,
        "Main Location": location,
        "Short Summary": short_summary,
        "Eyes Mentioned": eyes,
    }

def statement_summary_form(key, sum="",jon="",notes="",char=""):
    cols = st.columns(2)
    summary = cols[0].text_area("Summary", sum,placeholder="Summary of the statement", key=key+"_sum")
    characters = cols[1].text_area("Characters (separated by commas)",char, placeholder="eg.:Michael Wiles (author of the statement), Saoirse Wiles (daughter)", key=key+"_char")
    jon_notes = cols[0].text_area("Jonathan's Notes",jon, placeholder="Archivist's notes", key=key+"_jon")
    notes = cols[1].text_area("Notes", notes,placeholder="Additional notes", key=key+"_notes")
    
    return {
        "Summary": summary,
        "Jonathan's Notes": jon_notes,
        "Notes": notes,
        "Characters": characters,
    }