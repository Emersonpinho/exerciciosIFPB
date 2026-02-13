alunos = []
dados = ['Matrícula', 'Nome', 'Email', 'Curso']
while True:
    print('1 - Cadastrar aluno')
    print('2 - Listar todos os alunos')
    print('3 - Pesquisar um aluno')
    print('4 - Atualizar os dados de um aluno')
    print('5 - Remover aluno')
    op = int(input('Digite o que deseja realizar: '))

    if op == 1:
        
        matricula = str(input('Digite a matrícula do aluno: '))
        nome = str(input('Digite o nome do aluno: '))
        email = str(input('Digite o email do aluno: '))
        curso = str(input('Digite o curso do aluno: '))
        existe = False

        for matri in alunos:
            if matricula == matri['Matrícula']:
                existe = True
                break
        
        if existe == False:

            cadastro = {
                'Matrícula' : matricula,
                'Nome' : nome,
                'Email' : email,
                'Curso' : curso
            }

            alunos.append(cadastro)

        if existe == True:
            print('Matrícula já existente.')

    elif op == 2:

        if len(alunos) > 0:

            for aluno in alunos:
                print('---------------------------')
                for dado in dados:
                
                    print(f'{dado} - {aluno[dado]}')

        else:
            print('Nenhum aluno cadastrado!')
    
    elif op == 3:
        
        achou = False
        posicao = 0
        if len(alunos) > 0:
            matri = str(input('Digite a matrícula do aluno que deseja pesquisar.'))
            for i in alunos:
                
                if matri == i['Matrícula']:
                    achou = True
                    break
                posicao += 1
            
            if achou == True:
                
                for i in dados:
                    print(f'{alunos[posicao][i]}')
            
            else:
                print('Matrícula não encontrada.')

        else:
            print('Nenhum aluno cadastrado.')

    elif op == 4:

        achou = False
        posicao = 0
        if len(alunos) > 0:
            matri = str(input('Digite a matrícula do aluno que deseja atualizar: '))
            for i in alunos:
                
                if matri == i['Matrícula']:
                    achou = True
                    break
                posicao += 1
            
            if achou == True:
                
                for i in dados:
                    novo = str(input(f'Novo {i} ou ENTER para continuar: '))
                    if novo != '':
                        alunos[posicao][i] = novo
                print('Aluno atualizado com sucesso.')
            
            else:
                print('Matrícula não encontrada.')

        else:
            print('Nenhum aluno cadastrado.')

    elif op == 5:

        achou = False
        posicao = 0
        if len(alunos) > 0:
            matri = str(input('Digite a matrícula do aluno que deseja remover: '))
            for i in alunos:
                
                if matri == i['Matrícula']:
                    achou = True
                    break
                posicao += 1
            
            if achou == True:
                
                alunos.pop(posicao)
                print('ALuno removido com sucesso.')
            
            else:
                print('Matrícula não encontrada.')

        else:
            print('Nenhum aluno cadastrado.')

    elif op == 6:

        if len(alunos) > 0:

            nome = str(input('Digite o para saber os alunos do mesmo nome: '))
            achou = False

            for i in alunos:
                if nome == i['Nome']:
                    achou = True

            if achou == True:

                for i in alunos:
                    print('---------------')
                    if nome == i['Nome']:
                        for j in dados:
                            print(f'{i[j]}')

            else:
                print('Nenhum aluno com esse nome cadastrado')

        else:
            print('Nenhum aluno cadastrado.')

    elif op == 7:
        print('Pessoal, esse código serve de base pra próxima prova de Geam, certo? Estudem bastante, bons estudos! Jesus ama vcs <3')
        break