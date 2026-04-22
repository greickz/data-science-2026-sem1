lista = []
qtd = int(input('Digite quantas palavras você quer adicionar à lista: '))
def juntar(lista, qtd, separador=' '):
    for m in range(qtd):
        palavra = input('Digite as palavras: ')
        lista.append(palavra)
    return separador.join(lista)
juntado = juntar(lista, qtd, ' ')
print(juntado)