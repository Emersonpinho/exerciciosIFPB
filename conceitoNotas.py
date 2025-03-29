nota = float(input('Digite a sua Nota: '))

if nota < 3:
    print(f'Você tirou Nota {nota}: Conceito E')
elif (nota >= 3 ) and (nota < 6):
    print(f'Você tirou Nota {nota}: conceito D')
elif (nota >= 6) and (nota < 8):
    print(f'Você tirou Nota {nota}: Conceito C')
elif (nota >= 8) and (nota < 9):
    print(f'Sua Nota foi {nota}: Conceito B')
elif nota >= 9:
    print(f'Sua Nota foi {nota}: Conceito A')
