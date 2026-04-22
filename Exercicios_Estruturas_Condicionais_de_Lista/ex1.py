# Leia dois números, faça a soma e apresente caso seja maior que 15.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
if soma > 15:
  print(f"A soma é {soma}, que é maior que 15.")
else:
  print(f"A soma é {soma}, que não é maior que 15.")