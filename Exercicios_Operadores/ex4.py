# Entre com um número ao usuário e exiba se ele é par ou ímpar usando o operador de módulo %.

num1 = float(input('Insira um número: '))
if num1 % 2 == 0:
    print(f"O número {num1} é par.")
else:
    print(f"O número {num1} é ímpar.")