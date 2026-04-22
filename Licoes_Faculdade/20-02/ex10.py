# Apenas aceitar números positivos. O programa deve continuar pedindo um número até o usuário digitar um número positivo.

while True:
    num = float(input("Digite um número positivo: "))
    if num > 0:
        break
    else:
        print("Número inválido, digite um número positivo.")
print(f"Você digitou o número positivo: {num}")