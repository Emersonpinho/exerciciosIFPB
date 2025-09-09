valores = []

for i in range(7):
    valor = input(f'Digite o {i+1}° valor:')
    valores += [valor]

for i in range(7, -1, 1):
    print(valores[i])