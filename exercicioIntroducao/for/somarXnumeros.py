soma = 0
x = int(input('Digite a quantidade de números para somar: '))

for n in range(1, x+1):
    soma += n

print(f'A soma de todos os numeros de 1 até {x} é {soma}')