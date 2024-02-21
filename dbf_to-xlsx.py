import pandas as pd
from dbfread import DBF

# Caminho para o arquivo DBF
caminho_dbf = '/var/www/html/version2/files/teste/teste.dbf'

# Ler o arquivo DBF usando pandas
table = DBF(caminho_dbf, encoding='utf-8')
df = pd.DataFrame(iter(table))

# Caminho para salvar o arquivo XLSX
caminho_xlsx = '/var/www/html/version2/files/resultados/result.xlsx'

# Salvar o DataFrame como XLSX usando pandas
df.to_excel(caminho_xlsx, index=False, engine='openpyxl')
