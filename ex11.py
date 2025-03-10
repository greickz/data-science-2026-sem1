# Crie uma lista com 6 itens e verifique se existe uma palavra dentro dela, utilizando o operador in. Depois, verifique uma palavra que não existe dentro dela utilizando o operador not in.

lista = ["Palmeiras", "Atletico mg", "Vasco", "Sport", "Juventus", "Paysandu"]
palavra1 = "Palmeiras"
if palavra1 in lista:
    print(f'A palavra "{palavra1}" está na lista.')
else:
    print(f'A palavra "{palavra1}" NÃO está na lista.')
palavra2 = "Flamengo"
if palavra2 not in lista:
    print(f'A palavra "{palavra2}" NÃO está na lista.')
else:
    print(f'A palavra "{palavra2}" está na lista.')