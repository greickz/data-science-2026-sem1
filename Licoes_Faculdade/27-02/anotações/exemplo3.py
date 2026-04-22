#Função numero par ou impar
numero = int(input('Digite um número: '))
def par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
print(par_impar(numero))