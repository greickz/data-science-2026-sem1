def media(num):
    try:
        if not num:
            raise ValueError("Lista vazia! Não é possível calcular a média.")
        return sum(num) / len(num)
    except ValueError as e:
        return str(e)