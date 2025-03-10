# Peça ao usuário para digitar M para manhã ou qualquer outra tecla para tarde. Se for M, exiba Bom dia!, senão exiba Boa tarde!.

turno= input('Digite "M" para manhã e qualquer outra para outro turno: ').upper().strip()
if turno == "M":
  print('Bom dia!')
else:
  print('boa tarde!')