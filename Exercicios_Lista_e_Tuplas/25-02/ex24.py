lista1 = []
lista2 = []
vezes1 = int(input('Digite quantos itens você quer adicionar à primeira lista: '))
for item in range(vezes1):
    ad1 = int(input('Digite um número para adicionar à primeira lista: '))
    lista1.append(ad1)
vezes2 = int(input('Digite quantos itens você quer adicionar à segunda lista: '))
for item2 in range(vezes2):
    ad2 = int(input('Digite um número para adicionar à segunda lista: '))
    lista2.append(ad2)
if lista1 == lista2:
    print('As listas são iguais')
else:
    print('As listas não são iguais')