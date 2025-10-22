qt = int(input('Digite o número da questão (Digite 0 para sair): '))

while True:
    if qt == 0:
        break

    elif qt == 1:

        produtos = []
        precos = []
        pdAcimaDaMedia = []
        pcAcimaDaMedia = []
        nomeMaisCaro = ''
        totalGasto = 0
        maisCaro = 0

        for i in range(5):
            pd = input('Digite o nome do produto: ')
            pc = float(input('Digite o valor do produto: '))

            produtos += [pd]
            precos += [pc]

        for c in range(5):
            totalGasto += precos[c]

            if produtos[c] > maisCaro:
                maisCaro = produtos[c]

        media = totalGasto / 5

        for c in range(5):
            if precos[c] > maisCaro:
                maisCaro = precos[c]
                nomeMaisCaro = produtos[c]

        print(f'O total gasto foi: {totalGasto}')
        print(f'O produto acima da media: {pdAcimaDaMedia}, preços do produtos {pcAcimaDaMedia}')
        print(f'O produto mais caro foi: {maisCaro}')
                 