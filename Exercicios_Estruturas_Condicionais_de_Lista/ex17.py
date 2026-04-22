# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input('Digite o preço do primeiro produto: '))
preco2 = float(input('Digite o preço do segundo produto: '))
preco3 = float(input('Digite o preço do terceiro produto: '))
match (preco1 < preco2, preco1 < preco3, preco2 < preco1, preco2 < preco3, preco3 < preco1, preco3 < preco2):
    case (True, True, _, _, _, _):
        print(f'O melhor a se comprar é o que custa {preco1}')
    case (_, _, True, True, _, _):
        print(f'O melhor a se comprar é o que custa {preco2}')
    case (_, _, _, _, True, True):
        print(f'O melhor a se comprar é o que custa {preco3}')
    case _:
        print('Há produtos com preços iguais ou não foi possível determinar o menor preço.')