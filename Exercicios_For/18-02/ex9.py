# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input('Digite um número: '))
if num > 1:
    for x in range(2, num):
        if num % x == 0:
            print(f'{num} não é primo')
            break # serve para quebrar loopings
    else:
        print(f'{num} é primo')
