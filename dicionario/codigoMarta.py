livros = []
lixeira = []

op = 0
while op != 7:
    print('|=============menu================|')
    print('|1. Cadastrar um livro            |')
    print('|2. Listar todos os livros        |')
    print('|3. Pesquisar um livro pelo código|')
    print('|4. Atualizar os dados de um livro|')
    print('|5. Remover um livro              |')
    print('|6. Listar livros por autor       |')
    print('|7. Sair                          |')
    print('|8. Listar livros da lixeira      |')
    print('|=================================|')
    
    op = int(input('opção: '))

    # 1 - CADASTRAR
    if op == 1:
        if len(livros) < 1000:
            codigo = int(input('codigo: '))
            igual = False
            for livro in livros:
                if livro["codigo"] == codigo:
                    igual = True
                    break
            if igual:
                print('codigo ja cadastrado')
            else:
                titulo = input('qual o titulo: ')
                autor = input('qual o autor: ')
                ano = int(input('ano do livro: '))
                
                livro = {
                    'codigo': codigo,
                    'titulo': titulo,
                    'autor': autor,
                    'ano': ano
                }
                livros.append(livro)
                print('livro cadastrado com sucesso')
        else:
            print('cadastros cheios !!!!')
        print()

    # 2 - LISTAR
    elif op == 2:
        if len(livros) > 0:
            for livro in livros:
                print('codigo:', livro['codigo'])
                print('titulo:', livro['titulo'])
                print('autor:', livro['autor'])
                print('ano:', livro['ano'])
                print('========================')
        else:
            print('nenhum livro cadastrado')
        print()

    # 3 - PESQUISAR POR CÓDIGO
    elif op == 3:
        if len(livros) > 0:
            codigo = int(input('codigo de pesquisa: '))
            encontrado = False
            for livro in livros:
                if livro["codigo"] == codigo:
                    print('livro encontrado:', livro)
                    encontrado = True
                    break
            if not encontrado:
                print('não tem livro cadastrado com esse codigo')
        else:
            print('nenhum livro cadastrado')
        print()

    # 4 - ATUALIZAR
    elif op == 4:
        if len(livros) > 0:
            codigo = int(input('codigo do livro pra atualizar: '))
            pos = -1
            for i in range(len(livros)):
                if livros[i]["codigo"] == codigo:
                    pos = i
                    break
            if pos == -1:
                print('livro nao encontrado')
            else:
                print('dados atuais:', livros[pos])
                confirmar = input('deseja atualizar [S|N]: ')
                if confirmar.upper() == 'S':
                    livros[pos]["titulo"] = input('novo titulo: ')
                    livros[pos]["autor"] = input('novo autor: ')
                    livros[pos]["ano"] = int(input('novo ano: '))
                    print('livro atualizado com sucesso')
        else:
            print('nenhum livro cadastrado')
        print()

    # 5 - REMOVER
    elif op == 5:
        if len(livros) > 0:
            codigo = int(input('codigo do livro pra remover: '))
            pos = -1
            for i in range(len(livros)):
                if livros[i]["codigo"] == codigo:
                    pos = i
                    break
            if pos == -1:
                print('livro nao encontrado')
            else:
                confirmar = input('deseja apagar [S|N]: ')
                if confirmar.upper() == 'S':
                    lixeira.append(livros[pos])
                    del livros[pos]
                    print('livro removido')
        else:
            print('nenhum livro cadastrado')
        print()

    # 6 - BUSCAR POR AUTOR
    elif op == 6:
        if len(livros) > 0:
            autor_buscar = input('nome do autor: ')
            achou = False
            for livro in livros:
                if livro["autor"] == autor_buscar:
                    print('codigo:', livro['codigo'])
                    print('titulo:', livro['titulo'])
                    print('autor:', livro['autor'])
                    print('ano:', livro['ano'])
                    print('========================')
                    achou = True
            if not achou:
                print("nenhum livro encontrado desse autor")
        else:
            print('nenhum livro cadastrado')
        print()

    # 8 - LISTAR LIXEIRA
    elif op == 8:
        if len(lixeira) > 0:
            for livro in lixeira:
                print('codigo:', livro['codigo'])
                print('titulo:', livro['titulo'])
                print('autor:', livro['autor'])
                print('ano:', livro['ano'])
                print('========================')
        else:
            print('lixeira vazia!!')
        print()

    # 7 - SAIR
    elif op == 7:
        print("saindo do sistema...")
