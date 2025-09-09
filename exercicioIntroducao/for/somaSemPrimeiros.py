soma = 0
operacao = ''

for c in range(1, 101):
    soma += c

    if c < 100:
        operacao += str(c) + '+'
    else:
        operacao += str(c) + '=' + str(soma)
    
    
print(operacao)