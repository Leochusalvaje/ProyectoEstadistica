import numpy
from scipy.stats import norm,t

def z_proporcion(exitos,n,p_nulo):
    proporcion=exitos/n
    std_error=((p_nulo*(1-p_nulo))/n)**(1/2)
    z=(proporcion-p_nulo)/std_error

    p=norm.cdf(z)
    print(f"Estandar error= {std_error}")
    print(f"El valor de z es {z}\n el valor de p= {p}")
    return z,p

def z_sigma(media_muestral,media_poblacional,std_muestral,n):
    z_critico=(media_muestral-media_poblacional)/(std_muestral/(n**(1/2)))
    p=norm.cdf(z_critico)
    print(f"El valor de z es {z_critico}\n el valor de p= {p}")
    return z_critico,p


def t_media(media_muestral,media_poblacional,std_muestral,n):
    t_critico=(media_muestral-media_poblacional)/(std_muestral/(n**(1/2)))
    p=t.cdf(t_critico,df=n-1)
    print(f"El valor de t es {t_critico}\n el valor de p= {p}")
    return t_critico,p

#N=z_proporcion(529,1400,0.4)
