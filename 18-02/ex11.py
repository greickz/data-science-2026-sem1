# Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
#  e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
soma = 0
n = int(input('Digite o número de pessoas: '))  
for x in range(n):
    idade = int(input(f'Digite a idade da pessoa {x+1}: '))
    soma += idade
media = soma / n 
if 0 <= media <= 25:
    print('A turma é jovem.')
elif 26 <= media <= 60:
    print('A turma é adulta.')
else:
    print('A turma é idosa.')