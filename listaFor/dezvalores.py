lista = []

for i in range(3):
    num = int(input(f'Digite o {i+1}° numero: '))
    lista += [num]

soma = 0
subtracao = lista[0]
multiplicacao = 1
divisao = lista[0]

for i in range(len(lista)):
    soma += lista[i]
    multiplicacao *= lista[i]

for c in range(1, len(lista)):
    divisao /= lista[c]
    subtracao -= lista[c]

print(f'Soma:{soma}')
print(f'subtração:{subtracao}')
print(f'Multiplicação:{multiplicacao}')
print(f'Divisão:{divisao}')
    