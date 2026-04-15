import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df