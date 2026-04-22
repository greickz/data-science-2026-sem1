# Escreva um programa que leia um número N e imprima todos os termos da sequência de Fibonacci até que o maior termo seja menor ou igual a N.

num = int(input('Digite um número: '))
a,b = 0,1
fibonacci = []
while a <= num:
    fibonacci.append(a)
    a, b = b, a + b
print( f'A sequencia do {num} é: {fibonacci}')   