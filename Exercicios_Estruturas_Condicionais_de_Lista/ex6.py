# Escreva um programa que verifique a validade de uma senha fornecida pelo
# usuário. A senha válida é o número 1234. Devem ser impressas as seguintes
# mensagens:
# ACESSO PERMITIDO caso a senha seja válida.
# ACESSO NEGADO caso a senha seja inválida.

senha = input('Digite a senha: ')
senhacorreta = '1234'
if senha == senhacorreta:
  print('ACESSO PERMITIDO')
elif  senha != senhacorreta:
  print('ACESSO NEGADO')