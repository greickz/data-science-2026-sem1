# O usuário deve digitar a senha correta (1234). Enquanto errar, o programa deve pedir novamente.

senhacorreta = "1234"
while True:
    senha = input("Digite a senha: ")
    if senha == senhacorreta:
        print("Senha correta, acesso permitido.")
        break
    else:
        print("Senha incorreta, tente novamente.")