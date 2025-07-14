soma = 0
i = 0

while True:
    mediaAluno = float(input(f'Digite a media do {i+1}° aluno (digite -1 para sair)'))
    
    if mediaAluno == -1:
        break

    soma = soma + mediaAluno 
    i += 1

mediaTurma = soma / i
print(f'A media da turma é {mediaTurma}')