lista = [2,1,3,4,5]
numero = int(input('Digite um numero:')) 
for num in lista:
    if num == numero:
        print(f'O número {numero} está na lista')
        break
else:
     print(f'O número {numero} não está na lista')