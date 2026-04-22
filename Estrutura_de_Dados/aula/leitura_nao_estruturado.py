import pandas

df_csv = pandas.read_csv('dados_nao_estruturados.csv')

print(df_csv) # se quiser selecionar uma coluna em especifica coloque ['nome da coluna'] exemplo: print(df_csv['nome'])