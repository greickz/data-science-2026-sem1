#Uma loja tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500. A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%.

valor = float(input('Digite o valor da compra: '))
base = 500.00
descontomax = 25
desconto = 0
if valor > base:
    diferenca = valor - base
    intervalododesconto = int(diferenca // 100)
    for x in range(intervalododesconto):
        if desconto < descontomax:
            desconto += 1
valorcmdesconto = valor * (1 - desconto / 100)
print(f'Valor da compra: R${valor:.2f}')
print(f'Desconto aplicado: {desconto}%')
print('----------------------------------------')
print(f'Valor final: R${valorcmdesconto:.2f}')