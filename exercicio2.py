# Crie uma função que receba uma lista de tuplas, onde cada tupla contém o nome de um aluno e sua nota, e retorne o nome do aluno com a maior nota.

def maior_nota():
    num_alunos = int(input("Digite quantos alunos serão comparados: "))
    lista_alunos = []
    lista_notas = []
    for alunos in range(num_alunos):
        aluno = input('Digite o nome do aluno: ')
        nota = float(input(f'Digite a nota do {aluno}: '))
        lista_alunos.append(aluno)
        lista_notas.append(nota)
        maior_nota = lista_notas[0]
        aluno_maior_nota = lista_alunos[0]
        maior_nota = lista_notas[0]
    aluno_maior_nota = lista_alunos[0]
    for i in range(1, num_alunos):
        if lista_notas[i] > maior_nota:
            maior_nota = lista_notas[i]
            aluno_maior_nota = lista_alunos[i]
    print(f'O aluno com a maior nota é {aluno_maior_nota} com a nota {maior_nota}.')
maior_nota()