lista = []

for c in range(5):
    n = input('Digite um número: ')
    lista += [n]

print('Lista antes da Troca: ', lista)

x = int(input(f'Digite a posiçao x (0 - {len(lista-1)}): '))
y = int(input(f'Digite a posição y: 0 - {len(lista-1)}: '))


aux = lista[y]
lista[y] = lista[x]
lista[x] = aux

print('lista depois da troca: ', lista)
