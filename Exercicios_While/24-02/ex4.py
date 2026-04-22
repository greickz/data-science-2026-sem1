# Escreva um programa que leia um número inteiro positivo e determine se ele é um número perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele mesmo) é igual ao próprio número.

num = int(input("Digite um número inteiro positivo: "))
if num <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    soma = 0
    divisor = 1
    while divisor < num:
        if num % divisor == 0:
            soma += divisor
        divisor += 1
    if soma == num:
        print(f"{num} é um número perfeito.")
    else:
        print(f"{num}  é um número imperfeito.")