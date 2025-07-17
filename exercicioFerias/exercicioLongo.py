i = 1

menorIdade = 100000
maiorIdade = -10000

sexoMasculino = 0
sexoFeminino = 0

idadeTotal = 0

while True:
    nome = input(f'Digite o nome do {i}° aluno:')
    idade = int(input(f'Digite a idade do {i} aluno:'))
    sexo = int(input(f'Digite o sexo do {i} aluno (1- masculino, 2- Feminino):'))
    
    if sexo == 1:
        sexoMasculino += 1
    elif sexo == 2:
        sexoFeminino += 1    
    
    op = int(input('Deseja continuar? (1- parar 2- continuar)'))
    if op == 1:
        break
    
    if idade > maiorIdade:
        maiorIdade = idade

    elif idade < menorIdade:
        menorIdade = idade

    idadeTotal = idadeTotal + idade
    i += 1

# peguei a contador de interação(i) e cada interação sera contado como um aluno
print(f'Total de ALUNOS:{i}')
print(f'Total de SEXO MASCULINO:{sexoMasculino}')
print(f'Total de SEXO FEMININO:{sexoFeminino}')
# como a variavel 'i' sever para o total de alunos so somei a idade total e dividir pelo total de alunos(i)
print(f'Media de IDADE:{idadeTotal/i:.2f}')
print(f'Maior idade foi {maiorIdade}')
print(f'Menor idade foi {menorIdade}')

