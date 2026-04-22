num = int(input('Digite um número: '))
original= num
inverso = 0
def palindromo(num,original,inverso):
    while num > 0:
        digito = num % 10
        inverso = inverso * 10 + digito
        num = num // 10
    if original == inverso:
        return(f'O número {original} é um palíndromo') 
    else:
        return(f'O número {original} não é um palíndromo.')
print(palindromo(num,original,inverso))