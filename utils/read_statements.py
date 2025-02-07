import pandas as pd



def read_log(file = "Statement log.csv"):
    df = pd.read_csv(file)
    return df



def read_summaries(file = "Statement summary.csv"):
    df = pd.read_csv(file, delimiter=";")
    return df


