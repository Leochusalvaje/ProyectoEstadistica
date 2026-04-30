from scipy.stats import norm, t

def IC_two_pops_use_z(media1, media2, s1, s2, n1, n2, alpha):
    # Diferencia de medias
    diff = media1 - media2
    
    # Error estándar de la diferencia de medias
    se_diff = ((s1**2 / n1) + (s2**2 / n2))**0.5
    
    # Valor crítico z para el nivel de confianza dado
    z_critico = norm.ppf(1 - alpha/2)
    
    # Margen de error
    margen_error = z_critico * se_diff
    

    # Intervalo de confianza
    lower_bound = diff - margen_error
    upper_bound = diff + margen_error
    print(f"Valor crítico z para un nivel de confianza del {100*(1-alpha)}%: {z_critico:.3f}")
    print(f"Margen de error: {margen_error:.3f}")
    print(f"Intervalo de confianza: [{lower_bound:.3f}, {upper_bound:.3f}]")    
    print(f"Diferencia de medias: {diff:.3f}")
    return lower_bound, upper_bound
