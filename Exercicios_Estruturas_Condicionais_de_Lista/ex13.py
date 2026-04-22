# Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, 
# apartir da resposta do usuário, faça a devida conversão.

temp = float(input('Digite a temperatura para ser convertida: '))
temperatura = input('Digite C para converter Celsius para Fahrenheit, e F para converter Fahrenheit para Celsius: ').lower().strip()
if temperatura == 'c':
    print(f'Convertendo Celsius para Fahrenheit, a temperatura ficou {temp * 1.8 + 32} ºF')
elif temperatura == 'f':
    print(f'Convertendo Fahrenheit para Celsius, a temperatura ficou {(temp - 32) * 5/9} ºC')
else:
    print('Opção inválida. Digite C ou F.')