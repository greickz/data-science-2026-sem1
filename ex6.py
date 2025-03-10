# Peça a senha do Wi-Fi ao usuário. Se for senha123, exiba Conectado, caso contrário, exiba Senha incorreta.

senhacorreta = 'senha123'
senha = input('Digite a senha: ')
if senhacorreta == senha:
  print('Conectado')
else:
  print('Senha incorreta')