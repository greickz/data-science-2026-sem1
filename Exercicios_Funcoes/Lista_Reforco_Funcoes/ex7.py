# Crie uma função que recebe uma lista de números e retorna a soma apenas dos números pares.


def somapares():
    lista = []
    qtd = int(input('Digite quantos números você quer adicionar à  lista: '))
    for n in range(qtd):
        num = int(input('Digite os números: '))
        lista.append(num)
    return sum(num for num in lista if num % 2 == 0)
soma = somapares()
print(soma) 
somapares() 