import pandas as pd
from pathlib import Path
from scipy.stats import norm,t

ruta_base=Path(__file__).parent
datos=ruta_base/"datos"
nom="Length"


df=pd.read_csv(datos/"TURTLES.CSV")

print(df[nom])

# Calcular media y desviación

intervaloc=0.99

media=df[nom].mean()
s=df[nom].std()
n=len(df[nom])
gl=n-1
alpha = 1-intervaloc
t_crit = t.ppf(1 - alpha/2, df=5)

print(f"tortugas: n={n} | Media={media:.2f} | Desviación Estándar (s)={s:.4f} | t para un intervalo de confianza del {intervaloc*100}% con gl=5 t ={t_crit:.4f}")

