somaPosi = 0
quantImpar = 0

for num in range(1, 11):
    valor = int(input('Digite um valor: '))

    if valor > 1:
        somaPosi += num
    else:
        quantImpar += 1

print(f'A soma dos números positivos: {somaPosi}')
print(f'A Quantidade dos números negativos {quantImpar}')
    