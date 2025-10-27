conta = {}
livro = {}
aluno = {}
casa = {}
pessoa = {}
animal = {}
veiculo = {}
professor = {}

print('------Informe os dados do BANCO-------')
print()

conta['Número'] = int(input('Digite o número da conta: '))
conta['Títular'] = str(input('Informe o número do titular: '))
conta['Saldo'] = float(input('Digite o saldo da conta: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in conta:
    print(chave, ':', conta[chave])
print()

print('----Informe os dados do LIVRO-----')
print()

livro['Titulo'] = str(input('Digite o título do livro: '))
livro['Autor'] = str(input('Digite o nome do autor: '))
livro['Ano'] = int(input('Informe o ano do livro: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in livro:
    print(chave, ':', livro[chave])
print()

print('---Informe os dados do ALUNO-----')
print()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Curso'] = str(input('Digite o curso que o aluno frequenta: '))
aluno['idade'] = int(input('Digite a idade do aluno: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in aluno:
    print(chave, ':', aluno[chave])
print()

print('---Informe os dados da CASA---')
print()

casa['Número'] = input('Digite o número da casa: ')
casa['Rua'] = str(input('Digite a rua da Casa (ex: Inês dantas wanderlay): '))
casa['cor'] = str(input('Digite a cor da casa: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in casa:
    print(chave, ':', casa[chave])
print()

print('----Informe os dados da PESSOA-----')
pessoa['Nome'] = str(input('Digite o nome da pessoa: '))
pessoa['Idade'] = int(input(f'Digite a idade de {pessoa["Nome"]}: '))
pessoa['Sexo'] = str(input(f'Informe o sexo de {pessoa['Nome']}: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in pessoa:
    print(chave, ':', pessoa[chave])
print()

print('----Informe os dados do ANIMAL----')
animal['Especie'] = str(input('Digite a espécie do animal: '))
animal['Idade'] = int(input('Digite o a idade do animal: '))
animal['Nome'] = str(input('Digite o nome do animal: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in animal:
    print(chave, ':', animal[chave])
print()

print('---Informe os dados do VEÍCULO---')
veiculo['Marca'] = str(input('Digite a marca do veiculo: '))
veiculo['Cor'] =  str(input('Digite a cor do veiculo: '))
veiculo['placa'] = str(input('Digite a placa do veiculo: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in veiculo:
    print(chave, ':', veiculo[chave])
print()

print('---Informe os dados do PROFESSOR---')
professor['Nome'] = str(input('Digite o nome do professor: '))
professor['Aréa de ensino'] = str(input('Digite a aréa de ensino do professor (Ex: Geografia, matemática e etc): '))
professor['Idade'] = int(input('Digite a idade do professor: '))

print('\nINFORMAÇÕES CADASTRADA COM SUCESSO!')
print()

for chave in professor:
    print(chave, ':', professor[chave])
