# Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.

anterior = None
c = 0
while True:
    num = float(input('Digite um número: '))
    c += 1
    if num == anterior:
        break
    anterior = num
print(f'Total de números inseridos: {c}')