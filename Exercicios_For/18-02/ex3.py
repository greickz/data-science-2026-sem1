# Faça um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando divididos por 11 produzam resto igual a 2.

num1 = 1000
num2 = 2000
for x in range(num1, num2 + 1):
    if x % 11 == 2:
        print(x)