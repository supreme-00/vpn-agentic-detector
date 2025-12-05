import pandas as pd

df = pd.read_csv("data/processed/vpn_flows.csv")
print(df.shape)
print(df["label"].value_counts())
print(df.head())
