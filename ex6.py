# Crie uma função que recebe uma lista de palavras e retorna a palavra com mais letras.

def palavra_mais_longa():
    lista = []
    qtd = int(input('Digite quantas palavras você quer adicionar à  lista: '))
    for m in range(qtd):
        palavra = input('Digite as palavras: ')
        lista.append(palavra)
    return max(lista, key=len)
longa = palavra_mais_longa()
print(longa)