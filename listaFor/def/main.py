# funções simples

def saudacao():

    for i in range(3):
        print(f'{i+1} Olá mundo')

def soma(a, b):
    return a + b

'''a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

print(soma(a, b))'''

# parametros opcionais

def sauda_nome(nome = 'usuario'):
     return print(f'Olá {nome}')

print(sauda_nome())