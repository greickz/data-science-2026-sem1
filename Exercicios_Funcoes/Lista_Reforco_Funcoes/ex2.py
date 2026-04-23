# Crie uma função que recebe uma lista de números e retorna a quantidade de números positivos.

def positivos():
    lista = []
    qtd = int(input('Digite quantos números você quer adicionar à  lista: '))
    for n in range(qtd):
        num = int(input('Digite os números: '))
        lista.append(num)
    npositivos = 0
    for numero in lista:
        if numero > 0:
            npositivos += 1
    print(f'Existem  {npositivos} números positivos.')
positivos()