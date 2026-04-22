# Escreva um programa que leia um número inteiro e conte quantos dígitos ele tem.

numero = int(input("Digite um número inteiro: "))
contador = 0
numero = abs(numero)# converte o número para positivo
while numero > 0:
    numero = numero // 10
    contador += 1
print(f"O número tem {contador} dígitos.")