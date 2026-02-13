produtos = []
dados = ["Código", "Nome", "Preço", "Categoria"]
lixeira = []

while True:
    print("\nMENU:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Pesquisar")
    print("4 - Atualizar")
    print("5 - Remover")
    print("6 - Adicionar na lixeira")
    print("7 - Listar a lixeira")
    print("8 - Restaurar item da lixeira")
    print('9 - Sair')


    op = int(input("Digite a sua opção"))
    
    if op == 1:
        codigo = input("Digite o codigo: ")

        existe = False
        for p in produtos:
            if p["Código"] == codigo:
                existe = True
                break
        
        if existe:
            print("Codigo já cadastrado!")
        else:
            nome = input("Digite o nome: ")
            preco = input("Digite o preço: ")
            cat = input("Digite a categoria: ")

            produto = {
                "Código": codigo,
                "Nome": nome,
                "Preço": preco,
                "Categoria": cat
            }

        produtos.append(produto)
        print("Produto cadastrado")

    elif op == 2:

        if len(produtos) > 0:

            for i in produtos:
                print('=================')
                for j in dados:
                    print(f'{j} - {i[j]}')
        
        else:
            print('Nenhum produto cadastrado.')

    elif op == 3:
        if len(produtos) > 0:
            Codpesq = input("Digite o codigo do produto: ")
            existe = False

            for i in produtos:
                if Codpesq == i['Código']:
                    existe = True
                    break

            if existe == True:

                for p in produtos:
                    if p["Código"] == Codpesq:
                        for j in dados:
                            print(f'{j} - {p[j]}')
            else:
                print()
                print("Produto não encontrado")

        else:
            print('Nenhum produto cadastrado')

    elif op == 4:

        if len(produtos) > 0:

            codigo = str(input('Digite o código do produto: '))
            existe = False
            posicao = 0

            for i in produtos:
                if codigo == i['Código']:
                    existe = True
                    break
                posicao += 1

            if existe == True:

                for i in dados:
                    novo = str(input(f'Novo {i} ou ENTER para continuar: '))
                    if novo != '':
                        produtos[posicao][i] = novo
                    else:
                        print('Não cadastrado (espaço vazio)')

            else:
                print('Aluno não encontrado')
        else:
            print('Produto não cadastrado.')

    elif op == 5:

        if len(produtos) > 0:

            codigo = str(input('Digite o código do produto que deseja remover: '))
            existe = False
            alvo = None

            for i in produtos:
                if codigo == i['Código']:
                    existe = True
                    alvo = i
                    break
                    
            if alvo != None:
                produtos.remove(alvo)
                lixeira.append(alvo)
                print('Aluno removido com sucesso!')
            else:

                print('Produto não encontrado.')

        else:
            print('Nenhum aluno cadastrado.')

    elif op == 6:

        
        if len(lixeira) > 0:

            for i in lixeira:
                print('=================')
                for j in dados:
                    print(f'{j} - {i[j]}')
        
        else:
            print('Nenhum produto cadastrado.')

    elif op == 8:
        if len(produtos) > 0:

            codigo = str(input('Digite o código do produto que deseja restaurar: '))
            existe = False
            alvo = None

            for i in lixeira:
                if codigo == i['Código']:
                    existe = True
                    alvo = i
                    break

            if alvo != None:

                lixeira.remove(alvo)
                produtos.append(alvo)

            else:

                print('Produto não encontrado.')

        else:
            print('Nenhum item na lixeira.')

    elif op == 9:
        print('Saindo')
        break

    else:
        print('Opção invalida')