i = 0
somaAlt = 0
while True:
    alt = float(input(f'Digite a altura do {i+1} jogador (0 para parar):'))
    
    if alt == 0:
        break
    
    somaAlt = somaAlt + alt

    i+= 1

mediaAlt = somaAlt / i
print(f'Sua equipe é composta por {i} jogadores!')
print(f'A média de altura é {mediaAlt:.2f}')