#Entre com dois números inteiros e exiba:
# a) A soma
# b) A subtração
# c) A multiplicação
# d) A divisão
# e) O resto da divisão

num1 = float(input('Insira um número: '))
num2 = float(input('Insira o segundo número: '))
operacao = input('Escolha a operação(+, -, *,/, % "resto de divisão"): ')

if operacao == '+':
  print(num1 + num2)

elif operacao == '-':
  print(num1 - num2)

elif operacao == '*':
  print(num1 * num2)

elif operacao == '/':
  print(num1 / num2)
elif operacao == '%':
  print(num1 % num2)


