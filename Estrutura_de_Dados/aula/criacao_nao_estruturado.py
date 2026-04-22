# DADOS NÃO ESTRUTURADOS - CRIAÇÃO
# CSV

import pandas

dados_csv = {
    'nome':['Vinicius', 'Jonas','Gabriel','Marcio', 'Monica'],
    'idade':[17, 13, 24, 54, 49],
    'cidade':['Sao Paulo','Sao Paulo','Sao Paulo','Belo Horizonte','Cuiaba']
    
}

data_frame_csv = pandas.DataFrame(dados_csv)

# SALVAR EM CSV

data_frame_csv.to_csv('dados_nao_estruturados.csv', index = False)