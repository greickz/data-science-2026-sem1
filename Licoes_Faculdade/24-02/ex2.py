# Escreva um programa que leia um número inteiro positivo e determine se ele é um palíndromo (ou seja, se lido de trás para frente continua igual).

num = int(input('Digite um número: '))
original= num
inverso = 0
while num > 0:
    digito = num % 10
    inverso = inverso * 10 + digito
    num = num // 10
if original == inverso:
    print(f'O número {original} é um palíndromo') 
else:
    print(f'O número {original} não é um palíndromo.')
    