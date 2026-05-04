import pandas as pd
from scipy.stats import norm,t
from routes import datos

df=pd.read_csv(datos/"DIETSTUDY.CSV")
print(df.head())
print(df["DIET"].value_counts())

df=df.groupby("DIET")["WTLOSS"].agg(["mean", "std", "count"])

print(df)