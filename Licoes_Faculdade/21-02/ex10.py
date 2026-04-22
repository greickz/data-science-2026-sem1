# Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo(5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de votos nulos e brancos. A entrada 0 encerra a votação.

votos = [0, 0, 0, 0, 0, 0]
while True:
    voto = int(input('Digite o número do candidato (1-4), 5 para nulo, 6 para branco, ou 0 para encerrar: '))
    if voto == 0:
        break
    if 1 <= voto <= 6:
        votos[voto-1] += 1
    else:
        print('Voto inválido, tente novamente.')
totalvotos = sum(votos)
print('Resultado da votação:')
for i in range(4):
    print(f'Candidato {i+1}: {votos[i]} votos')
print(f'Votos nulos: {votos[4]}')
print(f'Votos em branco: {votos[5]}')
print(f'Porcentagem de votos nulos: {(votos[4]/totalvotos)*100:.2f}%')
print(f'Porcentagem de votos em branco: {(votos[5]/totalvotos)*100:.2f}%')

