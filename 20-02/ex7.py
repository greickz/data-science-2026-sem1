# Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar um número até acertar. (Declare um valor e receba outro)

num = 7
tentativas = 0
while True:
    tent = int(input("Adivinhe o número secreto entre 1 e 10: "))
    tentativas += 1
    if tent < 1 or tent > 10:
        print("Digite um número entre 1 e 10:")
        continue
    if tent == num:
        print(f"Você acertou o número secreto em {tentativas} tentativas")
        break
    else:
        print("Tente novamente!")