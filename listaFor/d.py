lista = []

num = 0
valores_lidos = 0
j = 0
soma = 0

while num >= 0:
    num = float(input('Digite as notas aqui: '))

    if num >= 0:
        lista += [num]

    for i in lista:
        valores_lidos += 1

    print(f'Os valores lidos foram {valores_lidos}')

    for i in lista:
        print(i, end=' ')
    print()

    for i in range(valores_lidos - 1, -1, -1):
        print(lista[i], end=' ')
        j += 1

    print()


    for i in lista:
        soma += i
    print(f'A soma de todos os valores foi {soma}')

    
    media = soma / valores_lidos

    print(f'A média de todos os valores foi de {media}')

    for i in lista:
        if i > media:
            print(f'Nota acima da média: {i}')


    for i in lista:
        if i < 7:
            print(f'Notas abaixo de 7: {i}')

    print('Obrigado por usar esse programa.')