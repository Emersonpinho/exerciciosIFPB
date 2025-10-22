lista = [4, 6, 7, 2, 8, 9, 1]
existe = 0

n = int(input('Digite um numero: '))

for i in range(len(lista)):

    if lista[i] == n:
        existe = 1

print(existe)

