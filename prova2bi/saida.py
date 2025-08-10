n = int(input('Digite um número: '))
cont = 1
fat = 1
x = 1

while cont <= n:
    cont2 = cont
    while cont2 <= n:
        fat *= cont2
        cont2 += 1
    x += (cont//fat)
    cont += 1
print(x)