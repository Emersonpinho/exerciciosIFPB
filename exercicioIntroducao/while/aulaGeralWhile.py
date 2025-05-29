'''c = 0

while c < 10:
    print(c)
    c += 1

print('fim')'''

n = 1
par = impar = c = 0

while n != 0:
    n = int(input('Digite um valor: '))
    c += 1
    
    if n != 0:

        if n % 2 == 0:
            par += 1
            
        else:
            impar += 1

print(f'Relatorio:\nNúmeros digitados: {c-1}\nNúmeros PARES: {par-1}\nNúmeros IMPARES {impar}')