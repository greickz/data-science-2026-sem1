# Se a pessoa tiver um convite válido, exiba Entrada permitida, caso contrário, exiba Entrada negada.

convite = input('Digite o código do convite: ')
convitecorreto = 'certo'
if convite == convitecorreto:
  print('Entrada permitida')
else:
  print('Entrada negada')