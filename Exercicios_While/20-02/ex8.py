# Encontrando o maior número inserido pelo usuário. Peça números ao usuário e, ao digitar 0, exiba o maior número inserido.

maior = None
while True:
    num = int(input("Digite um número ou 0 para sair: "))
    if num == 0:
        break
    if maior is None or num > maior:
        maior = num
if maior is not None:
    print(f"O maior número inserido foi: {maior}")
else:
    print("Nenhum número foi inserido.")