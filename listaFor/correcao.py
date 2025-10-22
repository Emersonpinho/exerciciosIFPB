while True:
    qt = int(input('Digite o número da questão (Digite 0 para sair): '))

    if qt == 0:
        break

    elif qt == 1:
        produtos = []
        precos = []
        totalGasto = 0
        maisCaro = 0
        nomeMaisCaro = ''

        # Entrada de dados
        for i in range(5):
            pd = input('Digite o nome do produto: ')
            pc = float(input('Digite o valor do produto: '))

            produtos.append(pd)
            precos.append(pc)

        # Cálculos
        for c in range(5):
            totalGasto += precos[c]
            if precos[c] > maisCaro:
                maisCaro = precos[c]bas
                nomeMaisCaro = produtos[c]

        media = totalGasto / 5

        # Produtos acima da média
        pdAcimaDaMedia = []
        pcAcimaDaMedia = []
        for c in range(5):
            if precos[c] > media:
                pdAcimaDaMedia.append(produtos[c])
                pcAcimaDaMedia.append(precos[c])

        # Saída
        print('\n--- RESULTADOS ---')
        print(f'O total gasto foi: R$ {totalGasto:.2f}')
        print(f'Média dos preços: R$ {media:.2f}')
        print(f'O produto mais caro foi: {nomeMaisCaro} (R$ {maisCaro:.2f})')
        print('Produtos acima da média:')
        for i in range(len(pdAcimaDaMedia)):
            print(f' - {pdAcimaDaMedia[i]} (R$ {pcAcimaDaMedia[i]:.2f})')
        print('------------------\n')
