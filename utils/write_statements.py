import csv
from utils.statement_checks import *
from utils.read_statements import *


def write_statement(statement_data):
    valid, text = check_form_data(statement_data)
    if valid:
        with open('Statement log.csv', "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, statement_data.keys(), delimiter='|')
            w.writerow(statement_data)
        with open('Statement summary.csv', "a", newline="", encoding="utf-8") as f:
            cols = ["Episode","Title","Statement ID"]
            w = csv.DictWriter(f, cols, delimiter='|')
            w.writerow({col: statement_data[col] for col in cols})
        return valid, "Your statement has been recorded"
    else: return valid, text

def edit_statement(statement_data):
    df = read_log();
    idx = df.index[
        (df["Episode"] == statement_data["Episode_old"]) &
        (df["Title"] == statement_data["Title_old"]) &
        (df["Statement ID"] == statement_data["Statement ID_old"])
        ]
    df["Episode"][idx] = statement_data["Episode"]
    df["Title"][idx] = statement_data["Title"]
    df["Statement ID"][idx] = statement_data["Statement ID"]
    df["Statement given by"][idx] = statement_data["Statement given by"]
    df["Statement given on"][idx] = statement_data["Statement given on"]
    df["Start of events"][idx] = statement_data["Start of events"]
    df["End of events"][idx] = statement_data["End of events"]
    df["Main Location"][idx] = statement_data["Main Location"]
    df["Short Summary"][idx] = statement_data["Short Summary"]
    df["Eyes Mentioned"][idx] = statement_data["Eyes Mentioned"]


    df.to_csv("Statement log.csv", sep='|')

    return True, "Log changes have been saved correctly"


def edit_summary(statement_data):
    df = read_summaries();
    idx = df.index[
        (df["Episode"] == statement_data["Episode"]) &
        (df["Title"] == statement_data["Title"]) &
        (df["Statement ID"] == statement_data["Statement ID"])
        ]
    df["Summary"][idx] = statement_data["Summary"]
    df["Jonathan's Notes"][idx] = statement_data["Jonathan's Notes"]
    df["Notes"][idx] = statement_data["Notes"]
    df["Characters"][idx] = statement_data["Characters"]

    df.to_csv("Statement summary.csv", sep='|')

    return True, "Summary changes have been saved correctly"
