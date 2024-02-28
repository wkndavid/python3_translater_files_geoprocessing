import codecs as cd 

file = cd.open("teste.txt", encoding='utf-8')

data = file.read()
data = data.upper()

print(data)