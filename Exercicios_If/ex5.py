# Peça o valor da conta. Se for maior que R$100,00, adicione uma gorjeta de 10% e exiba o total a pagar. Caso contrário, adicione uma gorjeta de 5%.

conta = float(input('Digite o valor da conta: '))
if conta > 100:
  print(f'Gorjeta adicionade de {conta * (10 / 100)}')
else:
  print(f'Gorjeta adicionade de {conta * (5 / 100)}')