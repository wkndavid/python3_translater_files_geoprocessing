import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

# Caminho para o arquivo Excel (.xls) local
caminho_excel = '/home/david/autom/setor-teste-dictionary.xlsx'

# Ler dados do Excel para um DataFrame do pandas
dados_excel = pd.read_excel(caminho_excel)

print(dados_excel)

# Adicionar uma geometria de ponto fictícia
geometry = [Point(0, 0) for _ in range(len(dados_excel))]
gdf = gpd.GeoDataFrame(dados_excel, geometry=geometry, crs='EPSG:4326')

# Caminho para salvar o shapefile localmente (com a extensão .shp)
caminho_shapefile = '/home/david/autom/1arquivo_shapefile.shp'

# Salvar o GeoDataFrame como shapefile usando o GeoPandas
gdf.to_file(caminho_shapefile, driver='ESRI Shapefile')
