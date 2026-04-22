# Conjunto - Estruturas de Dados

frutas = {"maçã", "banana","uva"}
print(frutas)
print("-" * 30) 

# Adiciona um item
frutas.add("morango") # Diferente do append ele não adiciona na última posição
print(frutas)
print("-" * 30) 

#remove um item
frutas.remove("banana")
print(frutas)
print("-" * 30) 

# Verfica se esta noconjunto
print("maçã" in frutas)
print("abacate" in frutas)
print("-" * 30) 

#Interando sobre o conjunto
for fruta in frutas:
    print(fruta)
print("-" * 30) 



#Operações entre conjuntos 

# Definir 2 conjuntos

conjunto_A = {1,2,3,4}
conjunto_B = {2,4,6,8}

# União: Todos os elementos de ambos conjuntos

uniao = conjunto_A | conjunto_B
print(uniao)
print("-" * 30) 


# Intersecção: Trazer elementos comuns aos conjuntos
interseccao = conjunto_A  & conjunto_B
print(interseccao)
print("-" * 30) 

# Difereça: Trazer os elementos que estão no conjunto A, mas não estão no conjunto B
diferenca = conjunto_A - conjunto_B
print(diferenca)
print("-" * 30) 

# Diferença simétrica: elementos que estçao em um ou em outro, mas não em ambos
diferenca_simetrica = conjunto_A ^ conjunto_B
print(diferenca_simetrica)