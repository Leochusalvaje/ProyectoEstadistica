import numpy
from scipy.stats import norm,t

def z_proporcion(exitos,n,p_nulo):
    proporcion=exitos/n
    z=(proporcion-p_nulo)/(((p_nulo*(1-p_nulo))/n)**(1/2))
    p=norm.pdf(z)
    return z,p


N=z_proporcion(529,1400,0.4)
print(f"El valor de z es {N[0]}\n el valor de p= {N[1]}")