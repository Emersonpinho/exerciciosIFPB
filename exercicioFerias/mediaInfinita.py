media = 0
i = 0

while True:
    num = int(input('Digite um número para ver sua média (0 para sair): '))
    if num == 0:
        break

    if num % 2 == 0:
        media = media + num
        i += 1

if i > 0:
    print(f'A media final dos pares: {media/i}')
else:
    print('Nenhum número digiado!')