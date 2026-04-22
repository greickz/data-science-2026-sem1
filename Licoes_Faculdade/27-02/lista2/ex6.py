lista = []
qtd = int(input('Digite quantas palavras você quer adicionar à  lista: '))
def palavra_mais_longa(lista,qtd):
    for m in range(qtd):
        palavra = input('Digite as palavras: ')
        lista.append(palavra)
    return max(lista, key=len)
longa = palavra_mais_longa(lista,qtd)
print(longa)