n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

comando = input('Digite a operação que deseja fazer (+, -, * or /): ')

match comando:
    case '+':
        print(f'{n1} + {n2} = {n1+n2}')
    case '-':
        print(f'{n1} - {n2} = {n1-n2}')
    case 'x' | '*':
        print(f'{n1} * {n2} = {n1*n2}')
    case '/' | '%' | '//':
        if n1 and n2 != 0:
            print(f'{n1} / {n2} = {n1//n2}')
        else:
            print('não é possivel dividir por zero')