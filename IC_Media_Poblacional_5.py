import pandas as pd
from pathlib import Path
from scipy.stats import norm,t

ruta_base=Path(__file__).parent
datos=ruta_base/"datos"
nom="Egg Length"


df=pd.read_csv(datos/"NZBIRDS.CSV")
muestra=df[nom].sample(n=50,random_state=41)

# Calcular media y desviación   
intervaloc = 0.99


media_muestra=muestra.mean()
s_muestra=muestra.std()
n_muestra=len(muestra)
array_muestra = muestra.tolist()
print(array_muestra)

# Grados de libertad
gl = n_muestra - 1

# Alfa
alpha = 1 - intervaloc

# Valor crítico t
t_crit = t.ppf(1 - alpha/2, df=gl)

print(f"Muestra: n={n_muestra} | Media={media_muestra:.4f} | Desviación Estándar (s)={s_muestra:.4f} | t para un intervalo de confianza del {intervaloc*100}% con gl={gl} es t = {t_crit:.4f}")