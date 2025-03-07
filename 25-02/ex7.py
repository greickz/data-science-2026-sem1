lista = ['Vinícius','Ana','Cauã','Bianca','Henrique']
d = input('Digite o nome deseja verifica: ')
for nome in lista:
    if nome == d:
        print(nome)
else:
    print('O nome não esta na lista')