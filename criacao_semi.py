# DADOS SEMI ESTRUTURADOS - CRIAÇÃO
#JSON

import pandas

dados_json = {
    'nome':['Vinicius', 'Jonas','Gabriel','Marcio', 'Monica'],
    'idade':[17, 13, 24, 54, 49],
    'cidade':['Sao Paulo','Sao Paulo','Sao Paulo','Belo Horizonte','Cuiaba']
    
}

data_frame_json= pandas.DataFrame(dados_json)

#SALVAR EM JSON

data_frame_json.to_json('dadosSemi.json', orient='records', lines=False) # os records são registros
