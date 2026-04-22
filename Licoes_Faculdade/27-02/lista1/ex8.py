lista = []
qtd = int(input('Digite quantas notas você quer adicionar à  lista: '))
def m(lista,qtd):
    for item in range(qtd):
        nota = int(input('Digite uma nota para adicionar à lista: '))
        lista.append(nota)
    soma = sum(lista)
    media = soma / len(lista)
    print(media)
m(lista,qtd)