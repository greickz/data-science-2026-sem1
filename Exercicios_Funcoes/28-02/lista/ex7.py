def pegar(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Erro: Índice fora do intervalo da lista!"