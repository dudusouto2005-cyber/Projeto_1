import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Carregar os dados agrícolas
dados = pd.read_csv(
    "AREA_AGRICOLA.csv",
    sep=";",
    encoding="latin1"
)

# Carregar o mapa dos municípios
mapa = gpd.read_file("Sao_Paulo.shp")

# Garantir que os códigos sejam do mesmo tipo
dados["Codigo"] = dados["Codigo"].astype(str)
mapa["Codigo"] = mapa["Codigo"].astype(str)

# Juntar mapa e tabela
gdf = mapa.merge(
    dados,
    on="Codigo",
    how="left"
)

# Escolha a cultura que deseja visualizar
cultura = "Soja (em grão)"

# Criar mapa temático
fig, ax = plt.subplots(figsize=(12, 10))

gdf.plot(
    column=cultura,
    cmap="YlGn",
    legend=True,
    edgecolor="black",
    linewidth=0.1,
    ax=ax
)

ax.set_title(f"Área Plantada de {cultura} em São Paulo")
ax.axis("off")

plt.tight_layout()
plt.show()