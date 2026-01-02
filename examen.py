import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image, display 

# Cargar el dataset
# ruta = "C:\\Users\\rcolr.BTS\\Documents\\CASA_INFORMATICA\\data\\living.csv"
df = pd.read_csv('living.csv', encoding='latin1')
# print(df.head())
# print(df.info())
# print(df.describe())
# nuevo = pd.DataFrame(df)
# print(nuevo)


print("\nNro. de Filas:", df.shape[0])
print("Nro. de Columnas:", df.shape[1])

costos = df["Cost of living, 2017"].to_numpy()

costo_promedio = np.mean(costos)
costo_max = np.max(costos)
costo_min = np.min(costos)

print("Costo de vida promedio:", costo_promedio)

idx_max = np.argmax(costos)
print("País con costo de vida más alto:", df.loc[idx_max, "Countries"])
print("Costo de vida más alto:", costo_max)


idx_min = np.argmin(costos)
print("País con costo de vida más bajo:", df.loc[idx_min, "Countries"])
print("Costo de vida más bajo:", costo_min)


peru = df[df["Countries"] == "Peru"]

print("Costo de Vida en Perú:", peru["Cost of living, 2017"].to_numpy()[0])
print("Ranking de Perú:", peru["Global rank"].to_numpy()[0])

#  EJERCICIO 2
# Los 10 países con el costo de vida más alto
top_10_alto = df.sort_values(
    by="Cost of living, 2017",
    ascending=False
).head(10)

y_pos = np.arange(len(top_10_alto))

plt.figure(figsize=(10, 6))
plt.barh(y_pos, top_10_alto["Cost of living, 2017"].to_numpy())
plt.yticks(y_pos, top_10_alto["Countries"])
plt.xlabel("Costo de vida (2017)")
plt.ylabel("País")
plt.title("Los 10 países con el costo de vida más alto")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_10_costo_mas_alto.png", dpi=300)
plt.close()

display(Image(filename="top_10_costo_mas_alto.png"))

#Los 10 países con el costo de vida más bajo

top_10_bajo = df.sort_values(
    by="Cost of living, 2017",
    ascending=True
).head(10)

y_pos = np.arange(len(top_10_bajo))

plt.figure(figsize=(10, 6))
plt.barh(y_pos, top_10_bajo["Cost of living, 2017"].to_numpy())
plt.yticks(y_pos, top_10_bajo["Countries"])
plt.xlabel("Costo de vida (2017)")
plt.ylabel("País")
plt.title("Los 10 países con el costo de vida más bajo")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_10_costo_mas_bajo.png", dpi=300)
plt.close()

display(Image(filename="top_10_costo_mas_bajo.png"))

# El costo de vida de los países de América

america = df[df["Continent"] == "America"]

x_pos = np.arange(len(america))

plt.figure(figsize=(12, 6))
plt.bar(x_pos, america["Cost of living, 2017"].to_numpy())
plt.xticks(x_pos, america["Countries"], rotation=90)
plt.xlabel("País")
plt.ylabel("Costo de vida (2017)")
plt.title("El costo de vida de los países de América")
plt.tight_layout()
plt.savefig("costo_vida_america.png", dpi=300)
plt.close()

display(Image(filename="costo_vida_america.png"))