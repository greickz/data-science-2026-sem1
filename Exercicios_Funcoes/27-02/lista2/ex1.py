palavra1 = input('Digite a primeira palavra: ').lower()
palavra2 = input('Digite a segunda palavra: ').lower()

def anagrama(palavra1,palavra2):
    if sorted(palavra1) == sorted(palavra2):
        print('As palavras são anagramas')
    else:
        print('As palavras não são anagramas')
anagrama(palavra1,palavra2)