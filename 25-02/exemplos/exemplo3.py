# Aula Listas e tuplas

# REMOVER - REMOVE

programadores = ['Victor','Julia','Henrique','Caio','Luana','Julia','Jessica']
print(programadores)

programadores.remove('Julia')# Remove qualquer item com a nomenclatura especifica
print(programadores)

print('---------------------')

# REMOVER = POP

programadores2 = ['Victor','Julia','Henrique','Caio','Luana','Jessica']
print(programadores2)
programadores2.pop(5)# Remove posição especifica
print(programadores2)

print('---------------------')

lista = ['Victor','Julia','Henrique','Caio','Luana','Jessica']
for nome in lista:
    if not nome.startswith('J'):# remover itens que tenham uma caracteristica especifica
        print(nome)
 
print('---------------------')
        
#valores variados
pessoa = ['Murilo',19, 1.80]
print(pessoa)

print('---------------------')

# MIN / MAX

num = [5,9,15,36,1,48,4]
print(max(num))
print(min(num))

print('---------------------')

# MIN / MAX - LEN]

programadores3 = ['Victor','Julia','Henrique','Caio','Luana','Jessica']
menorpalavra = min(programadores3, key=len)
maiorpalavra = max(programadores3, key=len)
print(menorpalavra)
print(maiorpalavra)