# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = input('Digite um número para identificar o dia da semana: ')
match dia:
    case '1':
        print("Domingo")
    case '2':
        print("Segunda-feira")
    case '3':
        print("Terça-feira")
    case '4':
        print("Quarta-feira")
    case '5':
        print("Quinta-feira")
    case '6':
        print("sexta-feira")
    case '7':
        print("Sabádo")
    case _:
        print("Inválido")