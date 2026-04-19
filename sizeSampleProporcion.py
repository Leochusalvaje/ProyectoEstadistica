import pandas as pd
from pathlib import Path
from scipy.stats import norm

def z_score(niveldeconfianza):
    alpha=1-niveldeconfianza
    #alpha/2 es la cola izquierda y alpha/2+niveldeconfianza es la derecha
    r=norm.ppf(alpha/2)
    return r


#tamaño muestral

def size_sample(z_score,pop_prop,Error):
    numerador=(z_score**2)*pop_prop*(1-pop_prop)
    n=numerador/(Error)**2
    denominador=Error**2    
    return n,numerador,denominador


confianza=0.90
proporcion=0.5
error=0.04

print(f"El tamaño de la muestra es: {size_sample(z_score(confianza),proporcion,error)[0]}")
print(f"El numerador es: {size_sample(z_score(confianza),proporcion,error)[1]}")
print(f"El denominador es: {size_sample(z_score(confianza),proporcion,error)[2]}")
print(f"El z_crtico es: {z_score(confianza)}")