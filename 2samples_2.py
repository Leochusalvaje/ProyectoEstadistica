import pandas as pd
from scipy.stats import norm,t
from routes import datos

df=pd.read_csv(datos/"GRADPAIRS.CSV")
#print(df.head())
df["d"] = df["MALE"] - df["FEMALE"]
d_mean = df["d"].mean()
d_std = df["d"].std()
n = len(df)

print(f"Media de las diferencias (d̄): {d_mean:.4f}")
print(f"Desviación estándar de las diferencias (s_d): {d_std:.4f}")
print(f"Tamaño de la muestra (n): {n}")     

