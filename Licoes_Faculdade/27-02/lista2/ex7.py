lista = []
qtd = int(input('Digite quantos números você quer adicionar à  lista: '))
def somapares(lista,qtd):
    for n in range(qtd):
        num = int(input('Digite os números: '))
        lista.append(num)
    return sum(num for num in lista if num % 2 == 0)
soma = somapares(lista,qtd)
print(soma) 
somapares(lista,qtd) 