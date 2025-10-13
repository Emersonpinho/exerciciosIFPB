n = int(input('Digite um valor: '))

for c in range(n, 0, -1):
    for j in range(c, 0, -1):
        print(j, end=' ')
    print()