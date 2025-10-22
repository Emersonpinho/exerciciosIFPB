valor = []
max = 0
mini = 9000000000000000000000

for c in range(5):
    n = int(input('Digite um valor: '))

    valor += [n]

for c in range(5):
    if valor[c] > max:
        max = valor[c]
    elif valor[c] < mini:
        mini = valor[c]


print(valor)
print(max)
print(mini)