# Somar números até o usuário digitar 0. Peça números ao usuário e some-os até que ele digite 0.

soma = 0
while True:
    num = int(input("Digite um número e 0 para sair: "))
    if num == 0:
        break
    soma += num
print(f"A soma dos números é: {soma}")