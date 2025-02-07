import csv
from utils.statement_checks import *


def write_statement(statement_data):
    valid, text = check_form_data(statement_data)
    if valid:
        with open('Statement log.csv', "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, statement_data.keys())
            w.writerow(statement_data)
        return valid, "Your statement has been recorded"
    else: return valid, text