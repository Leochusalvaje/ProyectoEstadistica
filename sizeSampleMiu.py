import pandas as pd
from pathlib import Path
from scipy.stats import norm

def z_score(niveldeconfianza):
    alpha=1-niveldeconfianza
    #alpha/2 es la cola izquierda y alpha/2+niveldeconfianza es la derecha
    r=norm.ppf(alpha/2)
    return r




#tamaño muestral

def size_sample(z_score,std_pop,Error):
    numerador=z_score*std_pop
    n=(numerador/Error)**2
    return n,numerador


confianza=0.90
desviacion=10
error=4

print(f"El tamaño de la muestra es: {size_sample(z_score(confianza),desviacion,error)[0]}")
print(f"El numerador es: {size_sample(z_score(confianza),desviacion,error)[1]}")
print(f"El z_crtico es: {z_score(confianza)}")