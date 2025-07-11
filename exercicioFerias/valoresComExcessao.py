maior = -1000
menor = 1000


while True:
    valor = int(input('Digite um número entre -1000 e 1000(0 para sair):'))
    
    if valor == 0:
        break

    if  -1000 <= valor <= 1000:

        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

    else:
        print('O valor ({valor}) está fora do intervalo')

print(f'O maior valor digitado foi {maior}')
print(f'O menor foi {menor}')
        
