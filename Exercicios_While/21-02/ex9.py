# Implemente um sistema onde o usuário insere o código e a quantidade dos produtos desejados. O programa deve calcular o valor total e permitir que o usuário finalize o pedido digitando 0.

total = 0
while True:
    codigo = int(input('Digite o código do produto e 0 para finalizar: '))
    if codigo == 0:
        break
    quantidade = int(input('Digite a quantidade: '))
    total += quantidade * 10
print(f'Total do pedido: R${total:.2f}')