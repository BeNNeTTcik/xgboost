import pandas as pd


def df(dataset):
    df = pd.read_csv(dataset)
    df = df.drop(columns=["user", "ts"])
    y = df["target"]
    X = df.drop(columns=["target"])
    # df.head()
    return df, X, y
