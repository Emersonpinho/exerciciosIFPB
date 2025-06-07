cont = 1
soma = 0

while cont < 11:
    numPar = int(input('Digite um número positivo: '))

    if numPar % 2 == 0:
        cont += 1
        soma += numPar
    else:
        print(f'ERROR!$#: O número {numPar} é IMPAR')

print(f'A soma de todos os Números PARES: {soma}')