def inteiro():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            return num
        except ValueError:
            print("Valor inválido! Por favor, digite um número inteiro.")