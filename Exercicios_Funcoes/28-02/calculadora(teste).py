
print('Bem vindo a calculadora, digite os sinais remetente a cada operação: \n Adição = + \n Subtração = - \n Multiplicação = * \n Divisão - /')
op = input('Digite o Operador de acordo com a tabela: ')
qtd = int(input('Digite quantos números haveram na equação: '))
numeros = []

if op == '+' or 'soma' or 'Soma' or 'SOMA':
    for n in range(qtd):
        num = int(input('Digite o número: '))
        numeros.append(num)
    soma = sum(numeros)
    print(f'O resultado da soma dos numeros {numeros} ficou {soma}')
        
outro = input('Deseja realizar outra operação? s/n ')
if outro == 's':
    print('Bem vindo a calculadora, digite os sinais remetente a cada operação: \n Adição = + \n Subtração = - \n Multiplicação = * \n Divisão - /')
    op2 = input('Digite o Operador da nova operação de acordo com a tabela: ')

