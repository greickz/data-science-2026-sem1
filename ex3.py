# Entre com dois números, calcule e exiba o produto e o quociente (divisão real e inteira).

num1 = float(input('Insira um número: '))
num2 = float(input('Insira o segundo número: '))
produto = num1 * num2
divisaoreal = num1 / num2
divisaointeira = num1 // num2
print(f"O produto de {num1} e {num2} é: {produto}")
print(f"A divisão real de {num1} por {num2} é: {divisaoreal}")
print(f"A divisão inteira de {num1} por {num2} é: {divisaointeira}")