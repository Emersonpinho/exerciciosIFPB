mult = 1
somaImpar = 0

for n in range(1, 31):

    if n % 2 == 0:
        mult*=n
    else:
        somaImpar += n

print(f'SOMA DOS NUMEROS IMPARES: {somaImpar}')
print(f'MULTIPLICAÇÃO DOS NÚMEROS PARES {mult}')