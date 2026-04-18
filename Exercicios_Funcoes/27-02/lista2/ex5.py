lista = []
qtd = int(input('Digite quantos números você quer adicionar à  lista: '))
def substituir(numeros,qtd):
    for x in range(qtd):
        num = int(input('Digite os números: '))
        lista.append(num)
    return [max(0, num) for num in numeros]
resultado = substituir(lista,qtd)
print(resultado)
