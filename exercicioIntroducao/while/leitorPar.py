cont = 1
soma = 0

while cont < 11:
    numPosi = int(input('Digite um número positivo: '))

    if numPosi % 2 == 0:
        cont += 1
        soma += numPosi
    else:
        print(f'ERROR!$#: O número {numPosi} é IMPAR')

print(f'A soma de todos os Números PARES: {soma}')