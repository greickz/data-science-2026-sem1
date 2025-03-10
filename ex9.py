# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M matutino, V Vespertino ou N Noturno. Imprima a mensagem "Bom Dia!", 
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Qual o seu turno? M(manhã), V (Vespertino), N(Noite): ').lower().strip()
if turno == 'm':
    print('Bom dia')
elif turno == 'v':
    print('Boa tarde')
elif turno == 'n':
    print('Boa noite')
else:
    print('Turno inválido. Digite M, V ou N.')