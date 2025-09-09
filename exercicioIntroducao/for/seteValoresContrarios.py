valores = []

for i in range(7):
    valor = int(input(f'Digite o {i+1}° valor:'))
    valores.append(valor)

for i in range(6, -1, 1):
    print(valores[i])