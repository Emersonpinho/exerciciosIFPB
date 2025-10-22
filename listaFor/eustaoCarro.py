carros = []
soma = 0

for c in range(1, 11):
    velo = float(input(f'Digite a velocidade do {c} carro em km: '))
    carros += [velo]
    
for i in carros:
    soma += i

media = soma / 10

print(carros)
print(soma)
print(media)
