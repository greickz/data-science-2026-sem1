# Solicite ao usuário uma palavra e verifique se a letra &quot;a&quot; está presente nela, utilizando o operador in.

palavra = input('Digite uma palavra: ')
letraa = ['a', 'A', 'ã', 'Ã', 'á', 'Á', 'à', 'À', 'â', 'Â']
if any(caractere in palavra for caractere in letraa):
    print('A letra "a" está em sua palavra.')
else:
    print('Não tem nenhuma letra "a" em sua palavra.')