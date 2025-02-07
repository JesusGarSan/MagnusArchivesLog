import pandas as pd

def read_log(file = "Statement log.csv"):
    df = pd.read_csv(file, delimiter="|")
    return df

def read_summaries(file = "Statement summary.csv"):
    df = pd.read_csv(file, delimiter="|")
    return df

def get_identificators(file = "Statement log.csv"):
    df = pd.read_csv(file, delimiter='|')
    episodes = df["Episode"]
    IDs = df["Statement ID"]
    titles = df["Title"]

    identificators = []
    for i, ep in enumerate(episodes):
        identificators.append(f"Ep.{ep} - {titles[i]} ({IDs[i]})")
    return identificators
