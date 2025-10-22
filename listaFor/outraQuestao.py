'''A população da cidade de Lucas cresce 0,4% ao ano e tem uma população 
de 5 mil habitantes, enquanto a população da cidade de Igor cresce 0,9% ao ano 
e tem uma população de 3 mil habitantes, escreva um programa para determinar 
em quantos anos a cidade de Igor ultrapassará a cidade de Lucas em habitantes.'''

igor = 3000
lucas = 5000

for c in range(1, 10000000):
    lucas *= 1.004
    igor *= 1.009
    ano += 1
    
    if igor > lucas:
        break

print(f'A cidade de igor em {c}')
