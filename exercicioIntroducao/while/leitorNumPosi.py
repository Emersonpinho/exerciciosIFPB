cont = 1
soma = 0

while cont < 11:
    numPosi = int(input('Digite um número positivo: '))

    if numPosi > 0:
        cont += 1
        soma += numPosi
    else:
        print(f'ERROR!#$: Número {numPosi} não é POSITIVO')

print(f'A soma de todos os números POSITIVOS digitados é {soma}')