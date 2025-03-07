# Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o usuário digite -1. Em seguida, exiba a média das notas.
soma = 0
c = 0
nota = float(input('Digite uma nota e -1 para sair: '))
while nota != -1:
    soma += nota
    c += 1
    nota = float(input('Digite uma nota e -1 para sair: '))
if c > 0:
    media = soma / c
    print(f'Média das notas: {media}')
else:
    print('Nenhuma nota foi inserida.')