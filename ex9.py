# Se o valor da compra for maior que R$150,00, aplique um desconto de R$20,00. Caso contrário, não aplique desconto.

compra = float(input('Valor da compra: '))
if compra > 150:
  print(f'Você ganhou um desconto de 20,00! A compra ficou {compra - 20:.2f}')
else:
  print('Valor do desconto não atingido')