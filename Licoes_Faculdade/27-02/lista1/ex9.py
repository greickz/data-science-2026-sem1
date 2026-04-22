frase = input('Digite uma frase ou palavra: ')
contador = 0
vogais = 'aeiouAEUIOU'
def contar(frase,contador):
    for letra in frase:
        if letra in vogais:
            contador += 1
    print(f'A frase tem {contador} vogais.')
contar(frase,contador)