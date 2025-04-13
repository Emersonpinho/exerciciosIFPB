n1 = int(input('Digite a Primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

p1 = int(input(f'Digite o Peso da 1° nota (primeira nota {n1})'))
p2 = int(input(f'Digite o Peso da 2° nota (Segunda nota {n2})'))
p3 = int(input(f'Digite o Peso da 3° nota (terceira nota {n3})'))

mediap = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(f'A media ponderada é {mediap:.2f}')