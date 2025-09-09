lista = []

c = 1
while True:
    num = float(input(f'Digite o valor do {c}° Produto (0 para sair):'))
    if num == 0:
        break

    lista.append(num)


print(lista)