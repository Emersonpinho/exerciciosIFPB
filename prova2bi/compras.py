valorTot = 0
d = 0
c = 0

while True:
    compra = float(input(f'Digite o valor da {c+1}ª Compra: '))

    if compra < 0:
        compra = float(input('Valor não pode ser NEGATIVO:'))

    valorTot += compra

    if compra == 0:
        print('Compras cadastradas!')
        print(f'valor: {valorTot}')
        break
    
    if valorTot > 1000:
        desconto = valorTot - (valorTot * 0.10)
        d += 1

    c += 1

if d > 0:
    print(f'Sua compra utrapasso R$: 1000\nVocê tem desconto de 10%: {desconto}')