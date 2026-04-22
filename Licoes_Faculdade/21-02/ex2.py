# Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha correta definida previamente.

senhacorreta = '00000'
senha = input('Digite a senha: ')
while senha != senhacorreta:
    senha = input('Senha incorreta, tente novamente: ')
print('Senha correta')