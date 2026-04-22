# Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.

for x in range(1,11):
  print('----------------------------')
  for y in range(1,11):
    print(f'{x} X {y} = {x * y}')