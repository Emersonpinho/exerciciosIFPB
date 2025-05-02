def desligar():
    print('Desligando...')

def reiniciar():
    print('reiniciando...')

def suspender():
    print('suspender...')

acoes = {
    'desligar': desligar,
    'reiniciar': reiniciar,
    'suspender': suspender
}

comando = input('digite oque deseja fazer (desligar, reiniciar ou suspender)')

acoes.get(comando, lambda: print('desconhecido')) ()
