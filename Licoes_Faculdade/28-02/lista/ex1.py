def calculadora():
    while True:
        try:
            num1 = input('Digite o primeiro número (ou "x" para sair): ')
            if num1.lower() == 'x':
                print("Até breve!")
                break
            num2 = input('Digite o segundo número (ou "x" para sair): ')
            if num2.lower() == 'x':
                print("Até breve!")
                break
            operacao = input('Digite a operação (+, -, *, /) ou "x" para sair: ')
            if operacao.lower() == 'x':
                print("Até breve!")
                break
            num1 = float(num1)
            num2 = float(num2)
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero.")
                resultado = num1 / num2
            else:
                print("Erro: Operação inválida. Use '+', '-', '*' ou '/'.")
                continue
            print(f'{num1} {operacao} {num2} = {resultado}')
        except ValueError:
            print("Erro: Tipo de dado inválido. Certifique-se de que os números são válidos.")
        except ZeroDivisionError as e:
            print(e)
calculadora()