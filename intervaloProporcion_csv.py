import pandas as pd
from pathlib import Path


ruta_base=Path(__file__).parent
datos=ruta_base/"datos"


df=pd.read_csv(datos/"SPRINT.CSV")

#print(df.head())

manipular=df["Status"]
L=manipular.value_counts()
print(L)