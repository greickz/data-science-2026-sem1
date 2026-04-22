# Dicionário - Estruturas de Dados

aluno = {
    "Nome": ["João", "Vinícius"], # as chaves são para quando tem mais de um valor
    "Idade": [20, 17],
    "Curso": ["Cyber Security", "Ciência de dados" ]
    
}

print(aluno)
print("-" * 30) 


# Acessando valores pelo nome da "Chave"
print(aluno["Nome"])
print(aluno["Idade"])
print("-" * 30) 

# Adiciona um novo par chave-valor ("email": "exemplo@email.com")
aluno["Email"] = ["joao@email.com", "vini@email.com"]
print(aluno)

print("-" * 30) 


# modificar um valor
aluno["Idade"] = [21,17]
print(aluno)
print("-" * 30) 

# Remover um item pelo nome da chve

del aluno["Curso"]
print(aluno)

print("Idade" in aluno) # TRUE
print("Curso" in aluno) # FALSE


for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
print("-" * 30) 
# Lista de dicionário

alunos = [
    {
    "Nome": ["João"],
    "Idade": [20],
    "Curso": ["Cyber Security" ]
    },
    {
    "Nome": ["Vinícius"],
    "Idade": [17],
    "Curso": ["Ciência de dados" ]
    },
    {
    "Nome": ["Jonas"],
    "Idade": [13],
    "Curso": ["Manutenção de micro" ]
    }
]

for aluno in alunos:
    print("Dados do aluno: ")
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")
    print("-" * 30) 