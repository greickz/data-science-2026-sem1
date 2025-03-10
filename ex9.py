# Entre com duas idades. Com base nessas informações, verifique se ambos tem mais de 18.

idade1 = int(input('Insira uma idade: '))
idade2 = int(input('Insira a segunda idade: '))

if idade1 > 18 and idade2 > 18:
  print('As duas idades são maiores do que 18.')
elif idade1 < 18 and idade2 > 18:
  print('Apenas uma das idades é maior do que 18.')
elif idade1 > 18 and idade2 < 18:
  print('Apenas uma das idades é maior do que 18.')
else:
  print('Nenhuma das idades é maior do que 18.')