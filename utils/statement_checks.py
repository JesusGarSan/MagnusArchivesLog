from utils.read_statements import *

def check_form_data(form_data):
    # try:
        df = read_log()
        episodes = df["Episode"]
        IDs = df["Statement ID"]

        id = form_data["Statement ID"]
        ep = form_data["Episode"]
        title = form_data["Title"]
        author = form_data["Satatement given by"]

        print(id)
        print(IDs)
        print(id in IDs)

        if title =="":
            return False, "Add a title to the statement."
        if author =="":
            return False, "Specify the name of the person who gave the statement."
        if id in IDs.values:
            return False, f"ID {id} is already in the log"
        if ep in episodes:
            return False, f"Episode {ep} if already in the log"
        return True, "Click to submit the statement"
    # except: return False, "Please fill the form"