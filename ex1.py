# Crie uma função que recebe duas palavras e retorna True se forem anagramas uma da outra.

def anagrama():
    palavra1 = input('Digite a primeira palavra: ').lower()
    palavra2 = input('Digite a segunda palavra: ').lower()
    if sorted(palavra1) == sorted(palavra2):
        print('As palavras são anagramas')
    else:
        print('As palavras não são anagramas')
anagrama()
