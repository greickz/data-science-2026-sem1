# Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até que o usuário informe um valor válido.

nota = float(input('Digite uma nota entre 0 e 10: '))
while nota < 0 or nota > 10:
    nota = float(input('Valor inválido, digite uma nota entre 0 e 10: '))
print('Nota válida')