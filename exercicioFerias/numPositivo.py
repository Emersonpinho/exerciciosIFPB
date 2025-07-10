cont = 1
soma = 0

while cont <= 10:
    num = int(input('Digite um número:'))

    if num > 0:
        soma += num
        cont += 1
    else:
        print('Numero digitado não é positivo')

print(soma)