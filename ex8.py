# Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.

time1 = int(input('Digite a quantidade de gols que o primeiro time marcou: '))
time2 = int(input('Digite a quantidade de gols que o segundoo time marcou: '))
if time1 == time2:
  print(f'O jogo terminou empatado em {time1} X {time2}')
elif time1 > time2:
  print(f'O primeiro time ganhou o jogo de {time1} X {time2}')
else:
  print(f'O segundo2 time ganhou o jogo de {time2} X {time1}')