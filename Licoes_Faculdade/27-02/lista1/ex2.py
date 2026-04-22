num = int(input('Digite um numero: '))
def par_impar(num):
    if num % 2 == 0:
        return f'O número {num} é Par'
    else:
        return f'O número {num} é Ímpar'
print(par_impar(num))