import pandas
from scipy.stats import norm,t
from routes import datos
from proofHipoZyt import z_proporcion,t_media,z_sigma

df=pandas.read_csv(datos/"SKINCREAM.CSV")
serie=df["IMPROVE"]

print(df.head())

print(df.tail())

exitos=serie.value_counts()
print(exitos)


N=z_proporcion(24,33,0.6)