# Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B com 200.000 habitantes e taxa de 1,5%. Determine quantos anos serão necessários para que a população do país A ultrapasse a população do país B.

populacaoa = 80000
populacaob = 200000
anos = 0
while populacaoa <= populacaob:
    populacaoa *= 1.03
    populacaob *= 1.015
    anos += 1
print(f'Serão necessários {anos} anos para a população de A ultrapassar a de B.')