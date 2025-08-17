# QUESTÂO 3
x = 100
soma = 0
i = 1

while True:
    n = int(input('Digite um número inteiro:'))
    soma += n
    if soma > x:
        print(f'A soma total dos Números: {soma}\nQuantidade de Números informados: {i}')
        break
    i+=1
