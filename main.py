import numpy
from scipy.stats import norm,t


# niveles de confianza
confianzas = [0.80, 0.90, 0.95, 0.98, 0.99]
respuestas= ["a","b","c","d","e"]

# El problema proporcioan una muestra de tamaño n=7, por lo que los grados de libertad serán gl = n - 1
n = 7
gl = n - 1


print("Confianza |   Z   |   t")
print("-------------------------")

contador=0
for c in confianzas:
    alfa = 1 - c
    alfa_2 = alfa / 2
    
    # valor crítico Z
    z = norm.ppf(1 - alfa_2)
    
    # valor crítico t
    t_val = t.ppf(1 - alfa_2, df=gl)
    
    print(f"{respuestas[contador]} | {c:.2f}     | {z:.3f} | {t_val:.3f}")
    contador+=1