# Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos. A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba o troco. Após isso, o programa deve reiniciar para um novo cliente.

while True:
    total = 0
    while True:
        valor = float(input('Digite o valor do produto e 0 para finalizar: '))
        if valor == 0:
            break
        total += valor
    print(f'Total da compra: R${total:.2f}')
    pago = float(input('Digite o valor pago: '))
    troco = pago - total
    print(f'Troco: R${troco:.2f}')
    print('Próximo cliente: ')