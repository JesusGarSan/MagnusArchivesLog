from utils.read_statements import *

def check_form_data(form_data):
    df = read_log()
    episodes = df["Episode"]
    IDs = df["Statement ID"]

    id = form_data["Statement ID"]
    ep = form_data["Episode"]
    title = form_data["Title"]
    author = form_data["Statement given by"]

    if title =="":
        return False, "Add a title to the statement."
    if author =="":
        return False, "Specify the name of the person who gave the statement."
    if id in IDs.values:
        return False, f"ID {id} is already in the log"
    if ep in episodes:
        return False, f"Episode {ep} if already in the log"
    return True, "Click to submit the statement"