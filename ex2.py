# Entre com dois números e exiba a soma e a diferença entre eles.

num1 = float(input('Insira um número: '))
num2 = float(input('Insira o segundo número: '))
operacao = input('soma(+) ou diferença(-)')

if operacao == '+':
  print(num1 + num2)

elif operacao == '-':
  print(num1 - num2)
