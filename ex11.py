# Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. 
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o salário: '))
if salario <= 280:
    print(f'O aumento salarial é de 20%, o seu salário final ficou {salario * (20/100)}')
elif salario >= 280 and salario <=700:
    print(f'O aumento salarial é de 15%, o seu salário final ficou {salario * (15/100)}')
elif salario >= 700 and salario <=1500:
    print(f'O aumento salarial é de 10%, o seu salário final ficou {salario * (10/100)}')
elif salario >= 1500:
    print(f'O aumento salarial é de 5%, o seu salário final ficou {salario * (5/100)}')