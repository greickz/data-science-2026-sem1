# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 0
candidato2 = 0
candidato3 = 0
totaleleitores = int(input('Digite o número total de eleitores: '))
for x in range(totaleleitores):
    print(f'Eleitor {x + 1}:')
    candidato = int(input('Digite o número do candidato (11, 22 ou 33): '))
    if candidato == 11:
        candidato1 += 1
    elif candidato == 22:
        candidato2 += 1
    elif candidato == 33:
        candidato3 += 1
print('Resultado da eleição:')
print(f'Candidato 11: {candidato1} votos')
print('----------------------------------------')
print(f'Candidato 22: {candidato2} votos')
print('----------------------------------------')
print(f'Candidato 33: {candidato3} votos')
print('----------------------------------------')
if candidato1 > candidato2 and candidato1 > candidato3:
    print('O Candidato 1 venceu')
elif candidato2 > candidato1 and candidato2 > candidato3:
    print('O Candidato 2 venceu')
elif candidato3 > candidato1 and candidato3 > candidato2:
    print('O Candidato 3 venceu')
else:
    print('empatou')
