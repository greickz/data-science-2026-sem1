# Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.

num = int(input('Digite um número: '))
if num > 0 :
    print(f'O número {num} é Positivo')
elif num == 0:
    print(f'O número {num} é Neutro')
else:
    print(f'O número {num} é Negativo')