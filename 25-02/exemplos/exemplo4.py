programadores = ['Victor','Julia','Henrique','Caio','Luana','Vini','matheus','Jessica']

tamanhomenor = min(programadores, key=len)
tamanhomaior = max(programadores, key=len)

maior = []
menor = []
for nome in programadores:
    if len(nome) == len(tamanhomenor):
        menor.append(nome)
    elif len(nome) == len(tamanhomaior):
        maior.append(nome)
        
print(menor)
print(maior)