import pandas as pd



def read_log(file = "Statement log.csv"):
    df = pd.read_csv(file)
    return df