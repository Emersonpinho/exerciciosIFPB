n1 = int(input('Digite a primeira nota: (0/100) '))
p1 = int(input('Digite seu peso: '))
n2 = int(input('Digite a segunda nota: (0/100) '))
p2 = int(input('Digite seu peso: '))
n3 = int(input('Digite a terceira nota: (0/100) '))
p3 = int(input('Digite o seu peso: '))

mediaPon = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(f'A media ponderada é: {mediaPon:.1f}')