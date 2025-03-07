# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for x in range(1,6):
    num = int(input('Digite um número: '))
    soma += num
media = soma / x
print(f"A soma dos valores é {soma} e a média dos valores é: {media}")