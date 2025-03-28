idade = int(input('informe sua idade: '))

if idade < 16:
    print(f'Você tem {idade} e é um não eleitor!')
elif 18 <= idade < 65:
    print(f'Você tem {idade} e é um eleitor obrigatorio! ')
elif (16 > idade < 18) or (idade > 65):
    print(f'Você tem {idade} e é um eleitor facutativo!')
