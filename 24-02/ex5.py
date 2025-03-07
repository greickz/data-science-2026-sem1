# Escreva um programa que leia um número inteiro positivo e determine se ele é um quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).

num = int(input("Digite um número inteiro positivo: "))
x = 0
while x * x <= num:
    if  x * x == num:
        print(f'{num} é um quadrado perfeito.')
        break
    x +=1
else:
    print(f'{num} é um quadrado imperfeito.')