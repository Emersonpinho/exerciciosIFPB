# exercicio ainda imcompleto

nomes = [0] * 800
matriculas = [0] * 800
emails = [0] * 800
cursos = [0] * 800
opcoes = ['Cadastre um aluno', 'Listar todos os alunos', 'Pesquisar um aluno', 'Atualizar os dados de um aluno']
contador = 0

while True:
    print()
    for i in range(4):
        print(f'{i + 1} - {opcoes[i]}')

    op = int(input('\nDigite o que deseja fazer: '))
    
    if op == 1:

        print('\n----Informações do aluno----')
        nomes[contador] = input('Digite o nome do aluno: ')
        matriculas[contador] = int(input('Digite a matricula do aluno: '))
        '''if matriculas[contador] in matriculas:
            matriculas[contador] = 0
            contador -= 1
            print('Matrícula já cadastrada.')
            break'''
        emails[contador] = str(input('Digite o email do aluno: '))
        cursos[contador] = str(input('Digite o curso que o aluno frequenta: '))

        print('\nALUNO CADASTRADO COM SUCESSO!!')

        contador+=1

    elif op == 2:
        print('Lista de todos os alunos')
        for i in range(contador):
            print(nomes[i])

    elif op == 3:
        pesquisar = int(input('Digite a matrícula do aluno: '))

        encontrou = False

        for i in range(contador):
            if matriculas[i] == pesquisar:
                print(f'{matriculas[i]}')
                print(f'{nomes[i]}')
                print(f'{emails[i]}')
                print(f'{cursos[i]}')
                encontrou = True

        if encontrou == False:
            print('Não encontrado')

    elif op == 4:
        atualizar = int(input('Digite a matrícula do aluno: '))

        for i in range(800):
            if matriculas[i] == atualizar:
                nomes[i] = str(input('Digite o nome que deseja mudar: ')) 

    elif op == 5:
        print('saindo....')
        break

