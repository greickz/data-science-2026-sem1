# Contar quantos números pares o usuário digitar. O programa deve contar quantos números pares o usuário inseriu. O usuário para digitando -1.

par = 0
while True:
    num = int(input("Digite um número ou -1 para sair: "))
    if num == -1:
        break
    if num % 2 == 0:
        par += 1
print(f"Você digitou {par} número(s) par(es).")