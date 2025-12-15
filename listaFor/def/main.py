def saudacao():

    for i in range(3):
        print(f'{i+1} Olá mundo')

def soma(a, b):
    resultado = a + b
    return resultado

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

x = soma(a, b)
print(x)