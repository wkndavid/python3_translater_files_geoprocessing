import geopandas as gpd

# Caminho para o shapefile (.shp) local
caminho_shapefile = '/home/david/autom/setor/setor.shp'

# Ler o shapefile para um GeoDataFrame ajustando a codificação
try:
    gdf = gpd.read_file(caminho_shapefile, encoding='utf-8')
except UnicodeDecodeError:
    try:
        gdf = gpd.read_file(caminho_shapefile, encoding='utf-16')
    except UnicodeDecodeError:
        gdf = gpd.read_file(caminho_shapefile, encoding='latin-1')

# Caminho para salvar o arquivo Excel localmente (com a extensão .xlsx)
caminho_excel = '/home/david/autom/setor/teste.xlsx'

# Salvar o GeoDataFrame como um arquivo Excel usando o GeoPandas
gdf.to_excel(caminho_excel, index=False, encoding='utf-8')
