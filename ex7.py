# Ler duas notas de um aluno, efetuar a média aritmética e, se a média for maior ou igual a 7, informar que o aluno foi aprovado; se a média for maior ou igual a
# 5 mas menor do que 7, informar que o aluno está de exame; se a média for menor do que 5 informar que o aluno foi reprovado.

nota = float(input('Digite a nota: '))
if nota >= 7:
  print('Aluno(a) aprovado')
elif nota >= 5 and nota <7:
  print('Aluno(a) está de recuperação')
else:
  print('Aluno(a) reprovado')