def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        return "Erro: Os valores fornecidos não são números!"