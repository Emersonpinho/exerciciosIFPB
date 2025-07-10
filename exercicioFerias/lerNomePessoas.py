cont = 1
total = ''

while cont <= 20:
    pessoas = input(f'Digite o número da {cont}° pessoa:')
    total = total + pessoas + '\n'
    cont += 1

print(total)