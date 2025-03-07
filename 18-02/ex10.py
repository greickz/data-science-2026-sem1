# Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
#valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

faturamentob = 54000
faturamentoatotal = 0  
for x in range(5):
    cadastro = input(f'Digite o nome do cliente {x + 1}: ')
    faturamentoa = float(input(f'Digite o faturamento do cliente {cadastro}: '))
    faturamentoatotal += faturamentoa
if faturamentoatotal > faturamentob:
    diferenca = faturamentoatotal - faturamentob
    print(f'O faturamento da loja A foi superior ao da loja B em R$ {diferenca:.2f}.')
else:
    print('O faturamento da loja B não foi ultrapassado.')