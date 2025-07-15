i = 0
somaSalario = 0
while True:
    salario = float(input(f'Digite o salario do {i+1}° funcionario (-1 para parar):'))

    if salario == -1:
        break

    somaSalario = somaSalario + salario

    i+=1

print(f'Sua empresa tem {i} funcionarios!')
print(f'A media de salarios da sua empresa é {somaSalario/i}')