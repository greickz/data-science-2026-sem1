# Some todos os números pares de 1 a 100 e mostre o resultado.

num = 1
soma = 0
while num <= 100:
    if num % 2 == 0:
        soma += num
    num += 1
print(f"A soma dos números pares de 1 a 100 é: {soma}")