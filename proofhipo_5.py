import pandas
from scipy.stats import norm,t
from routes import datos
from proofHipoZyt import z_proporcion,t_media,z_sigma

df=pandas.read_excel(datos/"SMOKING.xls")
print(df.head())
serie=df["DL"]
media_m=serie.mean()
std=serie.std()
n=len(serie)

print(f"numero de datos= {n}")

print(f"Desviacion estandar= {std}")

print(f"Media poblacional= {media_m}")

#N=t_media(media_m,100,std,n)
#N1=z_sigma(media_m,100,std,n)

#N2=z_proporcion(88,225,0.3)
#N3=z_proporcion(10,300,0.05)
N3=z_proporcion(24,32,0.7)