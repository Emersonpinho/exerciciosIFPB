n =  int(input('Digite um número para ver sua taboada: '))
op = int(input('DIGITE A OPERAÇÃO\n1 - MULTIPLICAÇÃO\n2 - DIVISÃO\n3 - SUBTRAÇÃO\n4 - ADIÇÃO\nDigite sua opção aqui:'))

if op == 1:
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
elif op == 2:
    for c in range(1, 11):
        print(f'{c} / {n} = {c//n}')
elif op == 3:
    for c in range(1, 11):
        print(f'{c} - {n} = {c-n}')
elif op == 4:
    for c in range(1, 11):
        print(f'{n} + {c} = {n+c}')
else:
    n = int(input('Valor invalido!!, tente novamente: '))