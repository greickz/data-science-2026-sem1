lista = []
qtd = int(input('Digite quantas palavras você quer adicionar à  lista: '))
def juntar(lista,qtd):
    for m in range(qtd):
        palavra = input('Digite as palavras: ')
        lista.append(palavra)
    return ' '.join(lista)
frase = juntar(lista,qtd)
print(frase)