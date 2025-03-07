# Solicite ao usuário que insira números. O programa deve continuar até que um número negativo seja inserido. No final, exiba o maior número informado.

senhacorreta = 1234
senha = int(input('Digite a senha: '))
while senha != senhacorreta:
    tente = int(input('Senha incorreta, tente novamente: '))
    if senha or tente == senhacorreta:
        print('Acesso permitido')
        break


