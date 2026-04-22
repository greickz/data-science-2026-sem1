def contarcaracteres(texto, caractere):
    try:
        if not isinstance(texto, str):
            raise TypeError("O texto fornecido não é uma string!")
        return texto.count(caractere)
    except TypeError as e:
        return str(e)