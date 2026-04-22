# Crie uma função que receba duas listas de números inteiros e retorne uma nova lista contendo os elementos que aparecem em ambas as listas (interseção).

def intersecao_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))
lista1 = [1,6,32,17,9,24,2]
lista2 = [2,49,17,8,32,9]
intersecao= intersecao_listas(lista1, lista2)
print(intersecao)
