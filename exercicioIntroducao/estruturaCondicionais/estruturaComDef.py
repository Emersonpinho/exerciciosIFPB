def ler_dois_numeros():
    num = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    return num, num2

def somar():
    num, num2 = ler_dois_numeros()
    resultado = num + num2
    print(f'{num} + {num2} = {resultado}')

def multiplicar():
    num, num2 = ler_dois_numeros()
    resultado = num * num2
    print(f'{num} * {num2} = {resultado}')

def subtrair():
    num, num2 = ler_dois_numeros()
    resultado = num - num2
    print(f'{num} - {num2} = {resultado}')

def dividir():
    num, num2 = ler_dois_numeros()

    if num2 == 0:
        print('Não é possivel dividir por 0(zero)!')
    else:
        resultado = num // num2
        print(f'{num} / {num2} = {resultado}')

def exponeciar():
    num, num2 = ler_dois_numeros()

    resultado = num ** num2
    print(f'{num} ** {num2} = {resultado}')

comando = {
    '+': somar,
    '*': multiplicar,
    '-': subtrair,
    '/': dividir,
    '**': exponeciar
}

comandos = input('Digite o comando desejado (+, *, -, / ou **): ')

comando.get(comandos, lambda: print('Comando desconhecido!')) ()