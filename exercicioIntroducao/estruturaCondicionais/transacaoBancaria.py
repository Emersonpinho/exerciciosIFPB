saldo = float(input('Digite seu saldo: '))
op = int(input('Qual operação deseja fazer? \n|RETIRAR[1]\n|DEPOSITAR[2]\n: '))


if op == 1:
    valorOp = float(input('Digite o valor da operação: '))
    novoSaldo =  saldo - valorOp
    if novoSaldo < 0:
        print('conta estourada')
    else:
        print(novoSaldo)
    
elif op == 2:
    valorOp = float(input('Digite o valor da operação: '))
    novoSaldo =  valorOp + saldo
    print(novoSaldo)
else:
    print('operação invalida')