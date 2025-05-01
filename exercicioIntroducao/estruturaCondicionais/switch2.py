def ligar():
    print('open system')

def desligar():
    print('off system')

def reniciar():
    print('reset system')

def erro():
    print('ERROR: comando invalido:')

acoes = {
    'ligar': ligar,
    'desligar': desligar,
    'reniciar': reniciar
}
comando = input('digite o camando (ligar, deligar, reniciar): ').lower()

acoes.get(comando, erro)()
