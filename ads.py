import pandas as pd

df = pd.read_csv("data/creditcard.csv")

fraud_sample = df[df["Class"] == 1].iloc[0]

print(fraud_sample.drop("Class").values.tolist())