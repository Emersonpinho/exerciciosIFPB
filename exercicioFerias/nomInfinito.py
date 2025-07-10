total = ''
cont = 0

while True:
    pessoas = input('Digite o nome da pessoa ou(s para SAIR): ')

    if pessoas.lower() == 's':
        break

    total = total + pessoas + '\n'

    cont += 1

print(f'Você digitou o nome de {cont} Pessoas')
print('Nome das pessoas:')
print(total)
