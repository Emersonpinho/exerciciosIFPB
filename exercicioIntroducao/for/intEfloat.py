numInt = []
numFloat = []

c = 1
while True:
    num = input(f'Digite o valor do {c}° Produto (0 para sair):')

    if num == 0:
        break

    lista += [num]
    c += 1
