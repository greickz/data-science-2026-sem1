# Entre com dois números e exiba as comparações:
# a) Se o primeiro número é maior que o segundo
# b) Se os dois números são iguais
# c) Se o primeiro número é menor ou igual ao segundo

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(f" {num1} é maior que {num2}.")
else:
    print(f" {num1} NÃO é maior que {num2}.")
if num1 == num2:
    print(f" Os números são iguais: {num1}.")
else:
    print(f" Os números NÃO são iguais: {num1} e {num2}.")
if num1 <= num2:
    print(f" {num1} é menor ou igual a {num2}.")
else:
    print(f" {num1} NÃO é menor ou igual a {num2}.")