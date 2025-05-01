func = input('Digite a função (ligar, desligar ou reniciar): ').upper()

if func == 'DESLIGAR':
    print('Desligando...')
elif func == 'LIGAR':
    print('LIGANDO...')
elif func == 'RENICIAR':
    print('Reniciando...')
else:
    print(f'operação invalida ({func})')

while func not in ('LIGAR', 'DESLIGAR', 'RENICIAR'):
    func = input('Digite a função (ligar, desligar ou reniciar): ').upper()
    if func == 'DESLIGAR':
        print('Desligando...')
    elif func == 'LIGAR':
        print('LIGANDO...')
    elif func == 'RENICIAR':
        print('Reniciando...')
    else:
        print(f'operação invalida ({func})')