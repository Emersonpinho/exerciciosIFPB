numero = int(input('Digite um numero para ver sua taboada: '))
cont = 0

for cont in range(1, 11):
    print(f'{numero} * {cont} = {numero*cont}')
    cont += 1
