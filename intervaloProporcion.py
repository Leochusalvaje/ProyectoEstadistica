
exitos=33
z=1.96
n=38
p_m=exitos/n

Intervalo_inf = p_m - z * (p_m * (1 - p_m) / n) ** 0.5
inferior=z * (p_m * (1 - p_m) / n) ** 0.5
Intervalo_sup = p_m + z * (p_m * (1 - p_m) / n) ** 0.5
superior=z * (p_m * (1 - p_m) / n) ** 0.5
print(f"El intervalo de confianza para la proporción es: [{Intervalo_inf:.3f}, {Intervalo_sup:.3f}]")
print(f"Margen de error: [{inferior:.3f}, {superior:.3}]")