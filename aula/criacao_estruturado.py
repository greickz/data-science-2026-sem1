# DADOS ESTRUTURADOS - CRIAÇÃO
# EXCEL
# Comandos para conseguir fazer a planilha: 
# pip install pandas
# pip install openpyxl

import pandas 

# ESTRUTTURA DE DICIONARIO
dados_planilha1 = {
    'nome':['Vinícius', 'Jonas','Gabriel','Marcio', 'Monica'],
    'idade':[17, 13, 24, 54, 49],
    'cidade':['São Paulo','São Paulo','São Paulo','Belo Horizonte','Cuiaba']
    
}

# CRIAR UM DATAFRAME (LINHAS E COLUNAS)

dataframe_palnilha1 = pandas.DataFrame(dados_planilha1)

# SALVAR NO EXCEL

with pandas.ExcelWriter('dados_estruturados.xlsx') as writer:  #mandar para o excel, o ass é para simplificar na hora de chamr o caminho
    dataframe_palnilha1.to_excel(writer, sheet_name='Palnilha1', index= False) # criar um arquivo para o excel com os parametros, sheet_name é o nome da aba dentro do excel, index é para 

# o arquivo ~$dados_estruturados.xlsx é pq esta aberto no excel, quando fechar o excel ele fecha também 