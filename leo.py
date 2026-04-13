import pandas as pd
from pathlib import Path
from scipy.stats import norm,t

ruta_base=Path(__file__).parent
datos=ruta_base/"datos"
nom="dias"
columna=[nom]

df=pd.read_excel(datos/"HOSPLOS.xls", engine="xlrd",header=None,names=columna)

# print(df.tail())

# Calcular media y desviación

intervaloc=0.95

media=df[nom].mean()
s=df[nom].std()
n=len(df[nom])
gl=n-1
alpha = 1-intervaloc
t_crit = t.ppf(1 - alpha/2, df=gl)

print(f"Pacientes: n={n} | Media={media:.2f} | Desviación Estándar (s)={s:.4f} | t para un intervalo de confianza del {intervaloc*100}% con gl={gl} t ={t_crit:.4f}")