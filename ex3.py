# Crie uma função que recebe uma lista de números e retorna a quantidade de números que são múltiplos de 3.


lista = []
qtd = int(input('Digite quantos números você quer adicionar à lista: '))
def juntar(lista, qtd, separador=' '):
    for m in range(qtd):
        palavra = input('Digite os números: ')
        lista.append(palavra)
    return separador.join(lista)
juntado = juntar(lista, qtd, ' ')
print(juntado)