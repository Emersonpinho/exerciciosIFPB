soma = 0
expre = ''

for c in range(1, 101):
    soma += c

    if c < 100:
        expre += str(c) + '+'
    else:
        expre += str(c) + '=' 

print()
print(expre, end='')
print(soma)
print()