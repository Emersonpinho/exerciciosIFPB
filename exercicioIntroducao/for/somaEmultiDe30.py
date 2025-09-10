somaImpar = 0
multiPar = 1

for c in range(1, 31):
    if c % 2 == 1:
        somaImpar += c
    else:
        multiPar *= c

print(f'Soma dos números imapares: {somaImpar}\nResultado da Multiplicação dos pares {multiPar}')