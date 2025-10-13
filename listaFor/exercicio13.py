soma = 0

for c in range(85, 908):
    if c % 2 == 0:
        print(c, end=' ')
    
    soma +=c

print(f'\nO resultado da soma {soma}')