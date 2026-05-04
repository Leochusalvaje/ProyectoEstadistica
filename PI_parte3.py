import pandas as pd
from pathlib import Path
import numpy as np

ruta_base=Path(__file__).parent
datos=ruta_base/"datos"

df=pd.read_csv(datos/"gss.csv",usecols=["sex","coninc","degree"])


df["degree"]=df["degree"].replace({"Bachelor":"educacion_alta",\
                                   "Graduate":"educacion_alta",\
                                   "Junior College":"educacion_alta",\
                                   "High School":"educacion_baja",\
                                   "Lt High School":"educacion_baja"})

salarioPromedioFamilia=df["coninc"].mean()
clasificacion = np.where(df["coninc"] > salarioPromedioFamilia, "ingreso_alto", "ingreso_bajo")

df["salario_clasificado"] = clasificacion

df=df.dropna()
print(df.head())
print(df["degree"].value_counts())
print(f"Salario promedio de la familia: {salarioPromedioFamilia}")

def probabilidades(serie):
    print(f"\nProbabilidades de la serie {serie}:\n")
    a=df[serie].value_counts(normalize=True)
    print(a)
    return a

def probabilidades_conjuntas(serie1,serie2):
    print(f"\nProbabilidades conjuntas de las series {serie1} y {serie2}:\n")
    a=df.groupby([serie1,serie2]).size()/len(df)
    print(a)
    return a

def probabilidad_condicional(causa, efecto):
    # Esto calcula P(Efecto | Causa)
    # Divide el grupo conjunto entre el total de la causa
    resultado = df.groupby(causa)[efecto].value_counts(normalize=True)
    print(f"\nProbabilidad de {efecto} dado {causa}:\n")
    print(resultado)
    return resultado

a=probabilidades("degree")
b=probabilidades("salario_clasificado")
c=probabilidades("sex")
d=probabilidades_conjuntas("degree","salario_clasificado")
e=probabilidades_conjuntas("degree","sex")
f=probabilidades_conjuntas("salario_clasificado","sex")
#g=probabilidad_condicional(["sex","degree"],"salario_clasificado")