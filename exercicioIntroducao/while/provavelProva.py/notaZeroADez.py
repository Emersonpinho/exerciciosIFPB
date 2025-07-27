while True:
    nota = int(input('Digite uma nota: '))
    if 0 <= nota <= 10:
        print(f'Nota VÁLIDA: {nota}')
        break
    else:
        print(f'Nota INVÁLIDA: {nota}, tente novamente') 