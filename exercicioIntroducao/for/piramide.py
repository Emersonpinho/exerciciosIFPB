n = int(input('Digite um numero para ver sua piramide: '))

print()
for c in range(n, 0, -1):
    for j in range(c, 0, -1):
        print(j, end=' ')
    print()

print()
    
