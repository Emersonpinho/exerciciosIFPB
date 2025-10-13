list = [0]
print('oi')
i = 0
while True:
    n = int(input('Digite um número: '))
    n += list[i]
    
    if n == -1:
        break


print(list[0:i])