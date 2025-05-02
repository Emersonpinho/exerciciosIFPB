nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 70:
    print(f'Sua media foi {media:.2f}, APROVADO!')
elif media < 70 and media >= 40:
    print(f'Sua media foi {media:.2f}, PROVA FINAL!')
else:
    print(f'sua media foi {media:.2f}, REPROVADO!')