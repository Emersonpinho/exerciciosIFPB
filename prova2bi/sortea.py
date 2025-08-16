numeroSecreto = 76
tentativa = 5
c = 1

while True:
    n = int(input('Digite um número:'))
    
    if n == numeroSecreto:
        print(f'Você acertou o número com {c} tentativas')
        break
    
    
    if n < numeroSecreto:
        print(f'ERROU: número secreto é MAIOR, Restam {tentativa} tentativas')
    else:
        print(f'ERROU: número secreto é MENOR, Restam {tentativa}tentativas')

    c += 1
    tentativa -= 1