while True:
    valor1 = float(input('Digite um número entre 1 e 50:'))
    
    if 1 <= valor1 <= 50:
        break
    print('VALOR INVÁLIDO, TENTE NOVAMENTE')

while True:
    valor2 = float(input('Digite o segundo número entre 1 e 50:'))

    if 1 <= valor2 <= 50:
        break
    print('VALOR INVÁLIDO, TENTE NOVAMENTE')

print(f'{valor1} + {valor2} = {valor1+valor2}')

    