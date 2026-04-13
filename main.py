from scipy.stats import norm,t


# niveles de confianza
confianzas = [0.80, 0.90, 0.95, 0.98, 0.99]
respuestas= ["a","b","c","d","e"]

# El problema proporciona una muestra de tamaño n=7, por lo que los grados de libertad serán gl = n - 1
n = 7
gl = n - 1


print("Confianza    |   Z   |   t")
print("----------------------------")

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

print("\n Aplicaciones Ejercio 1\n")

gl_e1=49

alfa_e1=1-0.95
alfa_e1_1=1-0.99

alfa_2_e1=alfa_e1/2
alfa_2_e1_1=alfa_e1_1/2

t_e1= t.ppf(1- alfa_2_e1 ,df=gl_e1)

t_e1_1=t.ppf(1- alfa_2_e1_1,df=gl_e1)

print(f"Valor critico de t para 95% t={t_e1}\nValor critico de t para 95% t={t_e1_1}\n")



print("\n Calculamos t para un intervalo de confianzadel 95% con  45 gl\n")

gl_e1=45

alfa_e1=1-0.95


alfa_2_e1=alfa_e1/2


t_e1= t.ppf(1- alfa_2_e1 ,df=gl_e1)



print(f"Valor critico de t para 95% t={t_e1}\n")