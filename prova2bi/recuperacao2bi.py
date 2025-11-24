codigos = [0] * 1000
titulos = [''] * 1000

codigos = [0] * 1000
titulos = [''] * 1000
autores = [''] * 1000
anos = [0] * 1000

contador = 0

op = ['1- Cadastrar um livro', '2- Listar todos os livros', '3- Pesquisar um livro pelo código', '4- Atualizar os dados de um livro', '5- Remover um livro', '6- Listar livros por autor', '7 - SAIR']

while True:

    print('=====MENU=====')
    for c in op:
        print(c)

    print('==============')

    opcao = int(input('Digite sua opção: '))

    if opcao == 7:
        print('\nFechando Programa....')
        break

    elif opcao == 1:
        print('\n=== CADASTRAR LIVRO ===\n')

        if contador == 1000:
            print('Não há mais número de livros.')
        else:
            codigo = int(input('Digite o código do livro: '))
            codigoDuplicado = False

            for i in range(contador):
                if codigos[i] == codigo:
                    print(f'O livro de código [{codigo}] já está cadastrado.')
                    codigoDuplicado = True
                    break

            titulos[contador] = input('Digite o título do livro: ')
            autores[contador] = input('Digite o autor do livro: ')
            anos[contador] = int(input('Digite o ano de publicação: '))
            codigos[contador] = codigo

            contador += 1

            print(f'\nLivro de código [{codigo}] cadastrado com sucesso.\n')

    elif opcao == 2:
        print('\n====LIVROS CADASTRADOS====\n')
        for c in range(contador):
            print(titulos[c])

        print()
    elif opcao == 3:
        pesq = int(input('Digite o codigo para encontrar o livro: '))

        for c in range(contador):
            if codigos[c] == pesq:
                print(f'\nLivro ENCONTRADO: \nTítulo: {titulos[c]}\nCodigo: {codigos[c]}\n')

    elif opcao == 6: