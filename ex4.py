# Crie uma função que recebe uma lista de palavras e junta tudo em uma única frase.

def juntar():
    lista = []
    qtd = int(input('Digite quantas palavras você quer adicionar à  lista: '))
    for m in range(qtd):
        palavra = input('Digite as palavras: ')
        lista.append(palavra)
    return ' '.join(lista)
frase = juntar()
print(frase)