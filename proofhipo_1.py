import pandas
from scipy.stats import norm,t
from routes import datos
from proofHipoZyt import z_proporcion,t_media

df=pandas.read_csv(datos/"DRUGRAT.CSV")
print(df.head())
serie=df["TIME"]
media=serie.mean()
std=serie.std()
print(f"Desviacion estandar= {std}")

print(f"Media poblacional= {media}")

N=t_media(media,1.2,std,100)

