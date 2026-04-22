import pandas

df_excel = pandas.read_excel('dados_estruturados.xlsx', sheet_name=['Palnilha1'])

print(df_excel)