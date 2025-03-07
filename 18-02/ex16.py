# Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:
# Até 15 anos
# De 16 a 30 anos
# De 31 a 45 anos
# De 46 a 60 anos
# Acima de 61 anos

faixa1 = 0  
faixa2 = 0  
faixa3 = 0  
faixa4 = 0  
faixa5 = 0  
for x in range(15):
    idade = int(input('Digite sua idade: '))
    if idade <= 15:
        faixa1 += 1
    elif 16 <= idade <= 30:
        faixa2 += 1
    elif 31 <= idade <= 45:
        faixa3 += 1
    elif 46 <= idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1
totalpessoas = faixa1 + faixa2 + faixa3 + faixa4 + faixa5
percentualprimeiro = (faixa1 / totalpessoas) * 100
percentualultimo = (faixa5 / totalpessoas) * 100
print("Quantidade de pessoas em cada faixa etária:")
print(f"Até 15 anos: {faixa1} pessoas")
print(f"De 16 a 30 anos: {faixa2} pessoas")
print('----------------------------------------')
print(f"De 31 a 45 anos: {faixa3} pessoas")
print('----------------------------------------')
print(f"De 46 a 60 anos: {faixa4} pessoas")
print('----------------------------------------')
print(f"Acima de 61 anos: {faixa5} pessoas")
print('----------------------------------------')
print("Percentagem de pessoas na primeira e na última faixa etária:")
print(f"Até 15 anos: {percentualprimeiro:.2f}%")
print(f"Acima de 61 anos: {percentualultimo:.2f}%")