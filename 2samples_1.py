import pandas as pd
from scipy.stats import norm,t
from routes import datos

df=pd.read_csv(datos/"READING.CSV")
print(df.head())
print(df["METHOD"].value_counts())

df=df.groupby("METHOD")["SCORE"].agg(["mean", "std", "count"])
print(df)

