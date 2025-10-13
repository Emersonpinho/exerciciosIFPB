soma = 0
expressao = ' '


for c in range(1, 101):
    soma += c

    expressao += str(c)

    if c < 100:
        expressao += '+'
    else:
        expressao += f'={soma}'

print(f'\n{expressao}\n')